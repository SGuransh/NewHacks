import re
<<<<<<< HEAD
from pdfminer.high_level import extract_pages, extract_text

=======
import pdfminer
from pdfminer.high_level import extract_text
>>>>>>> d3cb9bb3958da6aeab103c679a95906af16a696e
class Parser:
    result = None
    courses = None
    days_dict = None
    def __init__(self, filePath: str):
        self.filePath = filePath
        self.parseForList()
        self.getTimeTable()
        self.getCoursesByDays()


    def parseForList(self):
        text = extract_text(self.filePath)
        _split = text.split("\n")
        start = 0
        for text in _split:
            if text == 'Currently Enrolled':
                break
            start += 1

        new = _split[start + 2:]

        result = []
        for item in new:
            if (item not in ['', 'ACTIVITY', 'TIME', 'LOCATION', 'INSTRUCTOR', '(In Person)', 'TBA']) and \
                    ('https://map.utoronto.ca/?' not in item) and ('#' not in item) and ('✏' not in item) and \
                    ('Credit' not in item) and ('empty' not in item) and ('enrol' not in item) and (
                    'ACTIIVTY' not in item):
                result.append(item)
        i = 0
        for item in result:
            if "\x0c" in item:
                result[i] = item.removeprefix('\x0c')
            i += 1

        self.result = result

    def getTimeTable(self):
        courses = {}
        index = 0
        first = True
        course = {}
        prev_course = "prev"
        for item in self.result:
            if re.search("\(Fall\)|\(Winter\)|\(Full Session\)", item):
                if not first:
                    courses[prev_course] = course
                first = False
                prev_course = item
                course = {}
            if re.search("LEC", item):
                t = self.getNextLectureAndTimes(index)
                course["LEC"] = t[0]
            if re.search("TUT", item):
                t = self.getNextLectureAndTimes(index)
                course["TUT"] = t[0]
            index += 1
        self.courses = courses

    def getNextLectureAndTimes(self, start_index: int) -> (dict, int):
        # if('TUT' and 'LEC' not in timetable_list[start_index]):
        #     return(None, start_index)
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        dic = {}
        lecture = self.result[start_index]
        # dic[lecture] = [[timetable_list[start_index+1] + timetable_list[start_index+2]]]
        lecture_times = [self.result[start_index + 1] + self.result[start_index + 2].split(' ')[0]]
        end_i = start_index + 3
        for i in range(start_index + 3, len(self.result), 2):
            # print(timetable_list[i].split(' '))
            if self.result[i].split(' ')[0] not in days:
                break
            else:
                lecture_times.append(self.result[i] + self.result[i + 1])
            end_i = i
        locations = []
        if 'TUT' not in lecture:
            end_i += 2
        while '\uf08e' in self.result[end_i]:
            locations.append(self.result[end_i])
            end_i += 1
        # print(timetable_list[end_i])
        dic_lecture_times = {}
        for i in range(len(lecture_times)):
            if locations:
                dic_lecture_times[lecture_times[i]] = locations[i].removesuffix(" \uf08e")
        dic[lecture] = dic_lecture_times
        if 'TUT' in lecture:
            end_i -= 1
        return (dic, end_i)

    def getCoursesByDays(self):
        days_dict = {'Monday': {}, 'Tuesday': {}, 'Wednesday': {}, 'Thursday': {}, 'Friday': {}}
        for course in self.courses:
            for lecture in self.courses[course]['LEC']:
                dic_of_dates = self.courses[course]['LEC'][lecture]
                # print(dic_of_dates)
                course_name = course
                for date in dic_of_dates:
                    day = date.split(' ')[0]
                    location = dic_of_dates[date]
                    days_dict[day][course_name.split(' ')[0]] = location
        self.days_dict = days_dict

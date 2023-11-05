import re
from pdfminer.high_level import extract_pages, extract_text

# for page_layout in extract_pages("timetable.pdf"):
#     for element in page_layout:
#         print(element)


text = extract_text("timetable.pdf")
_split = text.split("\n")
start = 0
for text in _split:
    if text == 'Currently Enrolled':
        break
    start += 1

new = _split[start+2:]

result = []
for item in new:
    if (item not in ['', 'ACTIVITY', 'TIME', 'LOCATION', 'INSTRUCTOR', '(In Person)', 'TBA']) and \
            ('https://map.utoronto.ca/?' not in item) and ('#' not in item) and ('✏' not in item) and \
            ('Credit' not in item) and ('empty' not in item) and ('enrol' not in item) and ('ACTIIVTY' not in item):
        result.append(item)

current_list = result
i = 0
for item in result:
    if "\x0c" in item:
        result[i] = item.removeprefix('\x0c')
    i += 1

x = 0
# for item in result:
#     if item =='TUT 0103':
#         print('INDEX IS' + str(x))
#     x+=1
# print(result[104])

# print(result)

def getTimeTable(timetable_list:list) -> dict:
    courses = {}
    index = 0
    first = True
    course = {}
    prev_course = "prev"
    for item in timetable_list:
        if re.search("\(Fall\)|\(Winter\)|\(Full Session\)", item):
            print(item)
            if not first:
                courses[prev_course] = course
            first = False
            prev_course = item
            course = {}
        if re.search("LEC", item):
            t = getNextLectureAndTimes(timetable_list, index)
            course["LEC"] = t[0]
            print(t[0])
        if re.search("TUT", item):
            t = getNextLectureAndTimes(timetable_list, index)
            course["TUT"] = t[0]
            print(t[0])
        index += 1
    return courses

courses={'CSC207H1 F (Fall) Software Design': {'LEC': {'LEC 0201': {'Tuesday 1:00PM -2:00PM': 'EM 001', 'Thursday 1:00PM -2:00PM': 'EM 001'}}, 'TUT': {'TUT 5101': {}}}, 'CSC236H1 F (Fall) Introduction to the': {'LEC': {'LEC 0201': {'Monday 12:00PM -1:00PM': 'MP 202', 'Friday 12:00PM -1:00PM': 'MP 202'}}, 'TUT': {'TUT 0204': {'Wednesday 12:00PM -1:00PM': 'BF 215'}}}, 'MST233H1 F (Fall) Viking Cultures': {'LEC': {'LEC 0101': {}}}, 'NMC253H1 F (Fall) Egyptian Myths': {'LEC': {'LEC 0101': {}}}, 'STA237H1 F (Fall) Probability, Statistics': {'LEC': {'LEC 0101': {'Monday 1:00PM -3:00PM': 'MS 2158', 'Wednesday 2:00PM -3:00PM': 'AH 100'}}, 'TUT': {'TUT 0104': {'Wednesday 1:00PM -2:00PM': 'NF 119'}}}, 'MAT235Y1 Y (Full Session) Multivariable': {'LEC': {'LEC 0201': {'Monday 10:00AM -11:00AM': 'RW 110', 'Wednesday 10:00AM -11:00AM': 'RW 110', 'Friday 10:00AM -11:00AM': 'RW 110'}}, 'TUT': {'TUT 0303': {'Tuesday 12:00PM -1:00PM': 'OI 5230'}}}, 'CSC209H1 S (Winter) Software Tools and': {'LEC': {'LEC 0201': {'Tuesday 3:00PM -4:00PM': 'MY 150', 'Thursday 3:00PM -4:00PM': 'MY 150'}}, 'TUT': {'TUT 0301': {}}}, 'CSC258H1 S (Winter) Computer': {'LEC': {'LEC 5101': {}}, 'TUT': {'TUT 5301': {}}}, 'CSC263H1 S (Winter) Data Structures and': {'LEC': {'LEC 0301': {'Tuesday 1:00PM -2:00PM': 'NL 6', 'Thursday 1:00PM -2:00PM': 'BA 1130'}}, 'TUT': {'TUT 0103': {'Friday 12:00PM -1:00PM': 'ES B149'}}}, 'MAT223H1 S (Winter) Linear Algebra I': {'LEC': {'LEC 0301': {}}, 'TUT': {'TUT 0401': {}}}}

def getCoursesByDays(courses:dict)-> dict:
    days_dict = {'Monday': {}, 'Tuesday': {}, 'Wednesday':{}, 'Thursday':{}, 'Friday':{}}
    for course in courses:
        for lecture in courses[course]['LEC']:
            dic_of_dates = courses[course]['LEC'][lecture]
            # print(dic_of_dates)
            course_name = course
            for date in dic_of_dates:
                day = date.split(' ')[0]
                location = dic_of_dates[date]
                days_dict[day][course_name.split(' ')[0]] = location
    return days_dict







def getNextLectureAndTimes(timetable_list:list, start_index:int) -> (dict, int):
    # if('TUT' and 'LEC' not in timetable_list[start_index]):
    #     return(None, start_index)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    dic = {}
    lecture = timetable_list[start_index]
    # dic[lecture] = [[timetable_list[start_index+1] + timetable_list[start_index+2]]]
    lecture_times = [timetable_list[start_index + 1] + timetable_list[start_index + 2].split(' ')[0]]
    end_i = start_index+3
    for i in range(start_index+3, len(timetable_list), 2):
        # print(timetable_list[i].split(' '))
        if timetable_list[i].split(' ')[0] not in days:
            break
        else:
            lecture_times.append(timetable_list[i]+timetable_list[i+1])
        end_i = i
    locations = []
    if 'TUT' not in lecture:
        end_i += 2
    while '\uf08e' in timetable_list[end_i]:
        locations.append(timetable_list[end_i])
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

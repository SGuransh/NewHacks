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

# print(result)

def getTimeTable(timetable_list:list) -> dict:
    lecture_name = ''
    dic = {}
    index = 0
    while index < len(timetable_list):
        while 'LEC' not in timetable_list[index]:
            if 'TUT' in timetable_list[index]:
                break
            lecture_name += timetable_list[index]
            index += 1
        lectures, index = getNextLectureAndTimes(result, index)
        index+=1
        dic[lecture_name] = lectures
        lecture_name = ''
    return dic
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
    return (dic, end_i)

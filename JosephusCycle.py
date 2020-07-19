import file_reader
import zipfile
import csv
import chardet
import os

def get_people_list_txt(place):#获得初始游戏者列表
    with open(place) as fp: 
        people_str = fp.readlines()
    people_list = []
    for line in people_str:
        line = list(line.strip().split(' '))
        people_list.append(line)
    return (people_list)

def get_people_list_zip(place):
    people_list = []
    with zipfile.ZipFile(place, 'r') as zf: 
        first_file_name = zf.namelist()[0]
        people_betye = zf.read(first_file_name)
        people_str = people_betye.decode(chardet.detect(people_betye)['encoding'])#解码 
    temp = list(people_str.strip().split('\r'))
    for x in temp:
        x = list(x.strip().split(' '))
        people_list.append(x)
    return (people_list)

def get_people_list_csv(place):
    people_list = []
    with open(place) as csvfile: 
        readcsv = csv.reader(csvfile, delimiter = ',')
        for row in readcsv:
            people_list.append(row)
    return (people_list)

def get_people_list(path):
    file = os.path.splitext(path)
    filename, type = file
    if type == '.txt':
        return get_people_list_txt(path)
    elif type == '.csv':
        return get_people_list_csv(path)
    elif type == '.zip':
        return get_people_list_zip(path)
    else:
        pass
class Person():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

class Josephus():
    def __init__(self):
        self.people = []
    
    def append(self, Person):
        self.people.append(Person)
        return self.people

    def get_killed_person(self, start_num, interval):
        total_num = len(self.people)
        i = 0
        while i < (total_num - 1):
            start_num = (start_num + interval) % len(self.people)#测试
            start_num -= 1
            yield self.people[start_num] #生成器代替return
            del self.people[start_num]
            i += 1
            if start_num == -1:
                start_num = 0

        #return (self.people[0])

def get_person_list(gamer_list):#获得对象列表
    person_list = Josephus()
    for i in (range(len(gamer_list))):#行数
            #j = len(people_list[0])#列数
        temp = Person(gamer_list[i][0], gamer_list[i][1], gamer_list[i][2])
            #print(temp.age)
        person_list.append(temp)
    return person_list

if __name__ == '__main__':
    #people_list = getdadaForJC1.get_people_list('py.txt')
    people_list = get_people_list('py.txt')
    person_list = get_person_list(people_list)
    start_num = int(input('the start number is:'))
    interval = int(input('the interval is:'))
    killed_person = person_list.get_killed_person(start_num, interval)
    for x in killed_person:
        print('out ==> name:',x.name, 'gender:',x.gender, 'age:',x.age)
    survival = person_list.people[0]
    print('survival ==> name:',survival.name, 'gender:',survival.gender, 'age:',survival.age)


'''
import JosephusCycle1  #测试文件
def test(people_list, start_num, interval):
    person_list = JosephusCycle1.get_person_list(people_list)
    killed_person = person_list.get_killed_person(start_num, interval)
    killed_list = []
    for x in killed_person:
        killed_list.append(x.name)
    #survival = person_list.people[0]
    return killed_list


people_list = [[1,2,3],[4,5,6],[7,8,9]]    
start_num = int(input('the start number is:'))
interval = int(input('the interval is:'))
dead_list = test(people_list, start_num, interval)
assert(dead_list == [4,1])
'''
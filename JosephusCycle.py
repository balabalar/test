import zipfile
import csv
import chardet
import os 

class read(object):
    def get_people_list(self):
        raise NotImplementedError

class txt_reader(read):
    def __init__(self, path):
        self.path = path

    def get_people_list(self):
        with open(self.path) as fp: 
            people_str = fp.readlines()
        people_list = []
        for line in people_str:
            line = list(line.strip().split(' '))
            people_list.append(line)
        return (people_list)

class csv_reader(read):
    def __init__(self, path):
        self.path = path

    def get_people_list(self):
        people_list = []
        with open(self.path) as csvfile: 
            readcsv = csv.reader(csvfile, delimiter = ',')
            for row in readcsv:
                people_list.append(row)
        return (people_list)

class zip_reader(read):
    def __init__(self, path):
        self.path = path

    def get_people_list(self):
        people_list = []
        with zipfile.ZipFile(self.path, 'r') as zf: #打开zip中的.txt文件
            first_file_name = zf.namelist()[1]
            people_betye = zf.read(first_file_name)
            people_str = people_betye.decode(chardet.detect(people_betye)['encoding'])#解码 
        temp = list(people_str.strip().split('\r'))
        for x in temp:
            x = list(x.strip().split(' '))
            people_list.append(x)
        return (people_list)
'''
    def get_people_list(self):  #打开zip中的.csv文件
        people_list = []
        with zipfile.ZipFile(place, 'r') as zf: 
            first_file_name = zf.namelist()[0]
            people_betye = zf.read(first_file_name)
            people_str = people_betye.decode(chardet.detect(people_betye)['encoding'])#解码 
        temp = list(people_str.replace('\r','').split('\n'))
        for x in temp:
            x = list(x.strip().split(','))
            people_list.append(x)
        return (people_list)
'''

def reader(path):
    file = os.path.splitext(path)
    filename, type = file
    if type == '.txt':
        return txt_reader(path).get_people_list()
    elif type == '.csv':
        return csv_reader(path).get_people_list()
    elif type == '.zip':
        return zip_reader(path).get_people_list()
    else:
        pass


class person():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

def get_person_list(gamer_list):#获得对象列表
    person_list = Josephus()
    for i in (range(len(gamer_list))):#行数
            #j = len(people_list[0])#列数
        temp = person(gamer_list[i][0], gamer_list[i][1], gamer_list[i][2])
            #print(temp.age)
        person_list.append(temp)
    return person_list

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

if __name__ == '__main__':
    people_list = reader('py.txt')
    person_list = get_person_list(people_list)
    start_num = int(input('the start number is:'))
    interval = int(input('the interval is:'))
    killed_person = person_list.get_killed_person(start_num, interval)
    for x in killed_person:
        print('out ==> name:',x.name, 'gender:',x.gender, 'age:',x.age)
    survival = person_list.people[0]
    print('survival ==> name:',survival.name, 'gender:',survival.gender, 'age:',survival.age)


#*************约瑟夫类测试***********************
def test(people_list, start_num, interval):
    person_list = get_person_list(people_list)
    killed_person = person_list.get_killed_person(start_num, interval)
    killed_list = []
    for x in killed_person:
        killed_list.append(x.name)
    #survival = person_list.people[0]
    return killed_list

people_list = [[1,2,3],[4,5,6],[7,8,9]]    
dead_list1 = test(people_list, -1, 1)
assert(dead_list1 == [7,1]) #start_num = -1，interval = 1
dead_list2 = test(people_list, 1, -1)
assert(dead_list2 == [7,1]) #start_num = -1，interval = -1

#*************读取文件reader类测试**************
people_list0 = reader('py.txt')
assert people_list0[0][1] == '女'
assert people_list0[44][2] == '34'

people_list1 = reader('py.csv')
assert people_list1[0][0] == '妮妮'
assert people_list1[9][2] == '25'

people_list3 = reader('people.zip')
assert people_list3[0][1] == '女'
assert people_list3[44][2] == '34'

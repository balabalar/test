def get_people_list():
    fp = open('py.txt')  #file points
    people_str = fp.readlines()#with语句
    fp.close()
    people_list = []
    for line in people_str:
        line = list(line.strip().split(' '))
        people_list.append(line)
    return (people_list)


def get_survival(start_num, people_list, interval):  #逗号后加空格
    total_num = len(people_list)
    for i in range(total_num - 1):
        start_num = (start_num + interval) % len(people_list)#测试
        start_num -= 1
        print('Killd_person:', people_list[start_num])#可以用return代替
        del people_list[start_num]
        if start_num == -1:
            start_num = 0
    return (people_list[0])


__metaclass__ = type


class Person:
    def __init__(self, name):
        self.name = name
        self.age = 0  #self._name 变私有变量
        self.gender = 0
    def getName(self):
        print("the survival's name is:%s" % self.name)
    
    @property #变成属性
    def getAge(self):
        print("%s's age is:%s" % (self.name, age))
        return self.age

    def getGender(self, gender):
        print("%s's gender is:%s" % (self.name, gender))


if __name__ == '__main__':
    people_list = get_people_list()
    start_num = int(input('the start number is:'))
    interval = int(input('the interval is:'))
    survival = get_survival(start_num, people_list, interval)
    name, gender, age = survival[0], survival[1], survival[2]
    survival = Person(name)
    survival.getName()
    survival.getGender(gender)
    #survival.getAge(age)
    print(survival.getAge)

    assert (int(age) < 100), "the survival's age is older than 100"

class Josephus():
    def __init__(self):
        self.people = []
    def append(self,Person):
        self.people.append(Person)
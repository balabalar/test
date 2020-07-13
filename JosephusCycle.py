def get_peopel_list():
    f = open('py.txt')
    peopel_str = f.readlines()
    f.close()
    peopel_list = []
    for line in peopel_str:
        line = list(line.strip().split(' '))
        peopel_list.append(line)
    return(peopel_list)

def get_survival(start_num,peopel_list,interval):
    total_num = len(peopel_list)
    for i in range(total_num - 1):
        start_num = (start_num + interval) % len(peopel_list) 
        start_num -= 1
        print ('Killd_person:',peopel_list[start_num])
        del peopel_list[start_num]
        if start_num == -1: 
            start_num = 0
    return(peopel_list[0])


__metaclass__ = type

class Person:
    def __init__(self,name):
        self.name = name
    
    def getName(self):
        print("the survival's name is:%s"%self.name)

    def getAge(self,age):
        print("%s's age is:%s"%(self.name,age))

    def getGender(self,gender):
        print("%s's gender is:%s"%(self.name,gender))
        

if __name__ == '__main__':
    peopel_list = get_peopel_list()
    start_num = int(input('the start number is:'))
    interval = int(input('the interval is:'))
    survival = get_survival(start_num,peopel_list,interval)
    name, gender, age = survival[0], survival[1], survival[2]
    survival = Person(name)
    survival.getName()
    survival.getGender(gender)
    survival.getAge(age)

    assert(int(age) < 100),"the survival's age is older than 100"





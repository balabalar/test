import random
num = random.randint(1,101)
guess = 0
while 1:
    num_in = input('please input a integer that is in 1 to 100:')
    guess += 1

    if not num_in.isdigit():
        print('please input a integer.')
    elif int(num_in)<0 or int(num_in) > 100:
        print('this num should be in 1 to 100.')
    elif guess > 4:
        print('times out.')
        break
    else:
        if num == int(num_in):
            print('the answer is %d,it takes only %d times ,congratulations!'%num%guess)
            break
        elif num > int(num_in):
            print('your answer is less.')
        elif num < int(num_in):
            print('your answer is bigger.')
        else:
            print('sth wrong')

 
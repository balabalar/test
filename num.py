
print("请输入一个整数：")
num = int(input())

if num ==10:
    print("您输入的数字是：%d"%num)
    print('you are clever')
elif num > 10:
    print("您输入的数字是：%d"%num)
    print('this num is more than 10')
elif num < 10:
    print('您输入的数字是：%d'%num)
    print('this num is less than 10')
else:
    print('stupid')

# [in1, in2] = input().split()
# num1 = float(in1)
# num2 = float(in2)
# print(num1/num2)

# print('6')
# print('rhoda1023')


# in1 = int(input())
# in2 = int(input())

# print(in1*(in2 % 10))
# print(in1*int((in2/10) % 10))
# print(in1*int(in2/100))
# print(in1*in2)

# [in1, in2] = input().split()


#ori_num = int(input())
#err_num = int(input())
#if err_num != 0:
#    not_work = True
#    err_button = list(map(int, input().split(' ')))
#else:
#    not_work = False
#    err_button = 0
#
#if err_num == 10:
#    correct = True
#else:
#    correct = False
#
#correct_count = 0
#count_plus = 0
#count_minus = 0
#nor_button= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#now = 100
#
#answer = []
#
#if not_work:
#    for i in range(err_num):
#        nor_button.remove(err_button[i])
#else:
#    nor_button = nor_button
#
#for i in range(len(nor_button)):
#    nor_button[i] = str(nor_button[i])
#
#k = 0
#count_plus = 0

#num1 = int(input())
#
#if ((num1 % 4) == 0) & ((num1 % 100) != 0):
#    print('1')
#elif (num1 % 400) == 0:
#    print('1')
#else:
#    print('0')

num1, num2, num3 = map(int, input().split(' '))

program = True
i = 0

if num2 >= num3:
    print('-1')
    program = False
else:
    i = int(num1 / (num3 - num2))

while program:

    if (num1 + (num2 * i)) < (num3 * i):
        program = False
        print(i)
    i = i + 1

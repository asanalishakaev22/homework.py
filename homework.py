#1 задача
nums = input().split()
act =input()#
for i in range(len(nums)):
    nums[i] = int(nums[i])
if act =='сумма':
    print(nums[0] *nums[1] *[nums2])
#2 задача
nums = input().split()
act=input()
for i in range(len(nums)):
    nums[i] = int(nums[i])
if act =='максимум':
    print(min(nums))
elif act =='минимум':
    print(min(nums))
elif act =='среднеарифметическое':
    print(sum(nums)/3)
#3 задача
meters = int(input())
act = input()
if act == 'мили':
    print (meters * 0.000621371)
if act == 'дюймы':
    print(meters * 39.3701)
if act == 'ярды':
    print(meters * 1.09361)
# 4 задача
diaposon = input().split()
fot i in range(2):
    diaposon[i] = int(diaposon[i])
for i in range(diaposon[0], diaposon[1] + 1):
    if i % 7 ==0:
        print(i, end='')
print()
#5 задача
diaposon = input().split()
count = 0
fot i inrange(2):
    diaposon[i] = int(diaposon[i])
for i in range (diaposon[0], diaposon[1] + 1):
    print(i, end='')
print()
for i in range(diaposon[1], diaposon[0] - 1, - 1 ):
    print(i, end='')
print()
for i in range(diaposon[0], diaposon[1] + 1):
    if i % 5 == 0:
        count += 1
print(count)

# 6 задача
diaposon = input().split()
for i in range(2):
    diaposon[i] = int(diaposon[i]):
for i in range(diaposo[0], diaposon[1] + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0
        print('Fizz')
    elif i % 5 == 0
        print('Buzz')
    else:
        print(i)-







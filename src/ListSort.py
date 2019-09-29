def getDigitSum(x):
    digs = list(str(x))
    sum = 0
    for i in range(len(digs)):
        sum += int(digs.pop())
    return sum

n = int(input())

nums = input().split(' ')
num_tuples = list()
for i in range(n):
    num = int(nums.pop())
    num_tuple = (getDigitSum(num),num)
    num_tuples.append(num_tuple)
num_tuples.sort(key = lambda tupl: (tupl[0], tupl[1]))
num_tuples.reverse()
for i in range(n):
    print(num_tuples.pop()[1],end=' ')
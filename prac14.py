import random
def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))
    return res
num = 10
start = 100
end = 200
print(Rand(start, end, num))l1 = [5,6,77,45,22,12,24]

l1 = [x for x in l1 if x%2!=0]
print(l1)

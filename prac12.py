import random
my_list = [i for i in range(0,10) if i%2==0]
output = random.sample(my_list,5)
print("your list is:",output)
item_list = [12,24,35,70,88,120,155]
new_list = []
for i in item_list:
    if i not in [0,2,4,6]:
        new_list.append(i)
print(new_list)
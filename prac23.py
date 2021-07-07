lst = [12,24,35,24,88,120,155]
lt = set(lst)
lst = list(lt)
lst.sort()
lst.pop(1)

print(lst)
start = int(input("Enter Start range:"))
end = int(input("Enter End range:"))
for i in range(start, end+1):
    if ((i % 7 == 0) & (i % 5 != 0)):
        print(i, "is Devided by 7 and Not Multiply of 5.")

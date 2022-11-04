def happy(num, counter):
    num = str(num)
    total = 0
    for x in range(len(num)):
        total += int(num[x])**2
    print(num, total)
    if total == 1: 
        print("happy number!")
        return
    if counter == 500: 
        print("sad number ): ")
        return
    happy(total, counter + 1)


happy(
    int(input("input happy number: ")),
    0
)
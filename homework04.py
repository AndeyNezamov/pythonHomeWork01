number = int(input("Введите число: "))
result = 1
while result<=number:
    if result%2 == 0:
        print(result, end=" ")
        result+=1
    else:result+=1
while True:
    a = int(input())
    if a == 0:
        break
    for i in range(1,a+1):
        if i == a:
            print(i)
        else:
            print(i, end=" ")
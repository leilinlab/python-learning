for i in range(1, 6):
    print(i)


for i in range(10, 1, -2):
    print(i)


for i in range(1, 3):
    print(f"第{i}天")
    for j in range(1, 4):
        print(f"  第{j}节课")


for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}",end=" ")
    print()


for i in range(1, 6):
    for j in range(1, i + 1):
        print("*",end="")
    print()


for i in range(6, 1, -1):
    for j in range(1, i):
        print("*",end="")
    print()


for i in range(1, 10, 2):
    for j in range(1, i + 1):
        print("*",end="")
    print()


r = range(1, 10, 2)
lenR= len(r)
for i in r:
    for k in range(lenR - 1):
        print(" ",end="")
    for j in range(1, i + 1):
        print("*",end="")
    print()
    lenR -= 1
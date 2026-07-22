count = 1

while count <= 5:
    print(f"第{count}天：我正在学习AI开发")
    count+=1


count = 5

while count>=1:
    print(count)
    count -= 1


count = 1
while True:
    print(count)
    if count >=3:
        break
    count += 1

count = 0
while count < 5:
    count += 1
    if count ==3:
        continue
    print(count)
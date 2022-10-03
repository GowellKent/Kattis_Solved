a = int(input())
b = input().split(" ")
t = 0
for x in range(a):
    if int(b[x]) < 0:
        t+=1
print(t)
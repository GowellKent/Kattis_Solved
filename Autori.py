strIn = input().split("-")
newStr=""
for a in range(len(strIn)):
    newStr += strIn[a][0]
print(newStr)
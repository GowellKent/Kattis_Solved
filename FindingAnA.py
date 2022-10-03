s=str(input())
teks=""
for index, letters in enumerate(s):
    if letters == 'a':
        print(s[index:len(s)])
        break
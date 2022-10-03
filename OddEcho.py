words = []
num = int(input())
for i in range(num):
    words.append(input())
for x in range(len(words)):
    if x % 2 == 0:
        print(words[x])
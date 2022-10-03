G, T, N = map(int, input().split())
items = map(int, input().split())
print(int(0.9*(G-T))-sum(items))
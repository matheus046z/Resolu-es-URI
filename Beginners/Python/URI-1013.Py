a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

mab = (a + b + abs(a-b)) / 2
mbc = (b + c + abs(b-c)) / 2
maior = int((mab + mbc + abs(mab - mbc)) / 2)

print(str(maior) + " eh o maior")

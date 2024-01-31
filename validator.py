ans = 0
for i in range(12):
    number = input()
    if (int(number[0]) + 1 == int(number[-1])) or (int(number[0]) - 1 == int(number[-1])):
        ans += 1
print(ans)

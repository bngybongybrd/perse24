shake = 0
while True:
    if shake < 12:
        shake += int(input())
    else:
        print(shake-12)
        break

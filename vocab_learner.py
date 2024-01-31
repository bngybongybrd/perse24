words = int(input())
total = 0
interactions = 5
while True:
    if words >= 5:
        total += interactions
        interactions += 5
        words -= 5
    else:
        total += interactions-5+words
        break
print(total)
        
        

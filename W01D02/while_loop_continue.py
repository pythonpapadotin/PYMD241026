age = 5
while age <= 18:
    age += 1
    if age in [10, 15]:
        continue
    print(f'Age is {age}')

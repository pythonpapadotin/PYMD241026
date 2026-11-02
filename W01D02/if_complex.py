marks = int(input('Give me your marks'))

if marks >= 90:
    print('A')
else:
    # marks are less than 90
    if marks >= 80:
        print('B')
    else:
        # marks are less than 80
        if marks >= 70:
            print('C')



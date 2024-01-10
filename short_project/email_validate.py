with open('file/read.txt', 'r') as f:
    content = f.readlines()
    print(content[3])
    c = 0
    d = 0
    for i in content[3]:
        if i == '@':
            ar = content[3].index(i)
            print("position of @:",ar)
            c += 1
        elif i == '.':
            dot = content[3].index(i)
            print("position of dot:",dot)
            d += 1
        else:
            continue
    if c < 1:
        print("Invalid email format")
    elif c == 1:
        #print("valid email")
        if d > 0:
            if ar < dot:
                print("valid email")
            else:
                print("Incomplete email")
        else:
            print("Invalid email format")
    else:
        print("Invalid email format...only one @ is allowed")
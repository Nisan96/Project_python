def char1_validate(char1,email):
    list_char1 = []
    count = 0
    for c in email:
        count += 1
        if c == char1:
            i = count-1
            list_char1.append(i)
        else:
            continue
    return list_char1

def char2_validate(char2,email):
    list_char2 = []
    count = 0
    for c in email:
        count += 1
        if c == char2:
            i = count-1
            list_char2.append(i)
        else:
            continue
    return list_char2


"""
if __name__ == "__main__":
    with open('read.txt', 'r') as f:
        content = f.readlines()
        print(content[3])
    ar = char1_validate('@',content[3])
    dot = char2_validate('.',content[3])
    print("index of '@' :",ar)
    print("index of '.' :", dot)
    if ar[-1] > dot[-1]:
        print("Not recommended")
"""

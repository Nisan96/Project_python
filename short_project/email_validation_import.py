from email_validation import char1_validate,char2_validate

def position_validate(c,at, dt):
    for a in at:
        for d in dt:
            if d == 0:
                return "E-Mail Address does not appear to be valid!"
            elif d == a + 1:
                return "'.' used at wrong position in this email"
            elif d == a - 1:
                return "E-Mail Address does not appear to be valid!"
            else:
                continue
    if dt[-1] > at[0]:
        if dt[-1] == len(c) - 1:
            return "'.' used at wrong position in this email"
        elif len(dt) > 1:
            x = 1
            for q in dt:
                if q == dt[x] - 1:
                    return "E-Mail Address does not appear to be valid!"
                else:
                    if dt[x] == dt[-1]:
                        return "valid email"
                    x += 1
                    continue
        else:
            return "valid email"
    else:
        return "E-Mail Address does not appear to be valid!"






if __name__ == "__main__":
    with open('file/read.txt', 'r') as f:
        content = f.readlines()
        print(content[3])
        f.close()
    ar = char1_validate('@',content[3])
    dot = char2_validate('.',content[3])
    print("index of '@' :",ar)
    print("index of '.' :", dot)
    print(len(content[3]))

    if len(ar) > 1:
        if ar[0] == 0:
            print("Please Enter a part followed by '@'. this email is Incomplete")
        else:
            print("a part following '@' should not contain the symbol of '@'")
    elif len(ar) == 1:
        if ar[0] == 0:
            print("Please Enter a part followed by '@'. this email is Incomplete")
        elif ar[0] == len(content[3]) - 1:
            print("Please Enter a part following '@'. this email is Incomplete")
        else:
            if len(dot) == 1:
                if dot[0] == 0:
                    print("E-Mail Address does not appear to be valid!")
                elif dot[0] == len(content[3]) - 1:
                    print("'.' used at a wrong position")
                else:
                    p = position_validate(content[3],ar, dot)
                    print(p)
            elif len(dot) == 0:
                print("this email missing an '.'")
            else:
                p = position_validate(content[3],ar, dot)
                print(p)
    else:
        print("this email missing an '@'")



from email_validation import char1_validate,char2_validate

if __name__ == "__main__":
    with open('read.txt', 'r') as f:
        content = f.readlines()
        print(content[3])
        f.close()
    ar = char1_validate('@',content[3])
    dot = char2_validate('.',content[3])
    print("index of '@' :",ar)
    print("index of '.' :", dot)
    if len(ar) > 1:
        print("Error: only one '@' is applicable")
    elif len(ar) == 1:
        if ar[0] == 0:
            print("Error: Incomplete email")
    elif len(ar) == 0:
        print("Error: one '@' is compulsory in email")
    else:
        print("Error: Multiple '@' is not allowed in email")


    if dot[0] == 0:
        print("Error: Email don't seem to be valid")
    else:
        pass

    for a in ar:
        for d in dot:
            if d == a + 1 or d == a - 1:
                print("Error: character position not allowed")
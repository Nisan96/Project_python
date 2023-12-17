p = int(input('purchase amount:'))
a = int(input('enter age:'))
g = input("enter gender:")
pm = input("enter payment method:")

if p > 1000:
    if a >= 50:
        if g in ['female','Female','ladies','Ladies']:
            print("no free item for older citizen")
            if pm in ['card','Card']:
                print("10% dicount")
            elif pm in ['cash','Cash']:
                print("20% discount")
            else:
                print("payment method invalid")
        elif g in ['Male','male','Gents','gents']:
            print("no free item for older citizen")
            if pm in ['card', 'Card']:
                print("10% dicount")
            elif pm in ['cash', 'Cash']:
                print("20% discount")
            else:
                print("payment method invalid")
        else:
            print("Invalid gender")
    else:
        if g in ['female','Female','ladies','Ladies']:
            print("Chocolate is free for you")
            if pm in ['card','Card']:
                print("10% dicount for card payment")
            elif pm in ['cash','Cash']:
                print("20% discount for cash payment")
            else:
                print("payment method invalid")
        elif g in ['Male','male','Gents','gents']:
            print("Cake is free for you")
            if pm in ['card', 'Card']:
                print("10% dicount for card payment")
            elif pm in ['cash', 'Cash']:
                print("20% discount for cash payment")
            else:
                print("payment method invalid")
        else:
            print("invalid gender")
else:
    print("purchase amount is very low for getting any facility....sorry")



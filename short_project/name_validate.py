#n = "13ffghfh9"
def name_validate(n):
    s = n[0]
    try:
        st = int(s)
        if type(st) == int:
            return "name shouldn't start with number"
    except Exception as e:
        count = 0
        for i in n:
            #print(i)
            try:
                t = int(i)
                if type(t) == int:
                    return "it's number in name"
            except Exception as e:
                count += 1
                if count == len(n) - 1:
                    return "name is valid"
                else:
                    continue



if __name__ == "__main__":
    with open('read.txt', 'r') as f:
        content = f.readlines()
        print(content[0])
        f.close()
    name = name_validate(content[0])
    print(name)


#n = "13ffghfh9"
def name_validate(n):
    try:
        if type(int(n)) == int:
            return "Numbers can't be Name"
        elif type(int(n[0])) == int:
            return "name shouldn't start with number"
    except Exception as e:
        try:
            if type(int(n[0])) == int:
                return "name shouldn't start with number"
        except Exception as en:
            count = 0
            for i in n:
                # print(i)
                try:
                    t = int(i)
                    if type(t) == int:
                        return "Name contains number"
                except Exception as e:
                    count += 1
                    if count == len(n) - 1:
                        return "name is valid"
                    else:
                        continue


if __name__ == "__main__":
    with open('file/read.txt', 'r') as f:
        content = f.readlines()
        print(content[0])
        f.close()
    name = name_validate(content[0])
    print(name)


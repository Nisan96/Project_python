'''
file = open('read.txt', 'r')
content = file.readlines()
c = "Idoprogramming"
print(content)
print(len(content[1]))
print(len(content[0]))
print(len(c))

l = [1,'df','d',8]
print(l[-1])
'''
with open('file/read.txt', 'r') as f:
    content = f.readlines()
    ch = content[3]
    w = content[1]
    print(content[3])
    print(len(ch))
    print(len(w))
    print(content[4])
    print(len(content[4]))



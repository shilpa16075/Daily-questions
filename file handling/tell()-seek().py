with open("demo.txt",'r')as f:
    print(f.tell())
    f.read()
    print(f.tell())
    f.seek(0)
    print(f.tell())
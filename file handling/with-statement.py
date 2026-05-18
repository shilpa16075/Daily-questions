# with statement automatically close a file even if an exception/error occurs inside the block
with open('demo.txt','r') as f:
    data = f.read()
    print(data)


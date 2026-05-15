# append mode : add at the end of the file
file = open('demo.txt','a')   # append mode
file.write("If there's something worst then failure, it's regret" )
print(file)
file.close()
print('text successfully added ')
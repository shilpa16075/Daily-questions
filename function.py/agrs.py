def arbitary_para(*args):
    print(args)     # all the parameter are stored in tuple and are not allowed to changed later.
    total = sum(args)
    print(f'The numbers recieved in the agrs are {args}')
    print(total)
arbitary_para(1,2,3,4,5)


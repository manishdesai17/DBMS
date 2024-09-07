import  matrix_opration
t=True
while(t):
    print("1.Display Matrix:")
    print("2.Addition Matrix:")
    print("3.Exit")
    c=int(input("Enter your choice:"))
    if(c==1):
        matrix_opration.Initialize_matrix()
    elif(c==2):
        matrix_opration.Addition_matrix()
    elif(c==3):t=False
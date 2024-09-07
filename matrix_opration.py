a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
c=[[],[],[3,4,5]]
def Initialize_matrix():
    print("  First Matrix")
    for i in range(3):
        for j in range(3):
            print(" ", a[i][j], end="   ")
        print("\n")
    print("  Second Matrix")
    for i in range(3):
        for j in range(3):
            print(" ", b[i][j], end="   ")
        print("\n")

def Addition_matrix():
    print("Addition of Matrix")
    for i in range(3):
        for j in range(3):
            print(" ", a[i][j] + b[i][j], end="   ")
        print("\n")
def Multipicaton_matrix():
    print("Multipicaton of Matrix")
    for i in range(3):
        for j in range(3):

          for k in range(3):
             c[i][j]=c[i][j]+(a[i][k]*b[k][j])
             print(c[i][j])
Multipicaton_matrix()






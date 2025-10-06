from fractions import Fraction
r = int(input("enter the number of rows: "))
c = int(input("enter the number of columns: "))
mat = []
mat_new = [[0 for _ in range(c)]for _ in range(r)] #used when steps need to be printed,matrix dim should match r,c to add rows later

# to get the matrix as rows
for i in range(r):
    row = list(map(Fraction, input(f"Enter row {i+1} (space separated): ").split()))
    if len(row) != c:
        raise ValueError(f"Row {i+1} must have exactly {c} values")
    mat.append(row)

# to get max value in the input matrix
def max1(matrix):
    mx = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] > mx:
                mx = matrix[i][j]
    return mx
m = max1(mat)

#pos,val is used when rows of input matrix is arranged such that row with highest pivot value comes at top
#pos,val gives rows with all zero max value so that zero rows come at bottom when rows are arranged
def pos(lst):
    for i in range(len(lst)):
        if lst[i] != 0:
            return i
    return c      #as the all zero should have max value so that when arranging by comparison it always comes last
def val(lst):
    for i in range(len(lst)):
        if lst[i] != 0:
            return lst[i]
    return m+1

#Row class
class Row:
    def __init__(self,row):
        self.row = row
        self.pivot_val = 0
        self.pivot_pos = 0
    def find_pivot(self):
        i =0
        while i<=len(self.row)-1:
            if self.row[i]==0:
                i +=1
            else:
                self.pivot_val = self.row[i]
                self.pivot_pos = i
                break
    def normalize(self):
        self.find_pivot()
        if self.pivot_val != 0:
             for i in range(len(self.row)):
                 self.row[i] = self.row[i] / self.pivot_val

#Matrix class
class Matrix:
    def __init__(self, matrix,r,c,prnt=0):
        self.matrix = matrix
        self.r = r
        self.c = c
        self.row = []
        self.obj_row = []
        self.prnt = prnt
    #gen_rows() will first arrange the matrix rows and then create separate row objs with the row values in matrix
    def gen_rows(self):
        for i in range(self.r):
            self.row.append(self.matrix[i])
        for i in range(self.r):#arrange the rows initially
            for j in range(i,self.r):
                if pos(self.row[i])>pos(self.row[j]): #pos() gives pivot pos for list pivot_pos() gives pivot for row obj
                    temp = self.row[i]
                    self.row[i] = self.row[j]
                    self.row[j] = temp
                if pos(self.row[i]) == pos(self.row[j]): #if same pivot pos , arrange by pivot val
                    if val(self.row[i]) < val(self.row[j]):
                        temp = self.row[i]
                        self.row[i] = self.row[j]
                        self.row[j] = temp
        for i in range(self.r):#convert to object
            self.obj_row.append(Row(self.row[i]))

    def ref(self):
        self.gen_rows()
        for i in range(self.r):
            self.obj_row[i].find_pivot()
            self.obj_row[i].normalize()
            a = self.obj_row[i].pivot_pos #values below a should be zero for all rows below
            for j in range(i+1,self.r):
                self.obj_row[j].find_pivot()  # as pivot changes
                b = self.obj_row[j].row[a] #gets the values below pivot pos for each row
                if b !=0: # if its already zero , skip that row and move to next j
                     for k in range(len(self.obj_row[j].row)): # to change the entire row by subtracting prev row
                        self.obj_row[j].row[k] = self.obj_row[j].row[k]-(b*(self.obj_row[i].row[k]))
        #saves the values of edited row object to corresponding matrix
        for i in range(self.r):
            mat[i] = self.obj_row[i].row
        print("the REF of the matrix is:")
        #prints the matrix values as strings
        for row in mat:
            print([f"{x.numerator}/{x.denominator}" if x.denominator != 1 else f"{x.numerator}" for x in row])

    def rref(self):
        prnt = self.prnt
        self.gen_rows()
        if prnt != 0:  # to print steps(optional), prints the arranged row
            for y in range(self.r):
                mat_new[y] = self.obj_row[y].row
            print("the initial matrix,arranged wrt to pivot value is:")
            for row in mat_new:
                print([f"{x.numerator}/{x.denominator}" if x.denominator != 1 else f"{x.numerator}" for x in row])
            print("_" * 100)
        for i in range(self.r):
            self.obj_row[i].find_pivot()
            self.obj_row[i].normalize()
            if prnt != 0: #to print steps(optional)
                print(f"R{i} → R{i}/({self.obj_row[i].pivot_val})")
                for y in range(self.r):
                    mat_new[y] = self.obj_row[y].row
                for row in mat_new:
                    print([f"{x.numerator}/{x.denominator}" if x.denominator != 1 else f"{x.numerator}" for x in row])
                print("_" * 100)
            a = self.obj_row[i].pivot_pos  # values below a should be zero for all rows below
            for j in range(self.r):
                if j == i:
                    continue
                else:
                    self.obj_row[j].find_pivot()  # as pivot changes
                    b = self.obj_row[j].row[a]  # gets the values below pivot pos for each row
                    if b != 0:  # if its already zero , skip that row and move to next j
                        for k in range(len(self.obj_row[j].row)):  # to change the entire row by subtracting prev row
                            self.obj_row[j].row[k] = self.obj_row[j].row[k] - (b * (self.obj_row[i].row[k]))
                        if prnt != 0:  # to print steps(optional)
                            print(f"R{j} → R{j}-({b})*R{i}")
                            for y in range(self.r):
                                mat_new[y] = self.obj_row[y].row
                            for row in mat_new:
                                print(
                                    [f"{x.numerator}/{x.denominator}" if x.denominator != 1 else f"{x.numerator}" for x
                                     in row])
                            print("_"*100)
        for i in range(self.r):
            mat[i] = self.obj_row[i].row
        print("the RREF of the matrix is:")
        for row in mat:
            print([f"{x.numerator}/{x.denominator}" if x.denominator != 1 else f"{x.numerator}" for x in row])


n = int(input("choose the option:\n1.Find REF\n2.Find RREF\n "))
if n == 1:
    x = Matrix(mat,r,c)
    x.ref()
if n == 2:
    x = Matrix(mat,r,c)
    n = int(input("choose the option:\n1.Print steps\n2.Dont print steps\n"))
    if n == 1:
        x = Matrix(mat,r,c,1)
        x.rref()
    else:
        x = Matrix(mat,r,c)
        x.rref()





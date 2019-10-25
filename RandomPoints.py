from random import uniform
file_name = input("The name of the file is: ")
file = open(file_name+".txt","w")
n_lines = int(input("Type the number of lines: "))
file.write(str(n_lines) + "\n")
for i in range(n_lines):
    n = int(input("How many random numbers do you want? "))
    file.write(str(n) + "\n")
    a, b = map(float, input("Type the desired interval of x here: ").split())
    c, d = map(float, input("Type the desired interval of y here: ").split())
    for i in range(n):
        file.write(str(uniform(a,b)) + " " + str(uniform(c,d)) + "\n")
file.close()

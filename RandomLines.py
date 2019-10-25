from random import uniform
file_name = input("The name of the file is: ")
file = open(file_name+".txt","w")
n_lines = int(input("Type the number of lines: "))
file.write(str(n_lines) + "\n")
for i in range(n_lines):
    n_points = int(input("How many random numbers do you want? "))
    file.write(str(n_points) + "\n")
    a, b = map(float, input("Type the desired interval (a,b) here: ").split())
    m, n = map(float, input("Type here m and n (y = mx + n): ").split())
    eps = float(input("Choose your epsilon: "))
    for i in range(n_points):
        x = uniform(a,b)
        file.write(str(x) + " " + str(m*x + n + uniform(-1,1)*eps) + "\n")
file.close()

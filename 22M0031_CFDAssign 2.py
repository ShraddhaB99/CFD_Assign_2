import numpy as np
import matplotlib.pyplot as plt
#initialization
Length_x=3
Length_y=4
delta_x=0.1
delta_y=0.1
N_x=31 #(Length_x/delta_x) + 1
N_y=41 #(Length_y/delta_y) + 1

initial_xi=input("Enter initial guess!!!")#100
xi=np.zeros((N_x,N_y))

#Boundary Condition
for j in range(N_y):
    temp_y=j*delta_y
    for i in range(N_x):
        temp_x=i*delta_x
        if temp_x<=1.0 and j==0:
            xi[i][j]=100
        elif temp_x > 1.0 and j == 0:
            xi[i][j]=200
        elif temp_y <=1.9 and i==N_x-1:
            xi[i][j]=200
        elif temp_y > 1.9 and i==N_x-1:
            xi[i][j]=100
        elif i==0:
            xi[i][j]=100
        elif j==N_y-1:
            xi[i][j]=100
        else:
            xi[i][j]=initial_xi

print(xi)

beta=1 # beta= delta_x**2 / delta_y**2
c=0


#Point Jacobi iterative method
while(True):
    cont=1/(2 * (1 + beta**2))
    error_num=0
    error_detn=0
    error=0

    xi_n = xi 
    for i in range(1, N_x-1):
        for j in range(1, N_y-1):
            xi_old= xi[i][j]
            xi_n[i][j] = cont *(xi[i+1][j]+xi[i-1][j]+(beta**2)*(xi[i][j+1] + xi[i][j-1]))
            error_num = error_num +(xi_old - xi[i][j])** 2
            error_detn = error_detn + (xi[i][j]**2)
    error = np.sqrt(error_num) / np.sqrt(error_detn)
    xi[:] = xi_n
    if error<1e-4:
        break
    c=c+1
np.savetxt("200.csv", xi_n, delimiter=",")
plt.contourf(xi.T)
plt.colorbar()
plt.show()


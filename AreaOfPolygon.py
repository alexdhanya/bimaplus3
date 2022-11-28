import math
import numpy as np
from tabulate import tabulate

print("\n");


while True:
    try:
        n = int(input("Number of vertices of the polygon = "));
        if(n>2):
         break;
        else:
            print("Error: Number of vertices should be atleast 3")
            print("\n");
    except:
        continue


print("\n")

print("Caution: Ensure that the coordinates are entered in anti-clockwise direction");


print("\n");

def X_coordinates():       
    x = float(input("X" + str(i+1) + "= "))
    return x


def Y_coordinates():
    y = float(input("Y" + str(i+1) + "= "))
    return y

X_values = [];
y_values = [];
points = [];

for i in range(n):
    X_values.append(X_coordinates());
    y_values.append(Y_coordinates());
    points.append(i+1);


print("\n")

print("Points as defined by user")

# printing Aligned Header
print(f"{'Point' : <10}{'X' : ^10}{'Y' : >5}")

# printing values of variables in Aligned manner
for j in range(n):
    print(f"{points[j] : <10}{X_values[j] : ^10}{y_values[j] : ^10}")


print("\n")

A = 0
Sx = 0
Sy = 0
Ix = 0
Iy = 0
Ixy = 0
X_values.append(X_values[0]);
y_values.append(y_values[0]);

for i in range (len(X_values)-1):
    xi = X_values[i] + X_values[i+1];
    yi = y_values[i+1] - y_values[i];
    A += xi * yi

    xi_x = X_values[i+1] - X_values[i]
    yi_x = (y_values[i+1] **2) + (y_values[i] * y_values[i+1]) + (y_values[i] **2)
    xi_y = y_values[i+1] - y_values[i]
    yi_y = (X_values[i+1] **2) + (X_values[i] * X_values[i+1]) + (X_values[i] **2)
    Sx += xi_x * yi_x
    Sy += yi_y * xi_y

    y_x = (y_values[i+1] **3) + (y_values[i] * y_values[i+1] **2) + (y_values[i] **2 * y_values[i+1])+ (y_values[i] **3)
    y_y = (X_values[i+1] **3) + (X_values[i] **2 * X_values[i+1]) + (X_values[i] * X_values[i+1] **2) + (X_values[i] **3)
    x_xy = (y_values[i+1] * (3*X_values[i+1] **2 + (2 * X_values[i+1] * X_values[i]) + X_values[i] **2 )) + (y_values[i] * (3*X_values[i] **2 + (2 * X_values[i+1] * X_values[i]) + X_values[i+1] **2))
    Ix += xi_x * y_x
    Iy += y_y * xi_y
    Ixy += x_xy * xi_y

Ax = (0.5)*A

Sx = -(Sx/6)
Sy = Sy/6

Ix = -(Ix/12)
Iy = Iy/12
Ixy = -(Ixy/24)

Xt = Sy/Ax
Yt = Sx/Ax

Ixt = Ix - Yt**2 * Ax
Iyt = Iy - Xt **2 * Ax
Ixyt = Ixy + Xt * Yt * Ax

print("\n")
print("Geometric Characteristics")
print(f"Ax: {Ax:>9.2f}")
print(f"Sx: {Sx:>9.2f}")
print(f"Sy: {Sy:>9.2f}")
print(f"Ix: {Ix:>9.2f}")
print(f"Ix: {Iy:>9.2f}")
print(f"Ixy: {Ixy:>8.2f}")
print(f"Xt: {Xt:>9.2f}")
print(f"Yt: {Yt:>9.2f}")
print(f"Ixt: {Ixt:>8.2f}")
print(f"Iyt: {Iyt:>8.2f}")
print(f"Ixyt: {Ixyt:>7.2f}")

# print(tabulate([['Ax', {Ax: .2f}], ['Bob', 19]], headers=['Name', 'Age']))




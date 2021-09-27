# Basics of collatz Conjecture:
#     * If odd:
#         3x + 1
#     * if even:
#         x/2
from typing import List
import matplotlib.pyplot as plt

bullet = int(input("Enter the bullet number: "))
y_axis: List[int] = []
x_axis = []
steps = []
# print(x_axis)
while True:
    if bullet % 2 == 0:
        print("Even\n{}".format(bullet))
        bullet: int = int(bullet / 2)
        steps.append(bullet)
        y_axis.append(bullet)
        if bullet == 1:
            print("Beginning of Conjecture")
            print(steps)
            break
    if bullet % 2 != 0:
        print("Odd\n{}".format(bullet))
        bullet: int = int((3 * bullet) + 1)
        steps.append(bullet)
        y_axis.append(bullet)
        if bullet == 1:
            print("Beginning of Conjecture")
            print(steps)
            break

for i in range(0, len(y_axis)):
    x_axis.append(i)
    print(x_axis)
number_of_steps: int = len(steps)
print("number of steps: ", number_of_steps)
plt.plot(x_axis, y_axis, color='red', marker='o')
plt.title('Collatz Conjecture')
plt.xlabel('number', fontsize=14)
plt.ylabel('Ground', fontsize=14)
plt.show()
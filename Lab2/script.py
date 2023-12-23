import module

A = float(input("Enter A: "))
B = float(input("Enter B: "))
C = float(input("Enter C: "))

module.task_1(A, B, C)
import module

# Assume points is a list of (x, y) coordinates
points = [(0.2, 0.3), (0.8, 0.9), ...]  # Add your points

module.task_2(points)
import module

module.task_3()
import module

while True:
    print("1. Task 1")
    print("2. Task 2")
    print("3. Task 3")
    print("0. Exit")

    choice = int(input("Choose a task (0-3): "))

    if choice == 0:
        break
    elif choice == 1:
        A = float(input("Enter A: "))
        B = float(input("Enter B: "))
        C = float(input("Enter C: "))
        module.task_1(A, B, C)
    elif choice == 2:
        # Assume points is a list of (x, y) coordinates
        points = [(0.2, 0.3), (0.8, 0.9), ...]  # Add your points
        module.task_2(points)
    elif choice == 3:
        module.task_3()
    else:
        print("Invalid choice. Please choose again.")
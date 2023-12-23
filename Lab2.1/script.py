import module

#Створення циклу для визову меню після кожного таску
while True:
    print("1. Task 1")
    print("2. Task 2")
    print("3. Task 3")
    print("0. Exit")

    choice = int(input("Виберіть завдання (0-3): "))

    if choice == 0: # Умова виходу з циклу
        break
    elif choice == 1:
        A = float(input("Введіть сторону A: "))
        B = float(input("Введіть сторону B: "))
        C = float(input("Введіть сторону C: "))
        module.task_1(A, B, C)
    elif choice == 2:
        module.task_2()
    elif choice == 3:
        module.task_3()
    else:
        print("Непрвильний вибір. Спробуйте ще раз.")
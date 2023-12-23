#TASK1
def task_1(A, B, C):
    """
    Якщо значення сторін в порядку зростання, вони подвояться; В іншому випадку вони стануть протилежними.
    Виведіть нові значення A, B, C.
    """

    try:
        if A < B < C:
            A *= 2
            B *= 2
            C *= 2
        else:
            A = -A
            B = -B
            C = -C
        print(f"Нові значення: A={A}, B={B}, C={C}")
    except Exception as e:
        print(f"Помилка: {e}")

#TASK2

def task_2():
    try:
        file_path = input("Введіть шлях до файлу з матрицею: ")
        counts = count_matrix_elements(file_path)
        print(f"Кількість точок '0', які не потрапляють на жодну фігуру, або область: {counts['0']}")
        print(f"Кількість точок '1', що потрапляють на геометричну фігуру: {counts['1']}")
        print(f"Кількість точок '#', що потрапляють в зону болотяного кольору 10-го варіанту: {counts['#']}")
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте правильність шляху до файлу.")
#TASK3

def task_3():
    """
    
      Дослідіть ряд на збіжність.
    """
    try:
        n = 1
        s = u = 2.0
        e = 1e-20  # Мале значення для переривання циклу при збіжності 
        g = 1e5   # Велике значення для переривання циклу при розходженні 

        while abs(u) > e and abs(u) < g:
            n += 1
            if ((n/2)**n) == 0:
                break

            # Обчислення знаменника ряду
            denominator = 1
            for i in range(1, n + 1):
                denominator *= (2 * i - 1)

            u = ((-1)**n * factorial(n)) / (denominator * 5**n)
            s += u
            # Обробка виняткових випадків
        print(f"Ряд сходиться до: {s}")
    except ZeroDivisionError:
        print("Ділення на нуль!")
    except Exception as e:
        print(f"Помилка: {e}")

# Додаткова функція для обчислення факторіала
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

    #Функція для підрахунку точок які потрапляють в зону на системі координат
def count_matrix_elements(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(line.strip()) for line in file]

    counts = {'0': 0, '1': 0, '#': 0}
    for row in matrix:
        for char in row:
            if char in counts:
                counts[char] += 1

    return counts
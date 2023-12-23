def task_1(A, B, C):
    """
    If the values are in ascending order, double them; otherwise, make each value opposite.
    Output the new values of A, B, C.
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
        print(f"New values: A={A}, B={B}, C={C}")
    except Exception as e:
        print(f"Error: {e}")
def task_2(points):
    """
    Count the number of points inside the specified geometric region.
    """
    try:
        count = 0
        for x, y in points:
            # Implement the condition for the specified geometric region
            if 0 <= x <= 1 and 0 <= y <= 1:
                count += 1
        print(f"Number of points inside the region: {count}")
    except Exception as e:
        print(f"Error: {e}")
def task_3():
    """
    Investigate the series for convergence.
    """
    try:
        n = 1
        s = u = 2.0
        e = 1e-10

        while abs(u) > e:
            n += 1
            if ((n/2)**n) == 0:
                break
            u = (n*(n**0.5)) / ((n/2)**n)
            s += u

        print(f"Series converge to: {s}")
    except ZeroDivisionError:
        print("Division by zero!")
    except Exception as e:
        print(f"Error: {e}")

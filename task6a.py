def hollow_hourglass(n):
    for i in range(n):
        for j in range(2 * n - 1):
            if j < i or j >= 2 * n - 1 - i:
                print(" ", end=" ")
            else:
                if i == 0 or j == i or j == 2 * n - 2 - i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()
    for i in range(n - 2, -1, -1):
        for j in range(2 * n - 1):
            if j < i or j >= 2 * n - 1 - i:
                print(" ", end=" ")
            else:
                if i == 0 or j == i or j == 2 * n - 2 - i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()

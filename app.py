def print_multiplication_table(n):
    print("   ", end="")
    for col in range(1, n + 1):
        print(f"{col:3}", end=" ")
    print()
    for row in range(1, n + 1):
        print(f"{row:2}", end=" ")
        for col in range(1, n + 1):
            multi = row * col
            print(f"{multi:3}", end=" ")
        print()


def print_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def main():
    while True:
        num = int(input("Please enter a number: "))
        if num == -1:
            print("Bye!")
            break
        string = input("Please enter a command (triangle/mp): ")
        if string == "triangle":
            print_triangle(num)
        elif string == "mp":
            print_multiplication_table(num)


if __name__ == "__main__":
    main()

def main():
    n = int(input("Enter number of terms: "))

    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

if __name__ == "__main__":
    main()
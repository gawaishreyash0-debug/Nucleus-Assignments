def main():
    # Take multiple numbers as input, separated by spaces
    numbers = input("Enter numbers separated by spaces: ").split()
    
    for num_str in numbers:
        num = int(num_str)
        if num % 2 == 0:
            print(f"{num} is an even number")
        else:
            print(f"{num} is an odd number")

if __name__ == "__main__":
    main()
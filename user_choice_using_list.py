def main():
    while True:
        print("\nChoose an operation:")
        print("1. Square numbers")
        print("2. Filter even numbers")
        print("3. Convert strings to uppercase")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            numbers = input("Enter numbers separated by spaces: ")
            num_list = [int(num) for num in numbers.split()]
            squared = [num ** 2 for num in num_list]
            print("Squared numbers:", squared)
            
        elif choice == '2':
            numbers = input("Enter numbers separated by spaces: ")
            num_list = [int(num) for num in numbers.split()]
            evens = [num for num in num_list if num % 2 == 0]
            print("Even numbers:", evens)
            
        elif choice == '3':
            strings = input("Enter strings separated by spaces: ")
            str_list = strings.split()
            uppercased = [s.upper() for s in str_list]
            print("Uppercase strings:", uppercased)
            
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

        # Ask if the user wants to continue
        continue_choice = input("Do you want to perform another operation? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()

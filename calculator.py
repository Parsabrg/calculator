def get_number_input(line):
    while True:
        try:
            return float(input(line))
        except ValueError:
            print("Invalid input. Please enter a number.")

def perform_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return None
    else:
        print("Invalid operation.")
        return None

def main():
    print("Welcome to the Simple Calculator!")
    while True:
      num1 = get_number_input("Enter the first number: ")
      num2 = get_number_input("Enter the second number: ")
    
      operation = input("Enter the operation (+, -, *, /): ")
      result = perform_operation(num1, num2, operation)
    
      if result is not None:
          print(f"The result of {num1} {operation} {num2} is: {result}")

      again = input ("do you want to perform another calculation? (yes/no): ").strip().lower()
      if again != 'yes':
          print("Goodbye")
          break



main()

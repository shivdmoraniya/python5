try:
    # This block attempts an operation that might cause an error
    num1 = 10
    num2 = 0
    result = num1 / num2
    print(f"Result of division: {result}")
except ZeroDivisionError:
    # This block executes if a ZeroDivisionError occurs
    print("Error: Cannot divide by zero!")
except ValueError:
    # This block would execute if a ValueError occurs (e.g., int("abc"))
    print("Error: Invalid input value!")
except Exception as e:
    # This is a general exception handler for any other unexpected errors
    print(f"An unexpected error occurred: {e}")
else:
    # This block executes only if the try block completes without any exceptions
    print("No exceptions occurred.")
finally:
    # This block always executes, regardless of whether an exception occurred or not
    print("Exception handling complete.")

print("Program continues after exception handling demonstration.")
try:
    # Replace 'your_file.txt' with the actual path to your file
    with open("your_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'your_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
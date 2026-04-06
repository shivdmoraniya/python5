class InvalidInputError(Exception):
    """Custom exception for invalid input."""
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)

def process_data(value):
    if not isinstance(value, (int, float)) or value < 0:
        raise InvalidInputError("Input must be a non-negative number.")
    return value * 2

if __name__ == "__main__":
    try:
        result = process_data(-5)
        print(f"Processed result: {result}")
    except InvalidInputError as e:
        print(f"Error: {e}")

    try:
        result = process_data("text")
        print(f"Processed result: {result}")
    except InvalidInputError as e:
        print(f"Error: {e}")

    try:
        result = process_data(10)
        print(f"Processed result: {result}")
    except InvalidInputError as e:
        print(f"Error: {e}")
def get_day_type(day_number):
    match day_number:
        case 1 | 7:
            return "Weekend"
        case 2 | 3 | 4 | 5 | 6:
            return "Weekday"
        case _:
            return "Invalid day number"

if __name__ == "__main__":
    print(f"Day 3 is a: {get_day_type(3)}")
    print(f"Day 1 is a: {get_day_type(1)}")
    print(f"Day 8 is a: {get_day_type(8)}")
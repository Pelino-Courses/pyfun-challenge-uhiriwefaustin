import datetime

def difference(date1_str, date2_str):
    """
    Calculate the number of days between two dates.
    
    Acceptable formats:
    - 'YYYY-MM-DD' (e.g., '2025-10-28')
    - 'DD/MM/YYYY' (e.g., '10/11/2025')

    Args:
        date1_str (str): First date as a string.
        date2_str (str): Second date as a string.
    
    Returns:
        int: Number of days between the two dates.

    Examples:
        >>> difference('2025-10-28', '2025-11-10')
        13
        >>> difference('28/10/2025', '10/11/2025')
        13
    """
    try:
        # work on  first format: 'YYYY-MM-DD'
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
    except ValueError:
        try:
            # Work on second format: 'DD/MM/YYYY'
            date1 = datetime.datetime.strptime(date1_str, "%d/%m/%Y").date()
        except ValueError:
            print("Error: Please use 'YYYY-MM-DD' or 'MM/DD/YYYY' format for the first date.")
            return None

    try:
        # Here we Try on first format for second date
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
    except ValueError:
        try:
            # Then Try second format
            date2 = datetime.datetime.strptime(date2_str, "%d/%m/%Y").date()
        except ValueError:
            print("Error: Please use 'YYYY-MM-DD' or 'MM/DD/YYYY' format for the second date OR 'enter valid dates'")
            return None

    # Calculate difference
    solution = (date2 - date1).days
    return solution

# Asking for user input
if __name__ == "__main__":
    me=input("enter first_date:")
    you=input("enter second_date:")
    days = difference(me, you)
    if days is not None:
        print(f"Days difference: {days}")

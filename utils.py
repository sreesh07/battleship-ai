def validate_coordinates(x, y, size):
    """
    Ensure that the coordinates are within the board limits.
    Converts 1-based input to 0-based index.
    """
    return 1 <= x <= size and 1 <= y <= size

def print_separator():
    """
    Print a consistent horizontal line for clarity in the console.
    """
    print("-" * 40)

def format_board_row(row):
    """
    Format a single row for display.
    """
    return " ".join(row)

def get_ship_names():
    """
    Returns typical ship names for future expansions.
    """
    return ["Destroyer", "Cruiser", "Submarine"]

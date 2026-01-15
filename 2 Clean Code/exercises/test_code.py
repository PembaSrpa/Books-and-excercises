# This creates a physical file named test_code.py in your folder

# where the value to a parameter named location is being passed (with a space)
current_location = "New York"
next_location = "San Francisco"

def move_to(location):
    print(f"Moving to {location}")

# where this varaible is assigned this value (no space)
move_to(location=current_location)

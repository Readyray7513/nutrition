def main():
    # Prompt user for input, strip whitespace, and convert to lowercase
    user_input = input('What are you thinkin of?:').strip().lower()
    
    # Define a dictionary with items and their corresponding values
    items = {
        'apple': 130,
        'avocado': 50,
        'sweet cherries': 100,
        'kiwifruit': 90,
        'pear': 100,

    }
    




    # Check if the user input matches any of the dictionary keys
    if user_input in items:
        print(f"The value of {user_input} is {items[user_input]}")
    else:
        print("")
        return 1

# Run the main function
main()

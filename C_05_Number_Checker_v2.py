# Functions go here
def num_check(question, low, high):
    """Checks users enter an integer / float that is more than zero (or the optimal exit code)"""

    error = f"Oops! - please enter an integer between {low} and {high}."

    while True:

        try:
            # Changes response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine goes here

# Loop for testing purposes:
while True:
    print()

    # Ask user for an integer
    my_num = num_check("Choose a number: ", 1, 10)
    print(f"You chose {my_num}")
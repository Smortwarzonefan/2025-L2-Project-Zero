# Functions Go Here
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "Ok, sending 1,000,000 robux to your account"

        if response == "no" or response == "n":
            return "Ok, sending 1x nuke to your location"

        print("Please enter either yes or no.\n")

#Main Routine
print("Hello! Would you like free robux?")
yes_or_no = yes_no("Please enter either yes or no: ")
print(yes_or_no)
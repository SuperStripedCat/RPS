def string_checker(question, valid_ans=("yes", "no")):

    """check that user enter a valid word / first
    letter of the word based on a list of options.  Default to yes / no."""

    error = f"please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for var_item in valid_ans:
            # check if the user response is a word in the list
            if var_item == user_response:
                return var_item

            #check if the user response is a word in the list
            # the first letter of an item in the list
            elif user_response == var_item[0]:
                return var_item

        # print error if user does not enter something that is valid
        print(error)
        print()

# Main routine goes here

rps_list = ["rock", "scissors", "xxx"]

want_instructions = string_checker("Do you want to see the instruction? ",)

print("you choose: ", want_instructions)

user_choice = string_checker("choose: ", rps_list)
print("You choose: ", user_choice)
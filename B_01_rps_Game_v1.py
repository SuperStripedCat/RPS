import random

def int_check(question, exit_code=None):
    """ checks for an integer more than 0 (allows <enter>) """

    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)

        # check for infinite mode / exit code
        if response == exit_code:
            return exit_code

        try:
            # tries to make the response into an integers
            response = int(response)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            # if the response is not an integer, displays an error
            print(error)


# option based on a list

def rps_compare(user, comp):
    if user == comp:
        result = "tie"

    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "lose"
    elif user == "rock" and comp == "scissors":
        result = "win"
    elif user ==  "scissors" and comp == "scissors":
        result = "lose"

        # if it;s not a win / tie, then it's a loss
    else:
        result = "lose"

    return result

# Main Routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("💎📰✂️ Rock / Paper / Scissors Game 💎📰✂️")
print()

# Instructions

# Ask user for the number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode:", "" )

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:
    user_choice = input("choose: ")

    # Rounds heading
    if mode == "infinite":
        rounds_heading = f"\n💿💿💿 Round {rounds_played} ( Infinite Mode) 💿💿💿 "

    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played} of {num_rounds} 💿💿💿 "

    print(rounds_heading)
    print()

    user_points = input("choose: ")

    if user_points == "xxx":
        break

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game History / Statistics area ,
import random as r
import pyfiglet


def play(start,end):
    print(pyfiglet.figlet_format("Level 1"))
    num = r.randint(1, 5)
    hint = "its an Even Number" if num % 2 == 0 else "its an Odd Number"
    while 1:
        try:
            print("*" * 40)
            print("Guess A Number Between 1 and 5")
            guess = int(input("🤔 Enter Your Guess: "))
            if guess != num:
                print(f"❌ No {guess} is not the correct Number, Try again\nHint : {hint}")
            else:
                print(f"🎉 YAY! You Guessed it right ! the Correct Number Was {num}")
                if input("Do You Want to Play Again (y/n): ").strip().lower() == "n":
                    break
            num = r.randint(start, end)
        except ValueError:
            print("Enter Correct Values")
        except Exception as e:
            print(f"Error Something Went Wrong {e}")


def main():
    while 1:
        try:
            print(pyfiglet.figlet_format("Number Guessing Game"))
            print("Level 1 (Guess Between 1 and 5)")
            print("Level 2 (Guess Between 1 and 10)")
            print("Level 3 (Guess Between 1 and 20)")
            level = int(input("Enter The Level of Your Choice"))
            if level == 1:
                play(1,5)
                if input("Do You Want to Play another level (y/n): ").strip().lower() == "n":
                    break
            elif level == 2:
                play(1,10)
                if input("Do You Want to Play another level (y/n): ").strip().lower() == "n":
                    break
            elif level == 3:
                play(1,20)
                if input("Do You Want to Play another level (y/n): ").strip().lower() == "n":
                    break
            else:
                print("Wrong Input")
        except ValueError:
            print("Enter Correct Value")


main()

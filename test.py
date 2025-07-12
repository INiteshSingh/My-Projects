import random as r 
import pyfiglet

def play(start,stop):
    print(pyfiglet.figlet_format("Level 1"))
    num = r.randint(start,stop)
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
        except ValueError:
            print("Enter Correct Values")
        except Exception as e:
            print(f"Error Something Went Wrong {e}")

def main():
    while True:
        try:
            print("*"*40)
            print(pyfiglet.figlet_format("Number Guessing Game"))
            print("*"*40)
            print("Level 1 (Guess Between 1 and 5)")
            print("Level 2 (Guess Between 1 and 10)")
            print("Level 3 (Guess Between 1 and 20)")
            level = int(input("Enter Your Level: "))
            if level == 1:
                play(1,5)
                break
            elif level == 2:
                play(1,10)
                break    
            elif level == 3:
                play( 1,20)
                break
            else:
                print("Invalid Level. Please Choose 1, 2, or 3. ")
        except ValueError:
            print("Enter Only Numerical Values")
        except Exception as e:
            print(f"something went wrong !:\n{e}")


main()

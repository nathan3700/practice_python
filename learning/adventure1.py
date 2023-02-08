import random


class Adventure:
    def __init__(self):
        self.all_rooms = ["entry", "lab room", "computer room", "win"]
        self.current_room = "lab"

    def play_game(self):
        print("Welcome to Adventure Game!")
        print("You are a scientist on a mission to save the world from a deadly virus.")
        print("You have entered a lab and need to find the cure before it's too late.")

        self.current_room = self.entry_choices()

        if self.current_room == "lab room":
            self.lab_room_choices()

        if self.current_room == "computer room":
            self.computer_room_choices()

    def entry_choices(self):
        print("You have three choices to make:")
        print("1. Open the left door")
        print("2. Open the right door")
        print("3. Check the cabinets")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            return "lab room"
        elif choice == 2:
            return "computer room"
        else:
            print("You find a first aid kit and some snacks. Not what you were looking for.")
            print("You need to go back and choose another door.")
        return "entry"

    def lab_room_choices(self):
        print("You have entered a room with test tubes and equipment.")
        print("You see a locked box and need to solve a math problem to unlock it.")
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        result = num1 + num2
        answer = int(input(f"What is {num1} + {num2}? "))
        if answer == result:
            print("The box is unlocked and you find a clue.")
            print("You need to go back and choose another door.")
        else:
            print("The answer is incorrect. The box remains locked.")
        return "lab room"

    def computer_room_choices(self):
        print("You have entered a room with a computer and a microscope.")
        print("You find the cure and save the world!")
        return "win"


if __name__ == "__main__":
    adventure = Adventure()
    adventure.play_game()
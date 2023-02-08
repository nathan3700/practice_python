# Remembers a list of hobbies

default_hobbies = ["reading", "swimming", "gaming", "drawing"]


class Hobbies:
    def __init__(self, initial_name="Unknown", initial_hobbies=default_hobbies):
        self.name = initial_name
        self.hobbies = initial_hobbies

    def print_hobbies(self):
        # Use a for loop to print each hobby
        for hobby in self.hobbies:
            print(f"{self.name} enjoys " + hobby)

    def ask_if_my_hobby(self):
        while True:
            ans = input("Tell me a hobby (q to quit): ")
            if ans == "q":
                break
            if ans in self.hobbies:
                print(f"{ans} is one of {self.name}'s hobbies.")
            else:
                print(f"{ans} is not one of {self.name}'s hobbies.")


if __name__ == "__main__":
    hobbies_mike = Hobbies("Mike", ["skiing", "gaming", "drawing", "frisbee golf"])
    hobbies_susan = Hobbies("Susan", ["walking", "riding", "painting", "basketball"])

    hobbies_mike.print_hobbies()
    hobbies_mike.ask_if_my_hobby()

    hobbies_susan.print_hobbies()
    hobbies_susan.ask_if_my_hobby()

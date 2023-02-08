# Define a list of hobbies
hobbies = ["reading", "swimming", "gaming", "drawing"]

# Use a for loop to print each hobby
for hobby in hobbies:
    print("I enjoy " + hobby)

while True:
    ans = input("Tell me a hobby (q to quit): ")
    if ans == "q":
        break
    if ans in hobbies:
        print(f"{ans} is one of my hobbies.")
    else:
        print(f"{ans} is not one of my hobbies.")

# CIS110 - Choose Your Own Adventure
# Title: Bunny Adventure

print("Hello adventurer! Let's hop into a story about a brave little bunny.")
print("Before we begin, I need to ask you a few questions to help shape our story!")
print("Please type your answer and press Enter each time.")
input("Press Enter to begin...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":

    # Ask the user for 5 custom details about the story
    bunnyName = input("\nWhat is the bunny's name? ")
    while len(bunnyName.strip()) == 0:
        bunnyName = input("Please enter a bunny name: ")

    bunnyColor = input("What color is the bunny's fur? ")
    while len(bunnyColor.strip()) == 0:
        bunnyColor = input("Please enter a fur color: ")

    forestName = input("What is the name of the enchanted forest? ")
    while len(forestName.strip()) == 0:
        forestName = input("Please enter the forest name: ")

    foodType = input("What is the bunny's favorite food? ")
    while len(foodType.strip()) == 0:
        foodType = input("Please enter a food type: ")

    burrowName = input("Enter a cute burrow name ideal for a bunny: ")
    while len(burrowName.strip()) == 0:
        burrowName = input("Please enter a burrow name: ")

    # Begin story
    print("\nThe sun is setting over a peaceful meadow...")
    print(f"{bunnyName}, a curious {bunnyColor} bunny, is munching on some {foodType}.")
    print(f"As the sky turns orange, a glowing path appears, leading into the mysterious {forestName}...")

    # First decision
    decision1 = input(f"\nShould {bunnyName} hop into the enchanted forest and follow the glowing path? (yes or no): ")
    while decision1.lower() not in ["yes", "no"]:
        decision1 = input("Please type yes or no: ")

    if decision1.lower() == "yes":
        print(f"\n{bunnyName} hops along the glowing path into {forestName}.")
        print("The path flickers and a loud hum echoes through the trees. It's scary, but thrilling!")

        # Second decision (only asked if Decision 1 is yes)
        decision2 = input(f"\n{bunnyName} reaches a shimmering stream with glowing stones. "
                          f"Should {bunnyName} cross to reach the carrot patch? (yes or no): ")
        while decision2.lower() not in ["yes", "no"]:
            decision2 = input("Please type yes or no: ")

        if decision2.lower() == "yes":
            print(f"\nCarefully, {bunnyName} hops from stone to stone and reaches the juiciest carrot patch ever!")
            print("Overjoyed, she munches away with delight!")
        else:
            print(f"\n{bunnyName} hesitates and decides not to cross.")
            print(f"Instead, a cozy burrow appears nearby. She hops in and decides to name it {burrowName}.")
    else:
        print(f"\n{bunnyName} stays in the meadow, peacefully nibbling on {foodType}, "
              f"never knowing what adventure awaited.")
        decision2 = "no"  # force a value for ending logic

    # Alternate endings
    if decision1.lower() == "yes" and decision2.lower() == "yes":
        print(f"\nWith her belly full of magical carrots, {bunnyName} returns home to share her treasure.")
        print(f"She becomes a hero among the bunnies of {forestName}!")
    elif decision1.lower() == "no" and decision2.lower() == "no":
        print(f"\n{bunnyName} spends her days happily in the meadow, but always wonders what lay beyond the glowing path...")
    else:
        print(f"\n{bunnyName} discovers shiny gems inside {burrowName}. She naps peacefully, dreaming of what could have been.")

    print("\nThe End.\n")

    # Ask if user wants to play again
    keepPlaying = input("Would you like to play again? (yes or no): ")
    while keepPlaying.lower() not in ["yes", "no"]:
        keepPlaying = input("Please type yes or no: ")

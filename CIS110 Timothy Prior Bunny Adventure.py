# CIS110 - Choose Your Own Adventure
# Title: Clover the Bunny
# Author: Timothy Prior (with assistance)
# Description: A simple console-based choose-your-own-adventure using only Python fundamentals
# Tools used: print, input, while loops for validation, if/elif/else, and a replay loop

print("Hello adventurer! 🐰 Let's hop into an exciting story about a brave little bunny named Clover.")
print("Before we begin, I need to ask you a few questions to help shape the story.")
print("Please type your answer and press Enter each time.\n")
input("Press Enter to begin...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":

    # Ask user for details (5 variables) with validation
    bunnyName = input("\nWhat is the bunny's name? ")
    while len(bunnyName.strip()) == 0:
        bunnyName = input("Please enter a bunny name: ")

    bunnyColor = input("What color is the bunny's fur? ")
    while len(bunnyColor.strip()) == 0:
        bunnyColor = input("Please enter a fur color: ")

    forestName = input("What is the name of the enchanted forest? ")
    while len(forestName.strip()) == 0:
        forestName = input("Please enter the forest name: ")

    foodType = input("What is the bunny’s favorite food? ")
    while len(foodType.strip()) == 0:
        foodType = input("Please enter a food type: ")

    burrowName = input("What should Clover name the burrow she found? ")
    while len(burrowName.strip()) == 0:
        burrowName = input("Please enter a burrow name: ")

    # Story Intro
    print("\n🌅 The sun is setting over a peaceful meadow...")
    print(f"{bunnyName}, a curious {bunnyColor} bunny, is munching on some {foodType}.")
    print(f"As the sky turns orange, a glowing path appears, leading into the mysterious {forestName}...")

    # Decision 1
    decision1 = input(f"\nShould {bunnyName} hop into the enchanted forest and follow the glowing path? (yes or no): ")
    while decision1.lower() not in ["yes", "no"]:
        decision1 = input("Please type yes or no: ")

    if decision1.lower() == "yes":
        print(f"\n{bunnyName} hops along the glowing path into {forestName}.")
        print("The path flickers and a loud hum echoes through the trees. It's scary, but thrilling!")
    else:
        print(f"\n{bunnyName} stays behind in the meadow, peacefully nibbling on {foodType}, never knowing what adventure awaited.")

    # Decision 2
    decision2 = input(f"\n{bunnyName} stumbles upon a shimmering stream with glowing stones. Should {bunnyName} cross to reach the carrot patch? (yes or no): ")
    while decision2.lower() not in ["yes", "no"]:
        decision2 = input("Please type yes or no: ")

    if decision2.lower() == "yes":
        print(f"\nCarefully, {bunnyName} hops from stone to stone and reaches the juiciest carrot patch ever!")
        print("Overjoyed, she munches away with delight!")
    else:
        print(f"\n{bunnyName} hesitates and decides not to cross.")
        print(f"Instead, a cozy burrow appears nearby. She hops in and decides to name it {burrowName}.")

    # Alternate Endings
    if decision1.lower() == "yes" and decision2.lower() == "yes":
        print(f"\n🌟 With her belly full of magical carrots, {bunnyName} returns home to share her treasure.")
        print(f"She becomes a hero among the bunnies of {forestName}!")
    elif decision1.lower() == "no" and decision2.lower() == "no":
        print(f"\n🌼 {bunnyName} spends her days happily in the meadow, but always wonders what lay beyond the glowing path...")
    else:
        print(f"\n🌀 {bunnyName} discovers shiny gems inside {burrowName}. She naps peacefully, dreaming of what could have been.")

    print("\n🐾 The End.\n")

    # Play again?
    keepPlaying = input("Would you like to play again? (yes or no): ")
    while keepPlaying.lower() not in ["yes", "no"]:
        keepPlaying = input("Please type yes or no: ")

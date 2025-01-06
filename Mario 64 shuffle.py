import keyboard
import time
import random

# List of save slots
randomSaves = ["1", "2", "3"]
previous_save = None  # To keep track of the last used save slot

def simulate_startup_sequence():
    """Simulates pressing F5 followed by each number key from 1 to 0."""
    print("Simulating startup sequence...")
    for key in randomSaves:
        print(f"Saving with key {key}...")
        keyboard.press_and_release('f5')  # Save
        time.sleep(1)
        keyboard.press_and_release(key)  # Slot

def random_countdown():
    while True:
        # Generate a random time between 1 and 4 seconds
        countdown_time = random.randint(1, 2)
        print(f"Countdown starting for {countdown_time} seconds... (Press 'q' to quit)")

        while countdown_time > 0:
            # Check if the 'q' key is pressed to quit the program
            if keyboard.is_pressed('q'):
                print("\nQuitting the program...")
                return  # Exit the loop and stop further execution

            mins, secs = divmod(countdown_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(timer, end="\r")  # Print on the same line
            time.sleep(1)
            countdown_time -= 1
    
        picksave()

def picksave():
    global previous_save  # Access the global variable to track the last used save

    # Select a random save, ensuring it's different from the previous one
    available_saves = [save for save in randomSaves if save != previous_save]
    randomSave = random.choice(available_saves)

    print(f"Saving to slot {randomSave}...")
    keyboard.press_and_release('f5')  # Save
    time.sleep(.1)  # Delay for realism
    keyboard.press_and_release(randomSave)  # Slot
    time.sleep(.1)  # Delay for realism
    keyboard.press_and_release('f7')  # Load the save slot

    # Update the previous_save to the current one
    previous_save = randomSave

    # Call the countdown again
    random_countdown()

def saveAndLoad():
    keyboard.press_and_release('f5')  # Save

def startup():
    """Handles startup and initializes the sequence."""
    print("Press Enter to start...")
    keyboard.wait('enter')  # Wait for the Enter key
    print("\nStarting program...")

    simulate_startup_sequence()  # Simulate pressing F5 and numbers
    random_countdown()

startup()

# Let the program run indefinitely to listen for key events
print("Press 'Esc' to stop the program manually.")
keyboard.wait('esc')  # Press 'Esc' to stop the program manually

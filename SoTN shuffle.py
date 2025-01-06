import keyboard
import time
import random

# List of save slots
save_slots = ["f1", "f2", "f3"]
current_slot_index = 0  # To track the current slot for saving

def simulate_startup_sequence():
    """Simulates pressing F5 followed by each number key from 1 to the length of save_slots."""
    print("Simulating startup sequence...")
    # Only simulate saving once initially
    for key in save_slots:
        print(f"Saving with key {key}...")
        keyboard.press('shift')  # Hold Shift
        keyboard.press_and_release(key)  # Press the corresponding key
        keyboard.release('shift')  # Release Shift
        time.sleep(0.2)

def random_countdown():
    """Handles the countdown and slot management."""
    while True:
        # Generate a random time between 1 and 20 seconds
        countdown_time = random.randint(1, 20)
        print(f"Countdown starting for {countdown_time} seconds... (Press 'q' to quit)")

        while countdown_time > 0:
            # Check if the 'q' key is pressed to quit the program
            if keyboard.is_pressed('q'):
                print("\nQuitting the program...")
                return  # Exit the loop and stop further execution

            # Check if the spacebar is pressed to mark the current save slot as finished
            if keyboard.is_pressed('space'):
                mark_slot_as_finished()
                return  # Restart after marking slot

            mins, secs = divmod(countdown_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(timer, end="\r")  # Print on the same line
            time.sleep(1)  # Sleep for 1 second to slow down the countdown
            countdown_time -= 1
        
        # Once countdown finishes, pick a save
        picksave()

def picksave():
    """Handles saving to the current slot and loading from a random slot."""
    global current_slot_index

    if len(save_slots) == 0:
        print("No save slots available. Exiting.")
        return  # Exit if there are no save slots available

    # Get the current save slot (in sequence)
    current_save = save_slots[current_slot_index]
    print(f"Current save slot is {current_save} (index {current_slot_index})")

    # Simulate saving to the current slot (Shift + F1-F8)
    print(f"Saving to slot {current_save}...")
    keyboard.press('shift')  # Hold Shift
    keyboard.press_and_release(current_save)  # Press the corresponding key
    keyboard.release('shift')  # Release Shift

    # Simulate load from a random slot, making sure it's not the same as the current slot
    available_slots = [slot for slot in save_slots if slot != current_save]
    random_load = random.choice(available_slots)  # Pick a random slot from the remaining ones
    time.sleep(0.05)  # Short delay
    print(f"Loading from slot {random_load}...")
    keyboard.press_and_release(random_load)  # Load the randomly selected save slot

    # Move to the next slot in the list (wrap around if at the end)
    current_slot_index = (current_slot_index + 1) % len(save_slots)
    print(f"Next active slot is {save_slots[current_slot_index]}")

def mark_slot_as_finished():
    """Marks the current slot as finished and removes it from the available slots."""
    global current_slot_index

    if len(save_slots) == 0:
        print("No slots available to finish.")
        return  # No slots left to finish
    
    current_save = save_slots[current_slot_index]
    print(f"Marking {current_save} as finished and removing it from available slots.")
    
    # Remove the current save slot from the list
    save_slots.remove(current_save)

    # If no slots are left, stop the program
    if len(save_slots) == 0:
        print("No more slots to save or load. Exiting.")
        keyboard.wait('esc')  # Wait for the user to quit manually
        return

    # Adjust the current_slot_index after removal
    if current_slot_index >= len(save_slots):
        current_slot_index = len(save_slots) - 1  # Make sure we stay within bounds after removal

    print(f"Next active slot is {save_slots[current_slot_index]}.")

def startup():
    """Handles startup and initializes the sequence."""
    print("Press Enter to start...")
    keyboard.wait('enter')  # Wait for the Enter key
    print("\nStarting program...")

    simulate_startup_sequence()  # Simulate pressing F5 and numbers
    random_countdown()

# Main program execution
startup()

# Let the program run indefinitely to listen for key events
print("Press 'Esc' to stop the program manually.")
keyboard.wait('esc')  # Press 'Esc' to stop the program manually

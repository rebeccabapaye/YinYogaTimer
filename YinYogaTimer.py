import time 
import chime

# Chime function
def bell(num_of_chimes):
    i = 0
    while i < num_of_chimes - 1:
        chime.success()
        time.sleep(1)
        i += 1
    chime.success()

# Start with a welcome message
print("Welcome to Yin Yoga Timer!")
print("Please enter pose times separated by a comma and a space (e.g. 1, 2, 3 not 1,2,3).\n")

# Input and list generation
raw_sequence_data = input("Pose times in minutes: ")
sequence_list = raw_sequence_data.split(", ")
sequence = []
i = 0
while i < len(sequence_list):
    try:
        duration = float(sequence_list[i])
        sequence.append(duration)
        i += 1
    except:
        print("'", sequence_list[i], "' is invalid input for pose", i + 1)
        fixed_input = input("Please enter a number for pose time in minutes: ")
        sequence_list[i] = fixed_input

# List of times complete
print("Generating sequence ...")
print("Your sequence times are:", sequence)

# Remove last item from list and assign to final posture, which is a constant
shavasana = sequence.pop(-1)

# Pause for input before starting sequence
input("Ready to begin? Press enter. ")

# Three chimes for beginning of practice
bell(3)
time.sleep(5)

# Sequence loop
for duration in sequence:
    bell(1)
    time.sleep(duration * 60)
    bell(2)
    time.sleep(30)

# Final timing for shavasana
bell(1)
time.sleep(shavasana * 60)

# Three chimes for end of practice
bell(3)
print("Finished!")
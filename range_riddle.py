'''Task 1 Write a program that prints off different 
 moods for each day of the week.
 '''
 # Create a list of moods ssuch as "Happy", "Sad", "Energetic", and "Calm".
 # Using the range() function, loop through every day of the week 
 # And for each day, randomly select a mood from the list and print it.  
 
 # Import random
import random 
 
days = ["Sunday", "Monday", "Tuesday", "Wednesyday", "Thursday", "Friday", "Saturday"]
moods = ["Happy", "Sad", "Energetic", "Calm"]

# Loop through each day of the week
for day in days:
    # randomly select a mood
    mood = random.choice(moods)
    # Print the day and random mood to the console
    print(f"On {day}, You were feeling {mood}.")
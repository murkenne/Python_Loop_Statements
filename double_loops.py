# Task 1 Mood Tracker: Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening)
# For each day of the week. Use nested loops to implement this.
# The outer loop should itereate over the days and the inner loop should iterate over the times of day
# For each time, randomly select a mood from a predefined list and print it.  
# Use the random module again to randomly select the mood.  
import random

days = ["Sunday", "Monday", "Tuesday", "Wednesyday", "Thursday", "Friday", "Saturday"]
times = ["morining", "afternoon", "evening"]
moods = ["Happy", "Sad", "Energetic", "Calm"]

for day in days:
    for time in times:
        mood = random.choice(moods)
        print(f"On {day}, in the {time}, you were feeling {mood}.")


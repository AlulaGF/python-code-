# File: hour_distribution.py

# Open the file
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except FileNotFoundError:
    print(f"File '{fname}' not found in the current directory.")
    exit()

# Dictionary to store hour counts
hour_counts = {}

# Process each line
for line in fhand:
    # Look for lines that start with "From "
    if line.startswith("From "):
        # Split the line into words
        words = line.split()
        # The time is the 6th word (index 5)
        time_str = words[5]
        # Split the time by colon to get hour, minute, second
        hour = time_str.split(':')[0]
        # Increment the count for this hour
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

fhand.close()

# Sort the dictionary by hour (keys) and print
for hour in sorted(hour_counts):
    print(hour, hour_counts[hour])

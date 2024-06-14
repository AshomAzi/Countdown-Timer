import time

# Collect input from user
time_limit = int(input('Enter time in Seconds: '))

"""loop though users given time in seconds from 0 to time given
We can do this backward by using the step technique
Amd we increment backwards"""

for i in range(time_limit, 0, -1):

    # Calculating for seconds, we use modulus 60 to give us the remainder
    seconds = i % 60

    """calculating for minutes, we use division operator to give us the division value
    cause we have 60 secnode in a minute"""

    minutes = int(i / 60) % 60

    """Calculating for hours, we have 3600 seconds in 1 hour"""
    hours = int(i / 3600)

    # printing the time to display with 0 padding using a format specifier(seconds:02)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    # timer sleep for 1 second
    time.sleep(1)

print('Time over')

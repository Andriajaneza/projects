import time

def clock():
    hours = 0
    minutes = 0
    seconds = 0

    while True:
        print (str(hours) + ":" + str(minutes) + ":" + str(seconds))
        time.sleep(1)
        seconds += 1

        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        if hours == 24:
            time.sleep(2.5)
            hours = 0
            minutes = 0
            seconds = 0
    
clock()
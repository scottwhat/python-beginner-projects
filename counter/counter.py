import time

#enter a time, and countdown

inputTime = int((input("How many seconds to countDown foryour prize?")))

for x in range(inputTime, 0, -1):

    seconds = x % 60
    mins = int(x / 60 ) % 60
    hours = int(x / 3600) % 24

    print(f"{hours:02}:{mins:02}:{seconds:02}")
    time.sleep(1)

print("Congrats! ( . Y . )")
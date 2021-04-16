Drivers_speed = int(input("Enter your speed: "))
Speed_limit = int(input("Enter the speed limit: "))

if Drivers_speed <= Speed_limit:
    print("OK")
elif Drivers_speed == Speed_limit + 5:
    print(" Point: 1 ")
elif Drivers_speed == Speed_limit + 10:
    print(" Point: 2 ")
elif Drivers_speed == Speed_limit + 15:
    print(" Point: 3 ")
elif Drivers_speed == Speed_limit + 20:
    print(" Point: 4")
elif Drivers_speed == Speed_limit + 25:
    print(" Point: 5 ")
elif Drivers_speed == Speed_limit + 30:
    print(" Point: 6")
elif Drivers_speed == Speed_limit + 35:
    print(" Point: 7 ")
elif Drivers_speed == Speed_limit + 40:
    print(" Point: 8")
elif Drivers_speed == Speed_limit + 45:
    print(" Point: 9 ")
elif Drivers_speed == Speed_limit + 50:
    print(" Point: 10 ")
elif Drivers_speed == Speed_limit + 55:
    print(" Point: 11 ")
elif Drivers_speed == Speed_limit + 60:
    print(" Point: 12 ")
elif Drivers_speed >= Speed_limit + 60:
    print("Time to go to jail")

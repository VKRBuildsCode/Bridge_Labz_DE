


def wind_chill(t,v):
    wc = 35.74 + (0.6215 * t) - 35.75*(v ** 0.16) + 0.4275 * t * (v ** 0.16)
    return  wc
while True:
    temperature = float(input("Enter the temperature : "))
    wind_speed = float(input("Enter the speed : "))
    if temperature > 50 or wind_speed > 120 or wind_speed < 3:
        print("Enter valid temperature[<50] and wind speed[3< and <120")
    else:
        print(f"Wind chill is :{wind_chill(temperature,wind_speed)}")
        break
def speak(sound: str, repeat: int) -> None:
    print(sound * repeat)


print(speak(sound="woof", repeat=3))
speak(sound="meow", repeat=2)


def get_weather_report() -> str:
    weather = input("What is the weather?")
    if weather = "rainy" or "cold":
        print("Bring a jacket!")
    elif weather = "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather

get_weather_report()

print("Welcome to the BandName Generator Program!")

user_city = input("What city were you born? ")
pet_name = input("What's your childhood pet's name? ")

band_name = user_city.capitalize() + pet_name.capitalize()

print(f"Your new band name is {band_name}")

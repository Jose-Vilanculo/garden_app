# User input values for the season and plant type
season = input('''Select a season by typing out the name:
# Summer
# Winter
: ''').lower()

plant_type = input('''Select a season by typing out the name:
# Flower
# Vegetable
: ''').lower()


# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertilizer to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

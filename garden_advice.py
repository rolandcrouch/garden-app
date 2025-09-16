def get_user_input():
    """
    Get season and plant type input from user.
    """
    print("Available seasons: summer, winter")
    season = input("Enter the season: ").lower()
    
    print("Available plant types: flower, vegetable")
    plant_type = input("Enter the plant type: ").lower()
    
    return season, plant_type

def get_season_advice(season):
    """
    Get gardening advice based on the season.
    """
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"

def get_plant_type_advice(plant_type):
    """
    Get gardening advice based on the plant type.
    """
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."

def generate_advice(season, plant_type):
    """
    Generate complete gardening advice based on season and plant type.
    """
    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_type_advice(plant_type)
    return advice

def main():
    """
    Main function to run the gardening advice program.
    """
    season, plant_type = get_user_input()
    advice = generate_advice(season, plant_type)
    print(advice)

if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.

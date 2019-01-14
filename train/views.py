from django.shortcuts import render

# Create your views here.
runner_catergory = "Low-Key Competitive"
race_distance = "5k"

def decide_weekly_running_volume(runner_catergory, race_distance):
    """
    Function that takes customer's choosen experience level and returns a running volume
    """ 
    if runner_catergory == "low-key competitive":
        volume = 35
    else:
        volume = 30
    return volume
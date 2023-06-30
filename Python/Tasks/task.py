import requests
from datetime import datetime

# https://api.nasa.gov/
# TASK 1
def get_nasa_fact(date):
    '''
    :param date: date (YYYY-MM-DD)
    :return: dictionary
    '''

    api_key = None  # Generate your own API key
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    response = requests.get(url)
    '''
    Generate your api key in https://api.nasa.gov/
    create a function that receive date (YYYY-MM-DD) and send request to NASA with your personal API key
    If response status code is 200, function will return dict with keys:
    'date'
    'explanation'
     'title'
     'url'
     EXAMPLE:
     {
     'date': '2023-02-19', 
     'explanation': "Is this really the famous Pleiades star cluster? Known for its iconic blue stars, the Pleiades is 
     shown here in infrared light where the surrounding dust outshines the stars. Here three infrared colors have been 
     mapped into visual colors (R=24, G=12, B=4.6 microns). The base images were taken by NASA's orbiting Wide Field 
     Infrared Survey Explorer (WISE) spacecraft. Cataloged as M45 and nicknamed the Seven Sisters, the Pleiades star 
     cluster is by chance situated in a passing dust cloud. The light and winds from the massive Pleiades stars 
     preferentially repel smaller dust particles, causing the dust to become stratified into filaments, as seen. The 
     featured image spans about 20 light years at the distance of the Pleiades, which lies about 450 light years 
     distant toward the constellation of the Bull (Taurus).", 
     'title': 'Seven Dusty Sisters in Infrared', 
     'url': 'https://apod.nasa.gov/apod/image/2302/Pleiades_WiseAntonucci_960.jpg'
     }
    Check what will happened if you will send request with date before Jun 16, 1995 or after today date.
    In this case return dictionary with next keys:
    'code'
    'msg'
    EXAMPLE:
    {
    'code': 400, 
    'msg': 'Date must be between Jun 16, 1995 and Mar 19, 2023.'
    }
    else return dictionary with next keys:
    'code'
    'msg'
    EXAMPLE:
    {
    'code': 500, 
    'msg': 'Server is not available please try later'
    }
    Create tests for this function using Mock, test 3 cases
    1 - with response status code 200
    2 - with response status code 400  
    3 - with response status code 500
    '''
    pass


# Task 2
def generate_date():
    '''
    Create function what will generate today date and call get_nasa_fact function with current date.
    return will be dictionary what generate get_nasa_fact function
    Create 3 tests with freezegun:
    1 - date before Jun 16, 1995 (get_nasa_fact request Should return code 400)
    2 - date from future (get_nasa_fact request Should return code 400)
    3 - date 19.02.2023 (get_nasa_fact request should return code 200)
    :return: dictionary
    '''
    pass


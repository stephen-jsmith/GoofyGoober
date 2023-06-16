# Import Statements
from requests import get

# Define where the data is going to come from
base_url = 'https://wttr.in/'

def getData(city:str) -> str:
    ''' This function pings a weather api for the forecast of a given city
    
    # Arguments #
    :arg city: The location that we want the data from
    :type city: str

    # Returns #
    :ret out: The forecast for the given city
    :type out: str
    '''

    # Define the url for our chosen city
    url = base_url + city
    print(url)
    try:
        data = get(url)
        print(type(data))
        out = data.text
    except:
        out = 'Error occurred'
    
    return out

print((getData("Austin")))
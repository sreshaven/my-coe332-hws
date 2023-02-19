import xmltodict
import requests
import math
from flask import Flask

app = Flask(__name__)

def get_data() -> dict:
    """
    Processes the ISS data from XML into a dictionary and returns the state vectors data
    
    Args:
        no arguments
    
    Returns:
        iss_data (dict): the ISS data set as a dictionary
    """
    response = requests.get(url='https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    iss_data = xmltodict.parse(response.text)
    # get the state vectors data 
    iss_data = iss_data['ndm']['oem']['body']['segment']['data']['stateVector']
    return iss_data

@app.route('/', methods=['GET'])
def index() -> dict:
    """
    Returns the ISS dataset (epoch, position, and velocity at each point) for the '/' route
    
    Args:
        no arguments
    
    Returns:
        iss_data (dict): the ISS data set as a dictionary
    """
    iss_data = get_data()
    return iss_data

@app.route('/epochs', methods=['GET'])
def get_epochs() -> list:
    """
    Creates and returns a list of the epochs in the ISS dataset for the '/epochs' route

    Args:
        no arguments

    Returns:
        epochs_list (list): list of strings of the time stamps, or the epochs
    """
    iss_data = get_data()
    epochs_list = []
    for state_vec in iss_data:
        epochs_list.append(state_vec['EPOCH'])
    return epochs_list

@app.route('/epochs/<epoch>', methods=['GET'])
def get_state_vectors(epoch: str) -> dict:
    """
    Finds and returns the state vectors for the specified epoch in the url for the '/epochs/<epoch>' route

    Args:
        epoch (str): the time stamp for a data point

    Returns:
        epoch_output (dict): the state vectors from the specified epoch, if epoch not found, will return empty dictionary, position {X, Y, Z} has units of km and the velocity vector coordinates {X_DOT, Y_DOT, Z_DOT} has units of km/s
    """
    iss_data = get_data()
    epoch_output = {}
    for state_vec in iss_data:
        if state_vec['EPOCH'] == epoch:
            epoch_output = state_vec
            for key in epoch_output:
                if key != 'EPOCH':
                    epoch_output[key] = float(epoch_output[key]['#text'])
    return epoch_output

@app.route('/epochs/<epoch>/speed', methods=['GET'])
def get_speed(epoch: str) -> str:
    """
    Uses the get_state_vectors function to find the state vectors and calculate the instantaneous speed at that time stamp

    Args:
        epoch (str): the time stamp for a data point

    Returns:
        speed (str): the instantaneous speed at the time stamp, if epoch was not found in the dataset, will return message
    """
    epoch_dat = get_state_vectors(epoch)
    if len(epoch_dat) != 0:
        speed = math.sqrt(epoch_dat['X_DOT']**2 + epoch_dat['Y_DOT']**2 + epoch_dat['Z_DOT']**2)
        return str(speed) + ' km/s\n'
    else:
        return "The specified epoch was not found\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

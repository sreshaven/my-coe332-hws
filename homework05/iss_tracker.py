import xmltodict
import requests
import math
import json
from flask import Flask, request

app = Flask(__name__)

response = requests.get(url='https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
iss_data = xmltodict.parse(response.text)
# get the state vectors data 
iss_data = iss_data['ndm']['oem']['body']['segment']['data']['stateVector']
with open('iss_data.json', 'w') as out:
    json.dump(iss_data, out, indent = 2)

def get_data() -> list:
    """
    Processes the ISS data from json into a list of dictionaries and returns the state vectors data
    
    Args:
        no arguments
    
    Returns:
        iss_data (list): the ISS data set as a list
    """
    iss_data = []
    with open('iss_data.json', 'r') as f:
        iss_data = json.load(f)
    return iss_data

@app.route('/', methods=['GET'])
def index() -> list:
    """
    Returns the ISS dataset (epoch, position, and velocity at each point) for the '/' route
    
    Args:
        no arguments
    
    Returns:
        iss_dat (list): the ISS data set as a list
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
    offset = request.args.get('offset', str(0))
    limit = request.args.get('limit', str(len(iss_data)))
    if offset:
        try:
            offset = int(offset)
        except ValueError:
            return "Bad input: please specify a positive integer for offset\n"
    if limit:
        try:
            limit = int(limit)
        except ValueError:
             return "Bad input: please specify a positive integer for limit\n"
    epochs_list = []
    count = 0
    index = 0
    for state_vec in iss_data:
        if (count == limit):
            break
        if index >= offset:
            epochs_list.append(state_vec['EPOCH'])
            count += 1
        index += 1
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

@app.route('/help', methods=['GET'])
def help() -> str:
    """
    Returns string with help info about routes and methods for each route

    Args:
        no arguments

    Returns:
        help_str (str):
    """
    help_str = ""
    return help_str

@app.route('/delete-data', methods=['DELETE'])
def delete_data() -> str:
    """
    Deletes the ISS data from the json file that is being used

    Args:
        no arguments

    Returns:
        output (str): indicates that the data was deleted from the file
    """
    iss_data = []
    with open('iss_data.json', 'w') as out:
        json.dump(iss_data, out, indent = 2)
        return 'ISS Data has been deleted\n'

@app.route('/post-data', methods=['POST'])
def post_data() -> str:
    """
    Reloads the ISS data and adds to the json file again

    Args:
        no arguments

    Returns:
        output (str): message that indicates that the ISS data was reloaded
    """
    response = requests.get(url='https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    iss_data = xmltodict.parse(response.text)
    # get the state vectors data
    iss_data = iss_data['ndm']['oem']['body']['segment']['data']['stateVector']
    with open('iss_data.json', 'w') as out:
        json.dump(iss_data, out, indent = 2)
        return 'ISS Data has been reloaded\n'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

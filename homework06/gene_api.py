from flask import Flask, request
import requests
import redis
import csv

app = Flask(__name__)

def get_redis_client():
    return redis.Redis(host = 'redis-db', port = 6379, db = 0, decode_responses = True)

rd = get_redis_client()

@app.route('/data', methods=['POST','GET','DELETE'])
def handle_data() -> list:
    """
    If methods is POST, loads the auto trends data set into redis and returns message
    If method is GET, returns data from redis
    If method is DELETE, clears the data in redis and returns message

    Args:
        no arguments

    Returns:
        auto_data (list): (if method is GET) list of dictionaries of the cars data in redis
    """
    if request.method == 'POST':
        with open('auto_trends_data.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                item = dict(row)
                key = item['Manufacturer'] + '-' + item['Model Year'] + '-' + item['Vehicle Type']
                rd.hset(key, mapping = item)
        return 'Auto Trends data is loaded into Redis\n'
    elif request.method == 'GET':
        auto_data = []
        for key in rd.keys():
            auto_data.append(rd.hgetall(key))
        return auto_data
    elif request.method == 'DELETE':
        rd.flushdb()
        return 'Auto Trends data has been deleted from Redis\n'
    else:
        return 'The method you tried does not work\n'

@app.route('/years', methods=['GET'])
def get_years() -> list:
    """
    Returns a list of the years currently in redis for the Auto Trends database for the '/years' route
    
    Args:
        no arguments
    
    Returns:
        years_list (list): list of strings of the Model Year
    """
    years_list = []
    for key in rd.keys():
        car_dict = rd.hgetall(key)
        if car_dict['Model Year'] not in years_list:
            years_list.append(car_dict['Model Year'])
    return years_list

@app.route('/years/<year>', methods=['GET'])
def get_year_info(year: str) -> list:
    """
    Returns a list with all cars from that year if found in the Auto Trends database for the '/years/<year>' route

    Args:
        year (str): the string of a Model Year

    Returns:
        year_cars (list): list with cars from the specified year, if year not found, will be empty list
    """
    year_cars = []
    if year in get_years():
        for key in rd.keys():
            car_dict = rd.hgetall(key)
            if car_dict['Model Year'] == year:
                year_cars.append(car_dict)
    return year_cars

@app.route('/manufacturers', methods=['GET'])
def get_manufacturers() -> list:
    """
    Returns a list of the manufacturers currently in redis for the Auto Trends database for the '/manufacturers' route

    Args:
        no arguments

    Returns:
        manufacturers_list (list): list of strings of the Manufacturer
    """
    manufacturers_list = []
    for key in rd.keys():
        car_dict = rd.hgetall(key)
        if car_dict['Manufacturer'] not in manufacturers_list:
            manufacturers_list.append(car_dict['Manufacturer'])
    return manufacturers_list

@app.route('/manufacturers/<manufacturer>', methods=['GET'])
def get_manufacturer_info(manufacturer: str) -> list:
    """
    Returns a list with all cars from that manufacturer if found in the Auto Trends database for the '/manufacturers/<manufacturer>' route

    Args:
        manufacturer (str): the string of a Manufacturer

    Returns:
        manufacturer_cars (list): list with cars from the specified manufacturer, if manufacturer not found, will be empty list
    """
    manufacturer_cars = []
    if manufacturer in get_manufacturers():
        for key in rd.keys():
            car_dict = rd.hgetall(key)
            if car_dict['Manufacturer'] == manufacturer:
                manufacturer_cars.append(car_dict)
    return manufacturer_cars

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

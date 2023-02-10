import requests
TURBIDITY_THRESHOLD = 1.0
DECAY_FACTOR = 0.02

def calc_turbidity(a0: float, I90: float) -> float:
    """
    Calculates the turbidity with reading data

    Args:
        a0 (float): the calibration constant
        I90 (float): ninety degree detector current

    Returns:
        turbidity (float): turbidity value in NTU units (between 0 - 40)
    """

def calc_min_time(T0: float) -> float:
    """
    Calculates the minimum amount of time to return to below a safe turbidity threshold

    Args:
        T0 (float): the current turbidity value
    
    Returns:
        b (float): the minimum amount of time in hours
    """

def main():
    response = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
    turb_data = response.json()
    
if __name__ == '__main__':
    main()

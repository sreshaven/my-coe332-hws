import requests
import math
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
    turbidity = a0 * I90
    return turbidity

def calc_min_time(T0: float) -> float:
    """
    Calculates the minimum amount of time to return to below a safe turbidity threshold

    Args:
        T0 (float): the current turbidity value
    
    Returns:
        min_time (float): the minimum amount of time in hours
    """
    if (T0 <= TURBIDITY_THRESHOLD):
        return 0
    else:
        min_time = math.log(TURBIDITY_THRESHOLD/T0, 1 - DECAY_FACTOR)
        return round(min_time, 2)


def main():
    response = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
    turb_data = response.json()
    
    # calculate average turbidity
    recent_data = turb_data['turbidity_data'][-5:]
    avg_turb = 0.0
    for turb_dict in recent_data:
        cur_a0 = turb_dict['calibration_constant']
        cur_I90 = turb_dict['detector_current']
        avg_turb += calc_turbidity(cur_a0, cur_I90)
    avg_turb /= 5

    # print info about recent turbidity
    print('Average turbidity based on most recent five measurements = {:.4f} NTU'.format(avg_turb))
    if (avg_turb > TURBIDITY_THRESHOLD):
        print('Warning: Turbidity is above threshold for safe use')
        print('Minimum time required to return below a safe threshold = {:.2f} hours'.format(calc_min_time(avg_turb)))
    else:
        print('Info: Turbidity is below threshold for safe use')
        print('Minimum time required to return below a safe threshold = 0 hours')

if __name__ == '__main__':
    main()

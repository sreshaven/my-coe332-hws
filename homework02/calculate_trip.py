import json

def main():
    with open('landing_sites.json', 'r') as f:
        sites_data = json.load(f)

    cur_lat = 16.0
    cur_long = 82.0
    elapsed_time = 0.0
    site_count = 0

    for site in sites_data['sites']:
        site_count += 1

        # calculate distance and travel time
        travel_dist = # function call for distance here
        cur_lat = site['latitude']
        cur_long = site['longitude']
        travel_time = travel_dist / 10
        elapsed_time += travel_time

        # add time based on composition
        sample_time = 0
        if site['composition'] == 'stony':
            elapsed_time += 1
            sample_time = 1
        elif site['composition'] == 'iron':
            elapsed_time += 2
            sample_time = 2
        else:
            elapsed_time += 3
            sample_time = 3

        leg_str = "leg = {}, time to travel = {:.2f} hr, time to sample = {} hr".format(site['site_id'], travel_time, sample_time)
        print(leg_str)
    
    print('=' * 30)
    summary_str = "number of legs = {}, total time elapsed = {:.2f} hr".format(site_count, elapsed_time)
    print(summary_str)

if __name__ == '__main__':
    main()

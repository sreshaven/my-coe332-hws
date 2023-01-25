import json
import random

def main():
    sites_data = { 'sites': [] }
    
    compositions = ["stony", "iron", "stony-iron"]
    
    for i in range(5):
        data = {}
        data['site_id'] = i + 1
        data['latitude'] = (random.random() * 2) + 16
        data['longitude'] = (random.random() * 2) + 82
        data['composition'] = compositions[random.randint(0, 2)]
        sites_data['sites'].append(data)

    with open('landing_sites.json', 'w') as out:
        json.dump(sites_data, out, indent = 2)

if __name__ == '__main__':
    main()


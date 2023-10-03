import sys
import csv
import logging
import requests

def csv_to_json(csv_file_path):
    data = []
    try:
        with open(csv_file_path, 'r') as csvf:
            csv_reader = csv.DictReader(csvf)
            
            for row in csv_reader:
                data.append(row)
    except Exception as e:
        logging.error('Failed to process data', exc_info=e)
        exit(1)
    return data

def send(url, json_data):
    try:
        r = requests.post(url=url, json=json_data)
        print(f'Status code: {r.status_code}')
    except Exception as e:
        logging.error(f'Failder to send data to {url}', exc_info=e)
        exit(1)

if __name__ == '__main__':
    json_data = csv_to_json(sys.argv[1])
    send(sys.argv[2], json_data)
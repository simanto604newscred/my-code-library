__author__ = 'MAK'
import json
import requests
import csv
from datetime import datetime, timedelta, date
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

INPUT_FILEPATH = dir_path + '/example.json'
# OUTPUT_FILEPATH = './json_to_csv/'

DATE_FORMAT = '%d-%m-%Y'


with open(dir_path + '/config.json') as conf_file:
    CONFIG = json.load(conf_file)
    print("config loading successful")

URL = CONFIG['URL']


class JsonGetter:
    def __init__(self):
        self.json = None

    def get_post_request_params(self):
        params = {
                 "from": from_date.strftime(DATE_FORMAT),
                 "to": to_date.strftime(DATE_FORMAT),
                 }
        params.update(CONFIG['PROD'])

        return params

    def get_json(self):
        return self.make_post_request()

    def get_json_from_file(self, file=INPUT_FILEPATH):
        with open(file) as data_file:
            data = json.load(data_file)
        return data

    def make_post_request(self):
        data = {
            "data": json.dumps(self.get_post_request_params())
        }

        print("making post request at {}".format(datetime.now()))
        try:
            req = requests.post(URL, params=data)

        except requests.exceptions.RequestException as e:
            raise e

        print("post request completed at {}".format(datetime.now()))
        print(req)

        return req.json()


class JsonToCSV:

    def __init__(self, a_json, OUTPUT_FILEPATH):
        self.data = a_json if a_json else None
        self.OUTPUT_FILEPATH = OUTPUT_FILEPATH


    def convert(self):
        print("csv creation started at {}".format(datetime.now()))
        with open(self.OUTPUT_FILEPATH, 'w') as csvfile:
            fieldnames = [ 'id', 'phone_number', 'errors','status', 'datetime', 'total_parts', 'sms_content',
                           'department_id', 'template_id',
                           'custom_contents_01','custom_contents_02', 'custom_contents_03','custom_contents_04',
                           'custom_contents_05']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            if 'message' in self.data.keys():
                print("found items")
                for item in self.data['message']:
                    item = self.flatten(item)
                    writer.writerow(item)
        print("csv creation completed at {}".format(datetime.now()))

    def flatten(self, item):
        # import ipdb;ipdb.set_trace()
        item.update(item['numbers'][0])
        for i in range(1,6):
            key = '0{}'.format(i)
            item['custom_contents_{}'.format(key)] = item['custom_contents'][key]
        del item['numbers']
        del item['custom_contents']
        return item


if __name__ == '__main__':
    from_date = date(2018,5,1)
    while from_date < date(2018,11,1):
        to_date = from_date + timedelta(days=7)

        OUTPUT_FILEPATH = ''.join(['./json_to_csv/', from_date.strftime(DATE_FORMAT), '_to_',
                                   to_date.strftime(DATE_FORMAT), '.csv'])

        print(OUTPUT_FILEPATH)
        reporting_json = JsonGetter().get_json()

        JsonToCSV(reporting_json, OUTPUT_FILEPATH).convert()
        from_date = to_date




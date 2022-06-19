
import requests
from pprint import pprint
from datetime import datetime

class stack_over_flow:

    host = 'https://api.stackexchange.com'

    def __init__(self, site: str):
        self.site = site

    def fromdate(self):

        dt = datetime.now()

        # getting the timestamp
        ts = int(datetime.timestamp(dt))
        from_ts = ts - 172800
        return from_ts

    def stack(self):
        url = f'{self.host}/2.3/questions'
        # headers = self.get_headers()
        fromdate = self.fromdate()
        site = self.site
        params = {'fromdate': fromdate,
                  'order': 'desc',
                  'sort': 'activity',
                  'tagged': 'python',
                  'site': site}

        response = requests.get(url=url, params=params)
        # resp_status = response.json().get('href')
        resp_status = response.json().get('items')
        # pprint(resp_status)
        list_questions = []
        for link in resp_status:
            title_dict = link.get('title')
            link_dict = link.get('link')
            list_questions.append({'title': title_dict, 'link': link_dict})
        return list_questions


if __name__ == '__main__':
    stackover = stack_over_flow('stackoverflow')
    result = stackover.stack()
    pprint(result)



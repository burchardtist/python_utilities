# pip install requests

import requests
from lxml import html
from pprint import pprint

URL = 'https://www.fakeaddressgenerator.com/World_Address/get_us_address/state/CA'


def get_xpath_value():
    selector = '//div[div/span[contains(text(), \'{name}\')]]{tag}'
    input_ = '//input/@value'
    strong = '//strong/text()'

    response = requests.get(URL)
    root = html.fromstring(response.content)

    input_names = [
        'Full Name', 'Gender', 'Birthday', 'Driver License',
        'Social Security Number', 'Street', 'City', 'State',
        'Zip Code', 'Phone Number'
    ]

    result = dict()
    for name in input_names:
        for tag in [input_, strong]:
            value = root.xpath(selector.format(name=name, tag=tag))
            if value:
                result[name] = value.pop().replace('\xa0', ' ')
                break
            result[name] = 'error'
    pprint(result)


if __name__ == '__main__':
    get_xpath_value()

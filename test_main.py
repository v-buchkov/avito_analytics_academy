"""
Buchkov Viacheslav, DS Track, Python - HW2
"""

# Import function for testing
from main import Advert
import json


# Class for testing
class OutputTest:
    # Initialize with input (corpus) and expected outputs
    def __init__(self, advert_json: str, exp_output: list):
        self.advert_json = advert_json
        self.exp_output = exp_output

    def test(self):
        json_out = json.loads(self.advert_json)
        advert = Advert(json_dict=json_out)
        output = [advert.title, advert.price, advert.class_, advert.location.address, advert]
        # If both outputs equal to expected outputs => test is passed
        if [str(item) for item in output] == [str(item) for item in self.exp_output]:
            return True
        else:
            return False


if __name__ == '__main__':
    # Initialize test from HW example
    test1 = OutputTest(advert_json="""{
    "title": "python", "price": 0,
     "class": "snakes",
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
}""", exp_output=['python', 0, 'snakes', 'город Москва, Лесная, 7',  '\x1b[1;33;40m python | 0 RUB'])

    test2 = OutputTest(advert_json="""{
"title": "iPhone X",
"class": "phones",
"price": 100, "location": {
"address": "город Самара, улица Мориса Тореза, 50",
"metro_stations": ["Спортивная", "Гагаринская"] }
}""", exp_output=['iPhone X', 100, 'phones', 'город Самара, улица Мориса Тореза, 50',
                  '\x1b[1;33;40m iPhone X | 100 RUB'])

    test3 = OutputTest(advert_json="""{
"title": "Вельш-корги",
"class": "dogs",
"price": 1000, "location": {
"address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25" }
}""", exp_output=['Вельш-корги', 1000, 'dogs', 'сельское поселение Ельдигинское, поселок санатория Тишково, 25',
                  '\x1b[1;33;40m Вельш-корги | 1000 RUB'])
    # Print the result (True-False)
    print(test1.test(), test2.test(), test3.test())

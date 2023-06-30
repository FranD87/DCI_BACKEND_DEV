
import requests

class Horoscope:
    def __init__(self, sign, day='today'):
        self.sign = sign
        self.day = day

    def fetch(self):
        URL = 'https://aztro.sameerkumar.website/'
        data = requests.post(URL, params=(('sign', self.sign), ('day', self.day))).json()
        return data['description']


if __name__ == '__main__':
    aries = Horoscope('aries')
    libra = Horoscope('gemini')
    print(aries.fetch())
    print()
    print(libra.fetch())
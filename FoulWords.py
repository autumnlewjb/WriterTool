from bs4 import BeautifulSoup as bs
import requests
import re


def record_regex(pattern):
    with open('regex.txt', 'w+') as output_file:
        output_file.write(pattern)


class FoulWords:
    def __init__(self):
        self.url = r'https://en.wiktionary.org/wiki/Category:English_swear_words'
        self.req = requests.get(self.url)
        self.soup = bs(self.req.content, 'lxml')

    def get_element(self):
        narrow_down = self.soup.find('div', class_='mw-content-ltr')
        result = narrow_down.find_all('li')
        return [i.text for i in result]

    def create_regex(self):
        word_list = self.get_element()
        if not word_list:
            return None
        pattern = r''
        pattern += word_list[0]
        for i in range(1, len(word_list)):
            pattern += '|{}'.format(word_list[i])

        record_regex(pattern)

        return re.compile(pattern, re.IGNORECASE)


if __name__ == '__main__':
    fw = FoulWords()
    print(fw.req.status_code)
    for i in fw.get_element():
        print(i)

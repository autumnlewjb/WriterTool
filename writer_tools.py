from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from foul_words import FoulWords
import time


class WriterTools:

    def __init__(self):
        self.browser = None
        self.raw = None

    # get text from user
    def input_text(self):
        print("Enter your text below: ")
        print()
        self.raw = str(input())

    # remove punctuation from the input text
    def process_text(self, text=None) -> str:
        if text is None:
            text = self.raw
        li = list(text)
        i = 0
        final = ""
        while i < len(li):
            if li[i].isalpha():
                final += str(li[i])
            else:
                pass
            i += 1

        return final

    # return word count of a text
    def word_count(self):
        self.input_text()
        words = self.raw.split(" ")
        with_punc_with_space = 0
        no_punc_with_space = 0
        no_punc_no_space = 0

        for char in self.raw:
            with_punc_with_space += 1

            if char.isalpha():
                no_punc_no_space += 1
                no_punc_with_space += 1
            elif char == " ":
                no_punc_with_space += 1
        print("NUMBER OF CHARACTERS")
        print("With PUNCTUATION and SPACE: " + str(with_punc_with_space))
        print("With SPACE without PUNCTUATION: " + str(no_punc_with_space))
        print("ONLY TEXT: " + str(no_punc_no_space))
        print("\nNUMBER OF WORDS (PUNCTUATION EXCLUDED): " + str(len(words)))

    # check the diff between two texts
    def compare_str(self):
        self.input_text()
        compare1 = self.process_text()
        print("Enter the text to compare with your text: ")
        print()
        compare2 = self.process_text(str(input()))
        i = 0
        diff_raw = ""
        diff_compare = ""
        count = 0
        while i < min(len(compare1), len(compare2)):
            if compare1[i] != compare2[i]:
                diff_raw += compare1[i]
                diff_compare += compare2[i]
                count += 1
            else:
                pass
            i += 1

        print("Uncompared Characters: " + str(abs(len(compare1) - len(compare2))))
        print("Total number of different characters: " + str(count) + "/" + str(min(len(compare1), len(compare2))))
        if count > 0:
            print("In Your Text: " + str(diff_raw))
            print("In The Compare Text: " + str(diff_compare))

    # check for plagiarism
    def plagiarism(self):
        print('Your text must contains at least 30 characters!')
        self.input_text()
        if len(self.raw) >= 30:
            self.browser = webdriver.Chrome()
            self.browser.get("http://plagiarisma.net/")
            time.sleep(3)
            text_box = self.browser.find_element_by_name("query")
            text_box.send_keys(self.raw)
            self.browser.find_element_by_xpath("//button[@name='Submit']").click()
            print("This might take a while....")

            wait = WebDriverWait(self.browser, 30)
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))

            results = self.browser.find_elements_by_tag_name("p")
            print("RESULTS: ")
            for result in results:
                print(result.text)
            self.browser.close()
        else:
            print('Your text has less than 30 character. Unable to initiate plagiarism check. ')

    # censoring vulgar words from the text
    def censoring(self):
        self.input_text()
        regex = FoulWords().create_regex()
        
        if not regex:
            with open('regex.txt', 'r') as input_file:
                regex = input_file.read()

        print(regex.sub('#$%#$#$%$#', self.raw))


if __name__ == '__main__':
    print("WRTIER'S TOOL")

    menu = {
        '1': 'WORD COUNT',
        '2': 'TEXT COMPARISON',
        '3': 'PLAGIARISM CHECK',
        '4': 'CENSORING',
    }

    for key in menu:
        print(str(key) + ' ' + str(menu[key]))

    print("\nHello Writer!")
    option = int(input("What would you like to do?"))
    obj = WriterTools()
    if option == 1:
        obj.word_count()
    elif option == 2:
        obj.compare_str()
    elif option == 3:
        obj.plagiarism()
    elif option == 4:
        obj.censoring()

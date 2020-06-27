from FoulWords import FoulWords
from selenium import webdriver
import time


class WriterTools:

    def __init__(self):
        self.browser = None
        self.raw = None

    def input_text(self):
        print("Enter your text below: ")
        print()
        self.raw = str(input())
        # self.raw = "I love, to eat, apples!"

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

    def compare_str(self):
        self.input_text()
        compare1 = self.process_text()
        print("Enter the text to compare with your text: ")
        # compare2 = self.process_text("I love to eat apples")
        compare2 = self.process_text(str(input()))
        i = 0
        diff_raw = None
        diff_compare = None
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
        print("In Your Text: " + str(diff_raw))
        print("In The Compare Text: " + str(diff_compare))

    def plagiarism(self):
        self.input_text()
        self.browser = webdriver.Chrome()
        self.browser.get("http://plagiarisma.net/")
        time.sleep(3)
        text_box = self.browser.find_element_by_name("query")
        text_box.send_keys(self.raw)
        self.browser.find_element_by_xpath("//button[@name='Submit']").click()
        print("This might take a while....")
        time.sleep(15)
        results = self.browser.find_elements_by_tag_name("p")
        print("RESULTS: ")
        for result in results:
            print(result.text)
        self.browser.close()

    def censoring(self):
        self.input_text()
        regex = FoulWords().create_regex()
        print(regex.sub('#$%#$#$%$#', self.raw))


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

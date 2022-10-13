from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

class Cursor():
    def __init__(self) -> None:
        pass
    def fill_out(element_type: str, element_name: str, fill_text: str):
        search_bar = my_driver.find_element(element_type, element_name)
        search_bar.send_keys(fill_text)
    def click_it(element_type: str, element_name: str):
        search_button = my_driver.find_element(element_type, element_name)
        search_button.click()
    def get_results(element_type: str, element_name: str):
        num_of_results = my_driver.find_element(element_type, element_name).text
        num_of_results = num_of_results.split()
        my_num = num_of_results[0]
        if my_num == '4':
            print('Number of jobs confirmed! There are 4 jobs currently listed.')
        else:
            print(f'Number of jobs not confirmed. There are currently not 4, but {my_num} jobs listed.')

'''is it ok to leave the PATH to chromedriver.exe like this? i have considered putting in os module and os.walk() 
 but i thought it would be easier for you to just change the directory PATH according to your chromedriver location'''
s = Service("C:\Program Files (x86)\chromedriver.exe")

my_driver = webdriver.Chrome(service=s)
my_driver.maximize_window()
my_driver.get("https://jobs.eaton.com/jobs")

jobs = Cursor
jobs.fill_out('id','keyword-search','C++')
jobs.fill_out('id','location-search','Prague')
jobs.click_it('id','search-btn')
time.sleep(4)
jobs.get_results('id','search-results-indicator')

my_driver.quit()

if __name__ == "__main__":
    pass
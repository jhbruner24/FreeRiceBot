from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchWindowException

class FreeRiceBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def login(self):
        # username = ""
        # password = "" 
        self.driver.get('https://freerice.com/')

        sleep(1)
        self.driver.find_element_by_class_name('toolbar__user-salut').click()
        
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="login-password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div[2]/div/div/button').click()
        sleep(1)


    def earnRice(self):
        sleep(2)
        self.driver.find_element_by_class_name('toolbar__menu-toggle-icon').click()

        sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="root"]/nav/div/nav/ul/li[2]/a').click()

        sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div[2]/div/div/div[6]/div[1]/div[1]').click()

        while True:
            try:
                sleep(.1)
                equation = self.driver.find_element_by_class_name('card-title').text
                numbers = equation.split(' x ')
                if numbers[0] == '' or numbers[1] == '':
                    print(numbers)
                    print("Invalid argument")
                    continue
                firstInt = int(numbers[0])
                secondInt = int(numbers[1])
                answer = firstInt * secondInt

                answer1 = self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[2]').text
                answer2 = self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[3]').text
                answer3 = self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[4]').text
                answer4 = self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[5]').text

                if answer == '' or answer1 == '' or answer2 == '' or answer3 == '' or answer4 == '':
                    print("Invalid answer")
                    continue
                if answer == int(answer1):
                    self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[2]').click()
                elif answer == int(answer2):
                    self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[3]').click()
                elif answer == int(answer3):
                    self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[4]').click()
                elif answer == int(answer4):
                    self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[5]').click()

            except NoSuchElementException:
                print("No such element exception")
            except StaleElementReferenceException:
                print("Stale element exception")
            except ElementClickInterceptedException:
                print("Click Intercepted Exception")
            except ElementNotInteractableException:
                print("Element Not Interactable Exception")
            # except NoSuchWindowException:
            #     print("No such Window")
                
bot = FreeRiceBot()
#bot.login()
bot.earnRice()
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchWindowException

from time import sleep

class FreeRiceBot():
    def __init__(self):
        #Instantiate the bot
        self.driver = webdriver.Chrome()
        
    def login(self):
        #username = ""
        #password = ""
        self.driver.get('https://freerice.com/')
        
        #Navigate to login screen
        sleep(1)
        self.driver.find_element_by_class_name('toolbar__user-salut').click()
        
        #Input user information supplied in username in password vars
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="login-password"]').send_keys(password)

        #Press login button
        self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div[2]/div/div/button').click()
        sleep(1)


    def earnRice(self):
        #Comment out the following line if you are going to log in
        self.driver.get('https://freerice.com/')

        #Navigates to the 'Multiplication Table' category
        sleep(2)
        self.driver.find_element_by_class_name('toolbar__menu-toggle-icon').click()
        sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="root"]/nav/div/nav/ul/li[2]/a').click()
        sleep(.5)
        self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div[2]/div/div/div[6]/div[1]/div[1]').click()

        #Loops through forever, could modify the function to stop after some value of rice
        while True:
            try:
                #Decrease this sleep value at your own risk, FreeRice.com tends to crash for a couple mins if this is too low
                sleep(1.5)

                #Parsing equation
                equation = self.driver.find_element_by_class_name('card-title').text
                numbers = equation.split(' x ')
                if numbers[0] == '' or numbers[1] == '':
                    print("Invalid argument")
                    continue
                firstInt = int(numbers[0])
                secondInt = int(numbers[1])
                answer = firstInt * secondInt

                #Getting answer choices
                answer1 = self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[2]').text
                answer2 = self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[3]').text
                answer3 = self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[4]').text
                answer4 = self.driver.find_element_by_xpath('//*[@id="root"]/section/div/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div[5]').text

                #Choosing answer
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
            
            #The various excepetions that appeared when testing
            except NoSuchElementException:
                print("No such element exception")
            except StaleElementReferenceException:
                print("Stale element exception")
            except ElementClickInterceptedException:
                print("Click Intercepted Exception")
            except ElementNotInteractableException:
                print("Element Not Interactable Exception")
            #This final exception tended to appear when FreeRice.com crashed and thus wasn't useful for continuing the loop
            # except NoSuchWindowException:
            #     print("No such Window")
                
bot = FreeRiceBot()
#bot.login()
bot.earnRice()

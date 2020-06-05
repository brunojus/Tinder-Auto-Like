from selenium import webdriver
from time import sleep
from secrets import username,password
from selenium.webdriver.common.keys import Keys

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://tinder.com')

        sleep(5)
        self.driver.find_element_by_xpath("//button[@type = 'button' and @aria-label = 'Entrar com Facebook']//span").click()


        # Switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        self.driver.find_element_by_xpath('//*[@id="u_0_0"]').click()


        self.driver.switch_to_window(base_window)
        sleep(5)
        bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()

        sleep(1)

        bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()

       
    def like(self):
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()

    def dislike(self):
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button').click()

    def auto_swipe(self):
        while True:
            sleep(1)
            try:
                print('like')
                self.like()
            except Exception:
                print('popup')
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()
    
    def close_match(self):
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a').click()

bot = TinderBot()
bot.login()
bot.auto_swipe()
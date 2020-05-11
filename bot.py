import os
from time import sleep

from selenium import webdriver

CONFIG_FILE = 'settings.ini'

class MyBot:
    def __init__(self, url, username, password):
        """
        Initializes Bot Instance (May be used in the future)

        Args:
            url:str - The Instagram base url
            username:str - The Instagram username
            password:str - The Instagram password

        Attributes:
            
        """
        self.base_url = url
        self.username = username
        self.password = password

class InstagramBot(MyBot):
    def __init__(self, url, username, password):
        """
        Initializes InstagramBot Instance

        Args:
            url:str - The Instagram base url
            username:str - The Instagram username
            password:str - The Instagram password

        Attributes:
            
        """
        super().__init__(url, username, password)
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.login()

    def login(self):
        """
        Logs in using credentials in class attributes
        """
        self.driver.get(self.base_url)
        sleep(10)
        # finds fields and fills them
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        sleep(10)
        # clicks log in
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
        sleep(10)

    def nav_user(self, user):
        """
        Navigates to given user
        Args:
            user:str - Username we want to navigate to
        """
        self.driver.get('{}{}'.format(self.base_url, user))
        sleep(10)

    def follow_user(self, user):
        """
        Follows given user

        Args:
            user:str - Username we want to start following
        """
        self.nav_user(user)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Seguir')]").click()
        sleep(10)


if __name__ == '__main__':
    import configparser

    # Just in case, it creates a default file
    if not os.path.exists(CONFIG_FILE):
        conf = configparser.ConfigParser()
        conf['INSTAGRAM'] = {
            'url'       : 'https://www.instagram.com/',
            'username'  : 'test_user',
            'password'  : 'test_pass',
        }
        with open(CONFIG_FILE, 'w') as configFile:
            conf.write(configFile)
    
    conf = configparser.ConfigParser()
    conf.read(CONFIG_FILE)

    ig_bot = InstagramBot(
        conf['INSTAGRAM']['url'],
        conf['INSTAGRAM']['username'],
        conf['INSTAGRAM']['password'])

    ig_bot.follow_user('mister_jagger')
    

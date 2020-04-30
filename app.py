from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# To add inputs and press keys remotely
import time


class TwitterBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot = webdriver.Firefox()  # We can open up the page, visit the links, etc

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)   # Waits for page to load up
        #email = bot.find_element_by_class_name('r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-1inuy60 r-utggzx r-vmopo1 r-1w50u8q r-1lrr6ok r-1dz5y72 r-1ttztb7 r-13qz1uu')
        #email = bot.find_element_by_class_name('email-input')
        #password = bot.find_element_by_class_name('r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-1inuy60 r-utggzx r-vmopo1 r-1w50u8q r-1lrr6ok r-1dz5y72 r-1ttztb7 r-13qz1uu')
        password = bot.find_element_by_name('session[password]')
        email = bot.find_element_by_name('session[username_or_email]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [i.get_attribute('href')
                for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
            fLinks = list(filter(lambda x: 'status' in x,tweetLinks))
            for link in fLinks:
                bot.get(link)
                time.sleep(5)
                try:
                    bot.find_element_by_xpath("//div[@data-testid='like']").click()
                    time.sleep(15)
                except Exception as ex:
                    time.sleep(30)

testBot = TwitterBot('<email id>','<password>')
testBot.login()
testBot.like_tweet('football')	# Change this to whatever you like

# Import Dependencies
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH="C:/Drivers/chromedriver.exe"

driver=webdriver.Chrome()

target_url = "https://twitter.com/Login"

driver.get(target_url)

subject="Itc demerger"

# Setup the log in

sleep(10)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("abhisriv294")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys('Abhiatiitk@2022')
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()

# Search item and fetch it
sleep(5)
search_box = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

sleep(3)
latest = driver.find_element(By.XPATH,"//span[contains(text(),'Latest')]")
latest.click()

# UserTags=[]
# TimeStamps=[]
# Tweets=[]

# # show_more=0

# # def click_show_more():
# #     global show_more
# #     try:
# #         show_more_button = driver.find_element(By.XPATH, '//span[text()="Show more"]')
# #         if show_more_button.is_displayed():
# #             show_more_button.click()
# #             show_more=1
# #             return True
# #     except Exception as e:
# #         show_more=0
# #         pass
# #     return False


# # def click_back_button():
# #     # Find the "Back" button by its data-testid attribute
# #     back_button = driver.find_element(By.XPATH, '//div[@data-testid = "app-bar-back"]')

# #     # Click the "Back" button
# #     back_button.click()

# # Scroll down to load the tweet and click "Show more" until it's no longer available
#     # click_show_more()
#     # time.sleep(2)  # Add a short delay to allow content to load

# articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
# # while True:
# for article in articles:
#     UserTag = driver.find_element(By.XPATH,".//div[@data-testid='User-Name']").text
#     UserTags.append(UserTag)

#     Tweet = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
#     print(Tweet)
#     # # Scroll down to load the tweet and click "Show more" until it's no longer available
#     # click_show_more()
#     # time.sleep(5)  # Add a short delay to allow content to load
#     # # TimeStamp = driver.find_element(By.XPATH,".//time").get_attribute('datetime')
#     # # TimeStamps.append(TimeStamp)

#     # Tweet = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
#     # print(Tweet)

#     # time.sleep(2)

#     # if (show_more==1):
#     #     click_back_button()
#     #     show_more=0
#     #     time.sleep(4)
#     # Tweets.append(Tweet)
        
#         # Reply = driver.find_element(By.XPATH,".//div[@data-testid='reply']").text
#         # Replys.append(Reply)
        
#         # reTweet = driver.find_element(By.XPATH,".//div[@data-testid='retweet']").text
#         # reTweets.append(reTweet)
        
#         # Like = driver.find_element(By.XPATH,".//div[@data-testid='like']").text
#         # Likes.append(Like)
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
#     sleep(3)
#     articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
#     Tweets2 = list(set(Tweets))
#     if len(Tweets2) > 5:
#         break


# UserTags=[]
TimeStamps=[]
Tweets=[]
# Replys=[]
# reTweets=[]
# Likes=[]

articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
while True:
    for article in articles:
        # UserTag = driver.find_element(By.XPATH,".//div[@data-testid='User-Name']").text
        # UserTags.append(UserTag)
        
        TimeStamp = article.find_element(By.XPATH,".//time").get_attribute('datetime')
        TimeStamps.append(TimeStamp)
        
        Tweet = article.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
        Tweets.append(Tweet)
        
        # Reply = driver.find_element(By.XPATH,".//div[@data-testid='reply']").text
        # Replys.append(Reply)
        
        # reTweet = driver.find_element(By.XPATH,".//div[@data-testid='retweet']").text
        # reTweets.append(reTweet)
        
        # Like = driver.find_element(By.XPATH,".//div[@data-testid='like']").text
        # Likes.append(Like)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(3)
    articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    Tweets2 = list(set(Tweets))
    if len(Tweets2) > 200:
        break


# print(len(UserTags),
print(len(TimeStamps),
len(Tweets))
# len(Replys),
# len(reTweets),
# len(Likes))


import pandas as pd

df = pd.DataFrame(zip(TimeStamps,Tweets)
                  ,columns=['TimeStamps','Tweets'])

df.head()
df.to_csv('Tweet_data.csv')
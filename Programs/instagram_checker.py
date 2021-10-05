from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from tkinter import messagebox
import sys

browser=None
wait=None

def initialize(BC):
    global browser,wait
    if BC == 1:
        browser=webdriver.Firefox(executable_path="./drivers/geckodriver")
    elif BC == 2:
        browser=webdriver.Chrome(executable_path="./drivers/chromedriver")
    browser.get('https://www.instagram.com/')
    wait = WebDriverWait(browser, 30)
    

def loginInsta(ID,PASS):
    #login
    time.sleep(3)


    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input"))))
    browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(ID)

    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input"))))
    browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(PASS)

    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div"))))
    browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()

    time.sleep(random.randint(4,7))


def loginFb(ID,PASS):
    #login facebook from instagram
    
    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/button/span[2]"))))
    browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/button/span[2]').click()

    wait.until(EC.presence_of_element_located((By.XPATH,('//*[@id="email"]'))))
    browser.find_element_by_xpath('//*[@id="email"]').send_keys(ID)

    wait.until(EC.presence_of_element_located((By.XPATH,('//*[@id="pass"]'))))
    browser.find_element_by_xpath('//*[@id="pass"]').send_keys(PASS)

    wait.until(EC.presence_of_element_located((By.XPATH,('//*[@id="loginbutton"]'))))
    browser.find_element_by_xpath('//*[@id="loginbutton"]').click()


def formality(NAME):
    #notifcation close
    time.sleep(5)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[4]/div/div/div[3]/button[2]"))))
        browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        time.sleep(random.randint(3,6))
    except:
        print("",end="")

    #click on search
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div"))))
    except:
        messagebox.showerror("error","Network Problem or check login details")
        sys.exit()
    browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div').click()
    time.sleep(random.randint(3,5))

    #fill element to search
    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input"))))
    browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(NAME)
    time.sleep(random.randint(3,7))

               
    #click searched element
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span"))))
    except:
        messagebox.showerror("error","invalid user ID")
    if browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span').text == NAME:
        browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span').click()
    else:
        messagebox.showerror("error","enter a valid public username to search and restart the process")
        sys.exit()
    time.sleep(random.randint(4,6))


def get_owers_owings():
    #get followers
    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span"))))
    followers=browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text

    #get following
    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span"))))
    followings=browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text


    #click on followers
    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span"))))
    browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').click()
    time.sleep(random.randint(4,6))

    #getting the class name of the div for scrolling
    browser.execute_script("a = document.getElementsByClassName('isgrP')[0]")

    #open followers file and start appending followers name
    f=open("./results/followers_list.txt","w+")

    count=0
    for i in range(int(followers)):
        
        if count==0:
            wait.until(EC.presence_of_element_located((By.XPATH,('/html/body/div[4]/div/div[2]/ul/div/li['+str(i+1)+']/div/div[2]/div[1]/div/div/a'))))
            name=browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li['+str(i+1)+']/div/div[2]/div[1]/div/div/a').text
        else:
            wait.until(EC.presence_of_element_located((By.XPATH,('/html/body/div[4]/div/div[2]/ul/div/li['+str(i+1)+']/div/div[1]/div[2]/div[1]/a'))))
            name=browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li['+str(i+1)+']/div/div[1]/div[2]/div[1]/a').text
                
        name=name+"\n"
        f.write(name)
        if((i+1)%12==0):
            time.sleep(0.2)
            browser.execute_script("document.getElementsByClassName('isgrP')[0].scrollTo(0,document.getElementsByClassName('isgrP')[0].scrollHeight)")
            count+=1
            time.sleep(0.4)
        print(name)
            
    f.close()
    time.sleep(2)
    #click on close followers
    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[4]/div/div[1]/div/div[2]/button"))))
    browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()

    #wait
    time.sleep(random.randint(3,5))

    #click on followings
    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span"))))
    browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').click()
    time.sleep(random.randint(3,5))

    #open followings file and start appending followings name
    f=open("./results/followings_list.txt","w+")

    count=0
    for i in range(int(followings)):
        
        if count==0:
            wait.until(EC.presence_of_element_located((By.XPATH,('/html/body/div[4]/div/div[2]/ul/div/li['+str(i+1)+']/div/div[2]/div[1]/div/div/a'))))
            name=browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li['+str(i+1)+']/div/div[2]/div[1]/div/div/a').text
        else:
            wait.until(EC.presence_of_element_located((By.XPATH,('/html/body/div[4]/div/div[2]/ul/div/li['+str(i+1)+']/div/div[1]/div[2]/div[1]/a'))))
            name=browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li['+str(i+1)+']/div/div[1]/div[2]/div[1]/a').text
                
        name=name+"\n"
        f.write(name)
        if((i+1)%12==0):
            time.sleep(0.2)
            browser.execute_script("document.getElementsByClassName('isgrP')[0].scrollTo(0,document.getElementsByClassName('isgrP')[0].scrollHeight)")
            count+=1
            time.sleep(0.3)
        time.sleep(0.2)
        print(name)
            
    f.close()
    time.sleep(2)                                                                                              
    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[4]/div/div[1]/div/div[2]/button"))))
    browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()

def logout_insta():
    #logout Instagram
    time.sleep(4)
    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img"))))
    browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img').click()
    time.sleep(4)
    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[1]/section/main/div/header/section/div[1]/div/button"))))
    browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div/button').click()
    time.sleep(5)
    wait.until(EC.presence_of_element_located((By.XPATH,("/html/body/div[4]/div/div/div/button[9]"))))
    browser.find_element_by_xpath('/html/body/div[4]/div/div/div/button[9]').click()



def logout_facebook():
    #logout after login from facebook
    time.sleep(4)
    browser.get('https://www.facebook.com/')
    time.sleep(6)
    for i in range(5):
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a').click()
    wait.until(EC.presence_of_element_located((By.XPATH,('//*[@id="userNavigationLabel"]'))))
    browser.find_element_by_xpath('//*[@id="userNavigationLabel"]').click()
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,("Log Out"))))
    browser.find_element_by_partial_link_text("Log Out").click()

def handle_files():
    f=open("./results/followers_list.txt","r")
    fowers=f.read()
    f.close()
    followers=list(fowers.split("\n"))

    f=open("./results/followings_list.txt","r")
    fowings=f.read()
    f.close()
    followings=list(fowings.split("\n"))

    f=open("./results/following_not_followerBack_list.txt","w+")
    for i in followings:
        if(i in followers):
            print("",end="")
        else:
            f.write(i+"\n")
            print(i)
    f.close()

    print("\n\n\n")

    f=open("./results/follower_not_followed_list.txt","w+")
    for i in followers:
        if(i in followings):
            print("",end="")
        else:
            f.write(i+"\n")
            print(i)
    f.close()


def execute():
    choice=input("press 1 for instagram and 2 for facebook login\n")
    ID=input("enter login ID\n")
    PASS=input("enter password\n")
    NAME=input("enter the name to search\n")
    execute_GUI([ID,PASS,NAME,choice])

def execute_GUI(param_list):

    initialize(param_list[4])
    choice=param_list[3]
    ID=param_list[0]
    PASS=param_list[1]
    NAME=param_list[2]
    
    if(choice==1):
        try:
            loginInsta(ID,PASS)
        except:
            messagebox.showerror("error","network error or invalid details")
            sys.exit()
            
        formality(NAME)
        
        try:
            get_owers_owings()
        except:
            messagebox.showerror("error","network error please restart process")

        try:
            logout_insta()
        except:
            handle_files()
            messagebox.showerror("error","some error occured please logout and check results")
            sys.exit()
        time.sleep(2)
        browser.close()
        
    elif(choice==2):
        try:
            loginFb(ID,PASS)
        except:
            messagebox.showerror("error","network error or invalid details")
            sys.exit()
        
        formality(NAME)
        try:
            get_owers_owings()
        except:
            messagebox.showerror("error","network error please restart process")
            sys.exit()
        try:
            logout_insta()
        except:
            handle_files()
            messagebox.showerror("error","some error occured please logout and check results")
            sys.exit()
        try:
            logout_facebook()
        except:
            messagebox.showerror("error","please log out from facebook manually and press 'OK'!!")
        time.sleep(2)
        browser.close()

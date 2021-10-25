import requests
import random
import string
import time
import sys
import re
import os
from colorama import Fore, Back, Style
from colorama import init
init()
#==================================================
def line():
    print("==================================================")
#==================================================
print(Fore.LIGHTGREEN_EX)
line()
print("  _               _     _ _ _         ")
print(" | |   _   _  ___(_) __| (_) |_ _   _ ")
print(" | |  | | | |/ __| |/ _` | | __| | | |")
print(" | |__| |_| | (__| | (_| | | |_| |_| |")
print(" |_____\__,_|\___|_|\__,_|_|\__|\__, |")
print("                                |___/ ")
line()
print(Style.RESET_ALL)

#==================================================
print("Target credits : Estimated Time : Extra Notes")
print("3   :   ~27s : Not recommended compared to 4 credits")
print("4   :   ~27s :")
print("5   :   ~43s :")
print("7   :   ~61s :")
print("12  :   ~80s : Default and the recommended, enough for 1:1 ratio with the highest values")
print("22  :   TBD  : TBD, may be EXTREMELY slow")
print("TBD :   TBD  : TBD")

credit_amount = 0
def credit_input():
    try:
        credit_amount = input("\nHow many credits do you want? (default: 12) ")
        if str.strip(credit_amount) == "":
            credit_amount = 12
        credit_amount = int(credit_amount)
        if not credit_amount == 3 and not credit_amount == 4 and not credit_amount == 5 and not credit_amount == 7 and not credit_amount == 12 and not credit_amount == 22:
            print("Invalid amount of credits!")
            credit_input()
            return
    except:
        print("Invalid amount of credits!")
        credit_input()

credit_input()

#==================================================
startTime = time.time()
#================================================== TEMPORARY MAIL-STUFF
API = 'https://www.1secmail.com/api/v1/'
domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
domain = random.choice(domainList)

def generateUserName():
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(10))
    return username

def extract():
    getUserName = re.search(r'login=(.*)&',newMail).group(1)
    getDomain = re.search(r'domain=(.*)', newMail).group(1)
    return [getUserName, getDomain]

#CHECKS MAILS AND STORES CONTENT IN .TXT FILE
def checkMails():
    reqLink = f'{API}?action=getMessages&login={extract()[0]}&domain={extract()[1]}'
    req = requests.get(reqLink).json()
    length = len(req)
    if length == 0:
        print("Mailbox is empty. Hold tight. Mailbox is refreshed automatically every 2 seconds.")
        return False
    else:
        idList = []
        for i in req:
            for k,v in i.items():
                if k == 'id':
                    mailId = v
                    idList.append(mailId)

        x = 'mails' if length > 1 else 'mail'
        print(f"You've received verification mail")

        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, r'verifMails')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

        for i in idList:
            msgRead = f'{API}?action=readMessage&login={extract()[0]}&domain={extract()[1]}&id={i}'
            req = requests.get(msgRead).json()
            for k,v in req.items():
                if k == 'from':
                    sender = v
                if k == 'subject':
                    subject = v
                if k == 'date':
                    date = v
                if k == 'textBody':
                    content = v

            mail_file_path = os.path.join(final_directory, f'verifMail.txt')

            with open(mail_file_path,'w') as file:
                file.write("Sender: " + sender + '\n' + "To: " + mail + '\n' + "Subject: " + subject + '\n' + "Date: " + date + '\n' + "Content: " + content + '\n')

        return True

newMail = f"{API}?login={generateUserName()}&domain={domain}"
reqMail = requests.get(newMail)
mail = f"{extract()[0]}@{extract()[1]}"
#pyperclip.copy(mail)
print(Fore.LIGHTBLUE_EX)
line()
print("\nYour temporary email is " + mail + "\n")
line()
print(Style.RESET_ALL)

#================================================== REGISTRATION
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


print(Fore.YELLOW)
s = Service("./msedgedriver.exe")
driver = webdriver.Edge(service = s) #launch browser
driver.get("https://creator.nightcafe.studio/login?view=password-signup") #goto site

loaded = False
while not loaded:
    try:
        driver.find_element(By.NAME,"email").send_keys(mail)
        break
    except:
        print("Registration page not loaded yet")
    time.sleep(0.2)

password = "12345678"
driver.find_element(By.NAME,"password").send_keys(password)

driver.find_element(By.NAME,"confirmPassword").send_keys("12345678")

while not loaded:
    try:
        driver.find_element(By.CLASS_NAME,"css-4xonwm").click()
        break
    except:
        print("Button Reg-page not found")
    time.sleep(0.2)

while True:
    time.sleep(2)
    if checkMails():
        break

verifFile = open('verifMails/verifMail.txt', 'r')
link = ""
for line in verifFile:
    if "https://" in line:
        print("Verification Link Found.")
        link = line
        break

#================================================== VERIF SITE
driver.get(link)
while not loaded:
    try:
        driver.find_element(By.CLASS_NAME,"firebaseui-id-submit.firebaseui-button.mdl-button.mdl-js-button.mdl-button--raised.mdl-button--colored").click()
        break
    except:
        print("Verif site not loaded")
    time.sleep(0.2)

loaded = False
while not loaded:
    try:
        driver.find_element(By.CLASS_NAME,"css-1tzvq1v").click()
        break
    except:
        print("css-1tzvq1v not found")
    time.sleep(0.2)

loaded = False
while not loaded:
    try:
        driver.find_element(By.CLASS_NAME,"css-tpvdoh").click()
        break
    except:
        print("css-tpvdoh not found")
    time.sleep(0.2)

#================================================== GET FREE CREDIT
if not credit_amount == 3:
    time.sleep(2)
    driver.get("https://creator.nightcafe.studio/account/edit-profile")

    while not loaded:
        try:
            driver.find_element(By.CLASS_NAME,"css-qzr1ap").click()
            break
        except:
            print("Page not loaded")
        time.sleep(0.2)

    while not loaded:
        try:
            driver.find_element(By.CLASS_NAME,"css-hvws00").click()
            break
        except:
            print("Image button not responding")
        time.sleep(0.2)

    while not loaded:
        try:
            driver.find_element(By.CLASS_NAME,"css-tpvdoh").click()
            break
        except:
            print("Done Button not responding")
        time.sleep(0.2)

    while not loaded:
        try:
            driver.find_element(By.NAME,"username").send_keys(mail[0:10])
            break
        except:
            print("Username input not found")
        time.sleep(0.2)
        
    driver.find_element(By.NAME,"displayName").send_keys("t")

    driver.find_element(By.NAME,"bio").send_keys("t")

    driver.find_element(By.CLASS_NAME,"css-17tew97").click()

# aqualxx was here
#================================================== MORE FREE CREDIT
if not credit_amount == 3 and not credit_amount == 4:
    like_amount = 0
    if credit_amount == 5:
        like_amount = 10
    if credit_amount == 7:
        like_amount = 50
    if credit_amount == 12:
        like_amount = 100
    if credit_amount == 22:
        like_amount = 500
    time.sleep(2)
    driver.get("https://creator.nightcafe.studio/recent")

    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'css-vkhmfo')))

    # def like_post_no(index):
    #    element = driver.find_elements(By.XPATH,'//div[@class="css-jcvd79"]/button[1][@title="Like"]')[index]
    #    element.click()

    post_num = 0
    while True:
        try:
            element = driver.find_elements(By.XPATH,'//div[@class="css-jcvd79"]/button[1][@title="Like"]')[0]
            element.click()
            driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)

            post_num = post_num + 1
            if (post_num >= like_amount):
                break
        except:
            print("Can't find like button")
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight-100);")
            time.sleep(0.3)

time.sleep(2)
driver.get("https://creator.nightcafe.studio/create/text-to-image")

# print(Style.RESET_ALL)
#======================================== COMPLETED

f = open("accounts.txt", "a")
print(Fore.GREEN)
print("============================")
print("Account creation succesfull.")
print("Email:", mail)
print("Password:", password)
print("Time elapsed:", time.time() - startTime, "seconds")
print("Account saved to accounts.txt")
print("============================")

f.write("============================\n")
f.write("Email: "+mail+"\n")
f.write("Password: "+password+"\n")
f.write("============================\n")

f.close()
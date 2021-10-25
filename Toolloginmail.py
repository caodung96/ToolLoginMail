import threading,time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def regacc(acc):
    browser = webdriver.Firefox()
    #width=browser.get_window_size()['width']
    #height=browser.get_window_size()['height']
    #browser.set_window_size(width/4, height/2)
    #browser.set_window_position(0,0, windowHandle='current')
    browser.get('https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    #time.sleep(5)
    try:
        myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'identifierId')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    mail=browser.find_element_by_xpath('//*[@id="identifierId"]')
    mail.send_keys(acc)
    next=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
    next.click()
    try:
        myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'passwordNext')))
        time.sleep(2)
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    password=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    password.send_keys("123456789")

    try:
        #/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span
        #next=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
        next=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
        next.click()
    except:
        print()
    try:
        myElem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, 'accept')))
        dongy=browser.find_element_by_xpath('//*[@id="accept"]')
        dongy.click()
    except TimeoutException:
        print ("Loading took too much time!")
    time.sleep(2)
    try:
        xacnhan=browser.find_element_by_xpath('/html/body/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/span/span')
        xacnhan.click()
    except:
        print()

    time.sleep(7)
    try:
        ok=browser.find_element_by_class_name('h-De-Vb h-De-Y')
        ok.click()
    except:
        browser.get('https://drive.google.com/drive/my-drive')
        time.sleep(3)
        print()
    new=browser.find_element_by_class_name('a-w-d-aa-zd')
    new.click()

    time.sleep(5)
    moi=browser.find_element_by_class_name('a-v-T')
    moi.click()
    #/html/body/div[18]/div/div[1]/div/span[2]/span/div
    #//*[@id=":5v.ie"]
    try:
        newfolder=browser.find_element_by_id(':5v.ie')
        newfolder.send_keys("all")
    except:
        try:
            newfolder=browser.find_element_by_id(':5w.ie')
            newfolder.send_keys("all")
        except:
            print()
    #/html/body/div[20]/div[3]/button[2]
    time.sleep(2)
    tao=browser.find_element_by_name('ok')
    tao.click()
    try:
        tao=browser.find_element_by_name('ok')
        tao.click()
    except:
        print()
    time.sleep(3)
    #/html/body/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/button[1]/div[2]
    browser.get('https://accounts.google.com/signin/v2/challenge/pwd?continue=https%3A%2F%2Fmyaccount.google.com%2Fsigninoptions%2Fpassword%3Fcontinue%3Dhttps%3A%2F%2Fmyaccount.google.com%2Fpersonal-info%3Fpli%253D1&service=accountsettings&osid=1&rart=ANgoxceZ0PtRateSaEQGsoq947FeNsPIAbVsLWCQ5KjjFp_iMqu27wzu6brKJf4-6KyakMU3fFKRuid7L3t2WBEwqz-h5kf0Lw&TL=AM3QAYaYvcMtSAjc-1d6oBg9yu7MmXD47pOajq4D-OSJZ1AZBCALge5gJsnmCxgB&flowName=GlifWebSignIn&cid=1&flowEntry=ServiceLogin')
    #/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/input
    password=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    password.send_keys("123456789")
    try:
        next=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
        next.click()
    except:
        print()
    #//*[@id="i4"]
    try:
        myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'i4')))
        time.sleep(2)
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    npassword=browser.find_element_by_xpath('//*[@id="i4"]')
    npassword.send_keys("Sunny2015@")
    #//*[@id="i8"]
    rpassword=browser.find_element_by_xpath('//*[@id="i8"]')
    rpassword.send_keys("Sunny2015@")
    #/html/body/c-wiz/div/div[3]/c-wiz/div/div[2]/form/div/div[2]/div/div/button/
    time.sleep(5)
    change=browser.find_element_by_xpath('/html/body/c-wiz/div/div[3]/c-wiz/div/div[2]/form/div/div[2]/div/div/button/span')
    change.click()
    time.sleep(7)
    browser.close()
    #search=browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()

def login(acc,browser):
    #width=browser.get_window_size()['width']
    #height=browser.get_window_size()['height']
    #browser.set_window_size(width/4, height/2)
    #browser.set_window_position(0,0, windowHandle='current')
    mail=browser.find_element_by_xpath('//*[@id="identifierId"]')
    mail.send_keys(acc)
    next=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
    next.click()
    try:
        myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'passwordNext')))
        time.sleep(2)
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    password=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    password.send_keys("123456789")
    try:
        #/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span
        #next=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
        next=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
        next.click()
    except:
        print()
    time.sleep(2)
    try:
        myElem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, 'accept')))
        dongy=browser.find_element_by_xpath('//*[@id="accept"]')
        dongy.click()
    except TimeoutException:
        print ("Loading took too much time!")

    time.sleep(5)
    try:
        pw=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input')
        pw.send_keys("Suny2015@")
        rpw=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        rpw.send_keys("Suny2015@")
        time.sleep(2)
        next=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
        next.click()
    except:
        try:
            pw=browser.find_element_by_xpath('//*[@id="Password"]')
            pw.send_keys("Suny2015@")
            rpw=browser.find_element_by_xpath('//*[@id="ConfirmPassword"]')
            rpw.send_keys("Suny2015@")
            time.sleep(2)
            next=browser.find_element_by_xpath('//*[@id="submit"]')
            next.click()
        except:
            print()
    time.sleep(3)
    #/html/body/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/button[1]/div[2]
    browser.get('https://accounts.google.com/signin/v2/challenge/pwd?continue=https%3A%2F%2Fmyaccount.google.com%2Fsigninoptions%2Fpassword%3Fcontinue%3Dhttps%3A%2F%2Fmyaccount.google.com%2Fpersonal-info%3Fpli%253D1&service=accountsettings&osid=1&rart=ANgoxceZ0PtRateSaEQGsoq947FeNsPIAbVsLWCQ5KjjFp_iMqu27wzu6brKJf4-6KyakMU3fFKRuid7L3t2WBEwqz-h5kf0Lw&TL=AM3QAYaYvcMtSAjc-1d6oBg9yu7MmXD47pOajq4D-OSJZ1AZBCALge5gJsnmCxgB&flowName=GlifWebSignIn&cid=1&flowEntry=ServiceLogin')
    #/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/input
    password=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    password.send_keys("123456789")
    try:
        next=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
        next.click()
    except:
        print()
    #//*[@id="i4"]
    try:
        myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'i4')))
        time.sleep(2)
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    npassword=browser.find_element_by_xpath('//*[@id="i4"]')
    npassword.send_keys("Sunny2015@")
    #//*[@id="i8"]
    rpassword=browser.find_element_by_xpath('//*[@id="i8"]')
    rpassword.send_keys("Sunny2015@")
    #/html/body/c-wiz/div/div[3]/c-wiz/div/div[2]/form/div/div[2]/div/div/button/
    time.sleep(5)
    change=browser.find_element_by_xpath('/html/body/c-wiz/div/div[3]/c-wiz/div/div[2]/form/div/div[2]/div/div/button/span')
    change.click()
    time.sleep(7)


    #time.sleep(2)
    #browser.get('https://drive.google.com/drive/my-drive')
    #time.sleep(3)
    #new=browser.find_element_by_class_name('a-w-d-aa-zd')
    #new.click()

    #time.sleep(5)
    #moi=browser.find_element_by_class_name('a-v-T')
    #moi.click()
    #/html/body/div[18]/div/div[1]/div/span[2]/span/div
    #//*[@id=":5v.ie"]
    #try:
        #newfolder=browser.find_element_by_id(':5v.ie')
        #newfolder.send_keys("all")
    #except:
        #try:
            #newfolder=browser.find_element_by_id(':5w.ie')
            #newfolder.send_keys("all")
        #except:
            #print()
    #/html/body/div[20]/div[3]/button[2]
    #time.sleep(2)
    #tao=browser.find_element_by_name('ok')
    #tao.click()
    #try:
        #tao=browser.find_element_by_name('ok')
        #tao.click()
    #except:
        #print()
    time.sleep(5)
    browser.get('https://accounts.google.com/Logout')
    time.sleep(2)    
    clickuse=browser.find_element_by_class_name('UXurCe')
    clickuse.click()
    time.sleep(2)
    return browser
    #Password

def regaccnew(acc,browser):
    try:
        myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'identifierId')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    mail=browser.find_element_by_xpath('//*[@id="identifierId"]')
    mail.send_keys(acc)
    next=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
    next.click()
    try:
        myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'passwordNext')))
        time.sleep(2)
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    password=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    password.send_keys("123456789")

    try:
        #/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span
        #next=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
        next=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
        next.click()
    except:
        print()
        
    time.sleep(2)
    try:
        myElem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, 'accept')))
        dongy=browser.find_element_by_xpath('//*[@id="accept"]')
        dongy.click()
    except TimeoutException:
        print ("Loading took too much time!")
    browser.get('https://accounts.google.com/signin/v2/challenge/pwd?continue=https%3A%2F%2Fmyaccount.google.com%2Fsigninoptions%2Fpassword%3Fcontinue%3Dhttps%3A%2F%2Fmyaccount.google.com%2Fpersonal-info%3Fpli%253D1&service=accountsettings&osid=1&rart=ANgoxceZ0PtRateSaEQGsoq947FeNsPIAbVsLWCQ5KjjFp_iMqu27wzu6brKJf4-6KyakMU3fFKRuid7L3t2WBEwqz-h5kf0Lw&TL=AM3QAYaYvcMtSAjc-1d6oBg9yu7MmXD47pOajq4D-OSJZ1AZBCALge5gJsnmCxgB&flowName=GlifWebSignIn&cid=1&flowEntry=ServiceLogin')
    #/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/input
    password=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    password.send_keys("123456789")
    try:
        next=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
        next.click()
    except:
        print()
    #//*[@id="i4"]
    try:
        myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'i4')))
        time.sleep(2)
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    npassword=browser.find_element_by_xpath('//*[@id="i4"]')
    npassword.send_keys("Sunny2015@")
    #//*[@id="i8"]
    rpassword=browser.find_element_by_xpath('//*[@id="i8"]')
    rpassword.send_keys("Sunny2015@")
    #/html/body/c-wiz/div/div[3]/c-wiz/div/div[2]/form/div/div[2]/div/div/button/
    time.sleep(5)
    change=browser.find_element_by_xpath('/html/body/c-wiz/div/div[3]/c-wiz/div/div[2]/form/div/div[2]/div/div/button/span')
    change.click()
    time.sleep(7)
    browser.get('https://accounts.google.com/Logout')
    time.sleep(2)    
    clickuse=browser.find_element_by_class_name('UXurCe')
    clickuse.click()
    time.sleep(2)
    return browser


fileObject = open("Acc.txt", "r")
data = fileObject.read().split('\n')  
browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Den&utm_medium=button&utm_campaign=web&utm_content=gotodrive&usp=gtd&ltmpl=drive&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    #time.sleep(5)
try:
    myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'identifierId')))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")

for x in data:
    browser=regaccnew(x,browser)
    
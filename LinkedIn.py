from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time



#to press the continue to next step button
def next_step():
    next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
    next_button.click()
    time.sleep(2)

#to discard the application
def abort_application():
    cancel_application = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
    cancel_application.click()

    time.sleep(2)
    confirmation = driver.find_element(By.CSS_SELECTOR, value=".artdeco-modal__confirm-dialog-btn")
    confirmation.click()

chrome_driver = webdriver.ChromeOptions()
chrome_driver.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_driver)
#make sure that the link you will paste is the job link with easy apply button
#make sure you resume is uploaded to your account
#only works for applications which require you to enter the phone number, and date of birth if asked
driver.get("")
sign_in = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in.click()

time.sleep(2)

#to select the email and password value on the webpage
email = driver.find_element(By.CSS_SELECTOR, value=".card-layout #username")
password = driver.find_element(By.CSS_SELECTOR, value=".card-layout #password")

#to enter the email ID on the webpage from user
enter_userID = input("Enter your Email ID:\n ")
email.send_keys(enter_userID)

#to enter the password from the user
enter_userPassword = input("Enter your password:\n ")
password.send_keys(enter_userPassword)

sign_in_button = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
sign_in_button.click()

#in case of a captcha, the user will have to clear the captcha manually and once cleared, they can press the "Enter" key to continue the execution of the program
input("Press enter when cleared captcha.")

#to find the easy apply button on the job LinkedIn webpage
easy_apply = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
easy_apply.click()
time.sleep(2)

#to find the details required by the job on the webpage to be filled by the user if an information is missing
job_details = driver.find_elements(By.CSS_SELECTOR, value=".jobs-easy-apply-content")

for job in job_details:
    
    phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
    if phone.text == "":
        PHONE = input("Enter your phone number: \n")
        phone.send_keys(PHONE)

# not every job will have for Date Of Birth, in such case the try method will check if there any detail being asked regarding the DoB, in case there is already then program
# will not execute this line and will pass it
    try:
        DOB = driver.find_element(By.CSS_SELECTOR, value="input[id*=date-picker]")
        dob = input("Enter your Date Of Birth (Month/Date/Year): ")
        DOB.send_keys(dob)
    except NoSuchElementException:
        pass
    
    

for _ in range(2):
    next_step()

#confirmation for the experience
experience = input("Do you have any prior work experience? Type 'No' if none.")
if experience.lower() == "no":
    cancel_button = driver.find_element(By.XPATH, value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/div[1]/div/div[2]/button[1]")
    cancel_button.click()
else:
    print("You did not give an input.")

time.sleep(3)

#if the job application is asking for notice period and CTC then it will be executed otherwise it will be passed
try: 
    next_step()


    notice_period = driver.find_element(By.ID, value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3782263487-107345925-numeric")
    noticeperiod_time = input("Enter the notice period time: ")
    notice_period.send_keys(noticeperiod_time)



    time.sleep(2)

    ctc = driver.find_element(By.ID, value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3782263487-107345917-numeric")
    ctc_amount = input("Enter your CTC in INR: ")
    ctc.send_keys(ctc_amount)
except NoSuchElementException:
    pass

time.sleep(2)

#to finalise the application
review = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Review your application"]')
review.click()

time.sleep(2)

#to uncheck the follow the company's follow page check button
follow_page = driver.find_element(By.XPATH, value="/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[1]/label")
follow_page.click()

time.sleep(2)

input("Press 'Enter' to submit the application.")
time.sleep(2)

#to submit the application by pressing the submit application button on the job application
# submit_application = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Submit application"]')
# submit_application.click()

print("Your application has been submitted.")
time.sleep(5)

driver.quit()

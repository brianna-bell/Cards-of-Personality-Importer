from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import csv

#Set up Firefox WebDriver
options = Options()
options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
driver = webdriver.Firefox()
driver.get('https://www.cardsofpersonality.com/edit-deck/testubg-8936?secret=6758d9c8fb144d00392d147e')

# Wait for the table to appear on the page/for the page to fully load
try:
    # You could also wait for an element inside the table, e.g., a button
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )
    print("Table is loaded!")
except TimeoutError:
    print("Timed out waiting for table to load.")


# check for existing white cards
# numWhite = driver.find_element(By.CLASS_NAME, 'sc-pjHjD.CNlcm')
# if (int(numWhite.text) > 0):

#     # white cards - expand button
#     expandbut = driver.find_element(By.CLASS_NAME, 'sc-prorn.fpBoEr')
#     expandbut.click()

#     # white cards - get all current cards and delete them one by one
#     buttons = driver.find_elements(By.CLASS_NAME, 'sc-pbYBj.fWqrEZ')

#     deletedcards = 0

#     for pushy in buttons:
#         WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable(pushy)).click()
#         #pushy.click()
#         alert = Alert(driver)
#         try:
#             # Try to switch to the alert
#             alert = Alert(driver)
#             # If no exception is raised, the alert is present
#             alert.accept()  # Accepts the alert
#             #print("Alert accepted")
#         except NoAlertPresentException:
#             num = 567
#         deletedcards += 1
#         print('{} white cards deleted'.format(deletedcards))

# # check for existing black cards
# numBlack = driver.find_element(By.CLASS_NAME, 'sc-pjHjD.CNlcm')
# if (int(numBlack.text) > 0):
#     # black cards - expand button
#     expandbut = driver.find_element(By.CLASS_NAME, 'sc-prorn.fpBoEr')
#     expandbut.click()

#     # black cards - get all current cards and delete them one by one
#     buttons = driver.find_elements(By.CLASS_NAME, 'sc-pbYBj.fWqrEZ')

#     deletedcards = 0

#     for pushy in buttons:
#         WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable(pushy)).click()
#         #pushy.click()
#         alert = Alert(driver)
#         try:
#             # Try to switch to the alert
#             alert = Alert(driver)
#             # If no exception is raised, the alert is present
#             alert.accept()  # Accepts the alert
#             #print("Alert accepted")
#         except NoAlertPresentException:
#             num = 567
#         deletedcards += 1
#         print('{} black cards deleted'.format(deletedcards))


# with open('baiwhite.tsv', newline='', encoding="utf8") as csvfile:

#    reader2 = csv.reader(csvfile, delimiter='\n', quotechar='|')

#    for row in reader2:
        
#         rowStr = ''.join(row)
#         rowNoSpaces = rowStr.strip(' \t\n\r')
#         rowDone = rowNoSpaces.replace('\"\"','\"')
#         print(rowDone)

#         whitecardelem = driver.find_element(By.ID, 'AddaWhiteCard')
#         whitecardelem.send_keys(rowDone)

#         whitecardelem.submit()

with open('baiblack.tsv', newline='', encoding="utf8") as csvfile:

   reader3 = csv.reader(csvfile, delimiter='\n', quotechar='|')

   for row in reader3:
        
        rowStr = ''.join(row)
        rowNoSpaces = rowStr.strip(' \t\n\r')
        rowDone = rowNoSpaces.replace('\"\"','\"')
        print(rowDone)

        blackcardelem = driver.find_element(By.ID, 'AddaBlackCard')
        blackcardelem.send_keys(rowDone)

        blackcardelem.submit()



# Close the driver
driver.quit()
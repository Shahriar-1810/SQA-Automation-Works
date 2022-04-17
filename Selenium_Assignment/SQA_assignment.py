from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import time






#driver = webdriver.Chrome(ChromeDriverManager().install())



#-----------------------------------------------------------------------------------------------------------------------
#going to the url with the webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Nafis\\Desktop\\chromedriver_win32\\chromedriver.exe")


driver.implicitly_wait(5)

driver.get("http://automationpractice.com/index.php")
print(driver.title)


driver.find_element(By.CLASS_NAME, 'login').click()  #clicking the sign in button
#signIn = driver.find_elements(By.CSS_SELECTOR, 'div.header_user_info a')
#signIn[0].click()                                                        --> line27,28 is another way but complicated way to click on the sign in                                                                                                                          button

#-----------------------------------------------------------------------------------------------------------------------
# #creating the first account
driver.find_element(By.ID,'email_create').send_keys("nafis.3@hotmail.com") ##line 32--> filling up the email address space of create account                                                                                              section by using its unique id from the inspect

#create = driver.find_elements(By.CSS_SELECTOR, 'div.submit button i') ##clicking on the create account button by using Css                                                                     selector, meaning where it is actually situated in term of div,ul,li,span etc
#create[0].click()                                                      --->line 34,35 is another way but complicated way of clicking the create                                                                                                       account button
driver.find_element(By.ID, 'SubmitCreate').click()  # Easy way to clicking on create account button


#in line 40-63--> clicking and filling up the space bars by using their unique id
driver.find_element(By.ID, 'id_gender1').click()
driver.find_element(By.ID, 'customer_firstname').send_keys("Nafis")
driver.find_element(By.ID, 'customer_lastname').send_keys("Iqbal")
driver.find_element(By.ID, 'passwd').send_keys("admin@1234")

driver.find_element(By.ID, 'days').send_keys("18")
driver.find_element(By.ID, 'months').send_keys("October")
driver.find_element(By.ID, 'years').send_keys("1998")

driver.find_element(By.ID, 'optin').click()

#driver.find_element(By.ID, 'firstname').send_keys("Nafis")
#driver.find_element(By.ID, 'lastname').send_keys("Iqbal")

driver.find_element(By.ID, 'company').send_keys("BS23")
driver.find_element(By.ID, 'address1').send_keys("Block-f, Section-2, Dhaka-1216")
driver.find_element(By.ID, 'address2').send_keys("House-9, Aveneue-1")
driver.find_element(By.ID, 'city').send_keys("Mirpur")
driver.find_element(By.ID, 'id_state').send_keys("Texas")
driver.find_element(By.ID, 'postcode').send_keys("00000")
driver.find_element(By.ID, 'id_country').send_keys("United States")
driver.find_element(By.ID, 'other').send_keys("None")
driver.find_element(By.ID, 'phone').send_keys("0194830")
driver.find_element(By.ID, 'phone_mobile').send_keys("01746086")

driver.find_element(By.ID, 'submitAccount').click()  #easy way to click register button
#register = driver.find_elements(By.CSS_SELECTOR, 'button span i')
#register[0].click()                                              #line66,67-->another way but a complicated way of clicking register button

driver.find_element(By.CLASS_NAME, 'logout').click() #clicking log out using the class name from its inspect
#time.sleep(5)
#driver.quit()
# #------------------------------------------------------------------------------------------------------------------------
#creating 2nd account
#in line 75-104--> clicking and filling up the space bars by using their unique id
driver.find_element(By.ID,'email_create').send_keys("nafis.4@hotmail.com")

#create = driver.find_elements(By.CSS_SELECTOR, 'div.submit button i')
#create[0].click()
driver.find_element(By.ID, 'SubmitCreate').click()

driver.find_element(By.ID, 'id_gender1').click()
driver.find_element(By.ID, 'customer_firstname').send_keys("Shakib")
driver.find_element(By.ID, 'customer_lastname').send_keys("Iqbal")
driver.find_element(By.ID, 'passwd').send_keys("admin@1234")

driver.find_element(By.ID, 'days').send_keys("18")
driver.find_element(By.ID, 'months').send_keys("November")
driver.find_element(By.ID, 'years').send_keys("1998")

driver.find_element(By.ID, 'optin').click()

#driver.find_element(By.ID, 'firstname').send_keys("Nafis")
#driver.find_element(By.ID, 'lastname').send_keys("Iqbal")

driver.find_element(By.ID, 'company').send_keys("BS23")
driver.find_element(By.ID, 'address1').send_keys("Block-f, Section-2, Dhaka-1216")
driver.find_element(By.ID, 'address2').send_keys("House-9, Aveneue-1")
driver.find_element(By.ID, 'city').send_keys("Mirpur")
driver.find_element(By.ID, 'id_state').send_keys("Texas")
driver.find_element(By.ID, 'postcode').send_keys("00000")
driver.find_element(By.ID, 'id_country').send_keys("United States")
driver.find_element(By.ID, 'other').send_keys("None")
driver.find_element(By.ID, 'phone').send_keys("0194830")
driver.find_element(By.ID, 'phone_mobile').send_keys("01746086")

driver.find_element(By.ID, 'submitAccount').click() #easy way to click register button

driver.find_element(By.CLASS_NAME, 'logout').click() #clicking log out using the class name from its inspect

#-----------------------------------------------------------------------------------------------------------------------

#logging in with the 1st created account from the section 'Already Registered'
driver.find_element(By.ID, 'email').send_keys("nafis.3@hotmail.com")
driver.find_element(By.ID, 'passwd').send_keys("admin@1234")
driver.find_element(By.ID, 'SubmitLogin').click()

#-----------------------------------------------------------------------------------------------------------------------
#From here the task 4 of the pdf file starts and end at task 7 for the 1st user

driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a').click()  #clicking on the DRESSES button using Xpath which can be found from the inspect of that particular portion(DRESSES)

driver.find_element(By.XPATH, '//*[@id="categories_block_left"]/div/ul/li[1]/a').click() ##clicking on the Casual Dresses button using Xpath which can be found from the inspect of that particular portion(Casual Dresses)

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/div[2]/a[1]').click() #clicking on the Add Cart button using its Xpath which can be found from its inpect by clicking right button of the mouse

driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span/i').click() #clicking the option 'continue shopping by using its xpath
# cont = driver.find_elements(By.CSS_SELECTOR, 'div.button-container span i')
# cont[0].click()                                            #--> another complicated way of clicking the option 'continue shopping'

driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[3]/a').click()  #clicking on T-Shirt button by usiing its xpath from its inspect


driver.find_element(By.ID, 'color_2').click() #Filtering the list with blue color by using its unique id 'color_2' which is found from its inspect

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[3]/div[1]/p/button/span').click() # clicking the option 'add to cart' by using its xpath

driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a/span/i').click() #clicking 'proceed to checkout' after adding the product to the cart and the next page will be summary page.  Used xpath again

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]/span/i').click() #again clicking 'proceed to checkout' button from the current page which is the summary page and it will go to next page that is address segment after clicking proceed. Again used the xpath.

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/form/p/button/span/i').click() #again clicking 'proceed to checkout' button from the current page which is the address page and it will go to shipping segment page after clicking proceed. Again used the xpath.

driver.find_element(By.NAME, 'cgv').click() #giving tick to the agreement checkbox by using its unique name attribute from inspect
driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/form/p/button/span/i').click() #again clicking 'proceed to checkout' button from the current page which is the shipping page and it will go to payment segment page after clicking proceed. Again used the xpath.

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/div[3]/div[2]/div/p/a').click() #clicking 'Pay by check' button by using its xpath and it will lead the page to confirm order page

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/form/p/button/span/i').click() # clicking the button 'I confirm my order' by using its xpath

driver.find_element(By.CLASS_NAME, 'logout').click() #clicking the sign out button by using its unique class name

#------------------------------------------------------------------------------------------------------------------------------------------------

#logging in with the 2nd created account from the section 'Already Registered'
driver.find_element(By.ID, 'email').send_keys("nafis.4@hotmail.com")
driver.find_element(By.ID, 'passwd').send_keys("admin@1234")
driver.find_element(By.ID, 'SubmitLogin').click()

#-----------------------------------------------------------------------------------------------------------------------
#From here the task 4 of the pdf file starts and end at task 7 for the 2nd user

driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a').click()  #clicking on the DRESSES button using Xpath which can be found from the inspect of that particular portion(DRESSES)

driver.find_element(By.XPATH, '//*[@id="categories_block_left"]/div/ul/li[1]/a').click() ##clicking on the Casual Dresses button using Xpath which can be found from the inspect of that particular portion(Casual Dresses)

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/div[2]/a[1]').click() #clicking on the Add Cart button using its Xpath which can be found from its inpect by clicking right button of the mouse

driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span/i').click() #clicking the option 'continue shopping by using its xpath
# cont = driver.find_elements(By.CSS_SELECTOR, 'div.button-container span i')
# cont[0].click()                                            #--> another complicated way of clicking the option 'continue shopping'

driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[3]/a').click()  #clicking on T-Shirt button by usiing its xpath from its inspect


driver.find_element(By.ID, 'color_2').click() #Filtering the list with blue color by using its unique id 'color_2' which is found from its inspect

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[3]/div[1]/p/button/span').click() # clicking the option 'add to cart' by using its xpath

driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a/span/i').click() #clicking 'proceed to checkout' after adding the product to the cart and the next page will be summary page.  Used xpath again

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]/span/i').click() #again clicking 'proceed to checkout' button from the current page which is the summary page and it will go to next page that is address segment after clicking proceed. Again used the xpath.

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/form/p/button/span/i').click() #again clicking 'proceed to checkout' button from the current page which is the address page and it will go to shipping segment page after clicking proceed. Again used the xpath.

driver.find_element(By.NAME, 'cgv').click() #giving tick to the agreement checkbox by using its unique name attribute from inspect
driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/form/p/button/span/i').click() #again clicking 'proceed to checkout' button from the current page which is the shipping page and it will go to payment segment page after clicking proceed. Again used the xpath.

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/div[3]/div[2]/div/p/a').click() #clicking 'Pay by check' button by using its xpath and it will lead the page to confirm order page

driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[3]/div/form/p/button/span/i').click() # clicking the button 'I confirm my order' by using its xpath

driver.find_element(By.CLASS_NAME, 'logout').click() #clicking the sign out button by using its unique class name

time.sleep(5)
driver.quit()


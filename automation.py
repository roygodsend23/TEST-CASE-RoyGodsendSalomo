""" 
This is a script to create transaction for flight product using tiket.com until payment page.

Transaction information :
{
    'nama_lengkap' : 'Roy Godsend Salomo',
    'phone' : 82161869999,
    'email': 'roygodsend2301@gmail.com',
    'from' : 'Jakarta',
    'destination' : 'Surabaya',
    'date' : '27 July 2021',
}

Last Modified : 15:27 07/07/2021
"""

from selenium import webdriver

import time


chromedriver_location = './chromedriver'

# access tiket.com using webdriver
driver = webdriver.Chrome(chromedriver_location)
driver.get('https://m.tiket.com/')
flight_button = '/html/body/div[1]/div/main/div/div[2]/div/div[1]/div/div[8]/a'

driver.find_element_by_xpath(flight_button).click()



# flight form
city_from_button = '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/span'
driver.find_element_by_xpath(city_from_button).click()

driver.implicitly_wait(2)


city_from_form = '/html/body/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[2]'
driver.find_element_by_xpath(city_from_form).click()

city_destination_button = '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/span'
driver.find_element_by_xpath(city_destination_button).click()

driver.implicitly_wait(2)

city_destination_form = '/html/body/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[3]'
driver.find_element_by_xpath(city_destination_form).click()


flight_date_form = '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]'
driver.find_element_by_xpath(flight_date_form).click()

time.sleep(1)
driver.implicitly_wait(2)

flight_date_button = '/html/body/div[2]/div[7]/div/div/div/div/div[2]/div/div/div[2]/div/div[3]/div[5]/div[3]'
driver.find_element_by_xpath(flight_date_button).click()


driver.implicitly_wait(2)
search_flight_button = '/html/body/div[1]/div/div[2]/div/div[2]/div[7]/button'
driver.find_element_by_xpath(search_flight_button).click()

# Flight ticket select
time.sleep(5)

ppkm_confirm = '/html/body/div[10]/div[2]/div[2]/button[2]'
driver.find_element_by_xpath(ppkm_confirm).click()

driver.implicitly_wait(5)
info_confirm = '/html/body/div[1]/div/div[2]/div[1]/div[2]/button'
driver.find_element_by_xpath(info_confirm).click()

driver.implicitly_wait(5)
ticket = '/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div'
driver.find_element_by_xpath(ticket).click()


# Flight ticket passenger form
driver.implicitly_wait(5)
mini_contact_form = '/html/body/div[1]/div/div[2]/div/form/div[1]/div/div[2]/div/div'
driver.find_element_by_xpath(mini_contact_form).click()

# Change passenger information here
transaction = {
    'nama_lengkap' : 'Roy Godsend Salomo',
    'phone' : 82161869999,
    'email': 'roygodsend2301@gmail.com'
}

driver.implicitly_wait(5)
transaction_name = '/html/body/div[2]/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/input'
driver.find_element_by_xpath(transaction_name).send_keys(transaction['nama_lengkap'])

driver.implicitly_wait(5)

transaction_title = '/html/body/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div/input'
driver.find_element_by_xpath(transaction_title).click()

driver.implicitly_wait(5)
select_title = '/html/body/div[2]/div[28]/div/div/div[2]/div/div/div[1]'
driver.find_element_by_xpath(select_title).click()

driver.implicitly_wait(5)

transaction_phone = '/html/body/div[2]/div[3]/div/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/input'
driver.find_element_by_xpath(transaction_phone).send_keys(transaction['phone'])

transaction_email = '/html/body/div[2]/div[3]/div/div/div[2]/div[2]/div[4]/div[1]/input'
driver.find_element_by_xpath(transaction_email).send_keys(transaction['email'])

transaction_save_button = '/html/body/div[2]/div[3]/div/div/div[2]/div[3]/button'
driver.find_element_by_xpath(transaction_save_button).click()

passenger_details = '/html/body/div[1]/div/div[2]/div/form/div[2]/div/div[2]/div/div[1]/div/div/div/label'
driver.find_element_by_xpath(passenger_details).click()

driver.implicitly_wait(5)
passenger_details_save_button = '/html/body/div[2]/div[4]/div/div/div[2]/div/div/div[2]/button' 
driver.find_element_by_xpath(passenger_details_save_button).click()

# Payment page
payment_button = '/html/body/div[1]/div/div[2]/div/div[7]/div/button'
driver.find_element_by_xpath(payment_button).click()

payment_button_confirmation = '/html/body/div[2]/div[12]/div/div/div/div/div[3]/button[1]'
driver.find_element_by_xpath(payment_button_confirmation).click()
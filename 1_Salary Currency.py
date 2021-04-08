#---------------------------------------------------Salary Conversion---------------------------------------------------#
# Author    : Aldi Sugiarto
# Date      : April,7th 2021
# Version   : 1.0
# Email     : aldisugiarto@gmail.com
#-----------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------Import Module---------------------------------------------------#
# Import library
import json         # +json library
import requests     # +http request
import pandas as pd # +pandas library

from datetime import datetime
#-----------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------Variable declaration---------------------------------------------------#
# Define of api key to access standard currency
api_key = '0d6a86d11f0531eb9aab'
url = "http://jsonplaceholder.typicode.com/users"
path = "JSON Files/salary_data.json"
# Assign variable as a list
user_id=[]
name=[]
user_name=[]
email=[]
addr=[]
phone=[]
idr=[]
usd=[]
#-----------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------Class or Function---------------------------------------------------#
# -------------------Make converter function------------------- #
def convert_currency(amount,fromCurrency,toCurrency):
    url = 'https://free.currconv.com/api/v7/convert?q='+fromCurrency+'_'+toCurrency+'&compact=ultra&apiKey='+api_key
    response = requests.get(url)
    value = response.json()
    result = value[fromCurrency +'_'+toCurrency] * amount
    return result

#---------------------------------------------------Algorithm---------------------------------------------------#
response = requests.get(url)    # Get request from url
f = open(path)  # Open file specified
# Assign value for data user and salary
data_user = response.json()
data_salary = json.load(f)
# Change data_salary as a list
data_salary = data_salary['array']
# Iteration for list of dictionary
for user in data_user:
    for salary in data_salary:
        if user['id'] == salary['id']:
            user.update(salary) # Update new dict user
            #Call and assign return value from function convert_currency
            salaryInUSD = {'salaryInUSD':convert_currency(user['salaryInIDR'],'IDR','USD')}
            user.update(salaryInUSD) # Update dict in user
            # Add new list in list variable
            user_id.append(user['id'])
            name.append(user['name'])
            user_name.append(user['username'])
            email.append(user['email'])
            addr.append(user['address']['street']+' '+user['address']['suite'])
            phone.append(user['phone'])
            idr.append(user['salaryInIDR'])
            usd.append(user['salaryInUSD'])

# Add to new dict variable of user
newUser = {
    'id':user_id,
    'name':name,
    'username':user_name,
    'email':email,
    'address':addr,
    'phone':phone,
    'Salary In IDR':idr,
    'Salary in USD':usd
}
# Convert list of dict to dataframe
df = pd.DataFrame(newUser)
df.set_index('id',inplace=True)
# Print value of df
print(df)
#---------------------------------------------------------Thank You--------------------------------------------------------------#
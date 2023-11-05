# program to test calling prdict function provided by flask 

import requests

# url of flask application and where post request should go
# url = 'http://localhost:9696/predict'

host = 'car-prices-env.eba-6vtp3yrg.ap-southeast-2.elasticbeanstalk.com'
url = f'http://{host}/predict'

# test data
car = {"mileage_miles" : 120000,
"registration_year" : 2011, 
"previous_owners" : 0, 
"fuel_type" : "diesel", 
"body_type" : "saloon", 
"engine" : "2.0l", 
"gearbox" : "manual", 
"doors" : 4, 
"seats" : 5, 
"emission_class" : "euro_5", 
"service_history" : "unk"}

# post test data to url above and store response 
response = requests.post(url, json=car).json()

# extract the price of the car for the given test data
print('Price of car:', response['car_price'])
import requests as r
endpoint = 'http://127.0.0.1:8000/register'

data = {
    "first_name": "John",
    "middle_name": "Tolulope",
    "last_name": "Afariogun",
    "email": "afariogun.john2002@gmail.com",
    "state_of_Residence": "Edo",
    "faculty": "school of engineering",
    "department": "Business Law",
    "level": "3",
    "date_of_birth": "2002-02-25",
    "phone_number": "08162127365"

    }
get_response = r.post(endpoint, json=data)
print(get_response.json())


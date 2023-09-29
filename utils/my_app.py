import requests

url = 'http://localhost:5000/estimate_carbon_credits'
data = {
    'waste_type': 'plastic',
    'quantity': 1000  # Example quantity
}

response = requests.post(url, json=data)
result = response.json()
print(f'Estimated carbon credits: {result["carbon_credits"]}')

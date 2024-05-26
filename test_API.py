import requests
import json


data={
  "transaction_id": 7,
  "user_id": 574,
  "género": "M",
  "linea_tc": 9700,
  "interes_tc": 54,
  "monto": 500,
  "fecha": "02/01/20",
  "hora": 7,
  "dispositivo": "{'año': 2019, 'marca': 'Apple', 'proveedor': 'Telcel'}",
  "establecimiento": "Farmacia",
  "ciudad": "Ciudad de México",
  "status_txn": "Aceptada",
  "is_prime": True,
  "dcto": 0,
  "cashback": 0
}

url = 'http://127.0.0.1:8000/predict'

resp = requests.post(url, json=data)

print(resp.content)


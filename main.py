from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
import json
import xgboost as xgb
import pandas as pd
import ast
from datetime import datetime

class PredictionInput(BaseModel):
  transaction_id: int
  user_id: int
  género: str
  linea_tc: int
  interes_tc: int
  monto: int
  fecha: str
  hora: int
  dispositivo: str
  establecimiento: str
  ciudad: str
  status_txn: str
  is_prime: bool
  dcto: int
  cashback: int


class PredictionOutput(BaseModel):
    prediction: float 

app = FastAPI()

def preprocessing(data):
  
    print("Starting...")
    data_copy = data.copy()
    print(type(data))
    print(data.keys())
    
    if not isinstance(data_copy, pd.DataFrame):
        data_copy = pd.DataFrame(data, index=[0], columns=data.keys())
    
    print(type(data_copy))
    print('reading dispositivo')
    print(data_copy.values)
    print(data_copy['dispositivo'])

    
    dispositivo_df = pd.json_normalize(data_copy['dispositivo'].apply(ast.literal_eval))

    print('Dispositivo read')
    
    data_copy = pd.concat([data_copy, dispositivo_df], axis=1)
    data_copy['fecha'] = pd.to_datetime(data_copy['fecha'])
    data_copy['day_of_week'] = data_copy['fecha'].dt.day_name()
    data_copy['day_of_month'] = data_copy['fecha'].dt.day
    data_copy['porcentaje_cashback'] = data_copy['cashback'] / data_copy['monto']
    data_copy['antiguedad_celular']= datetime.now().year - data_copy['año']
   
    object_columns = data_copy.select_dtypes(include=['object']).columns
    data_copy[object_columns] = data_copy[object_columns].astype('category')

    data_copy.drop(['fecha', 'dispositivo', 'cashback', 'transaction_id','año'], axis=1, inplace=True)

    for col in data_copy.columns:
        if data_copy[col].dtype not in [float, 'category']:
            data_copy[col] = data_copy[col].astype(float)
    
    return xgb.DMatrix(data_copy, enable_categorical=True)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
   print(input_data)
   
   try:
       prepi = preprocessing(input_data.model_dump())
   except Exception as e:
       print("Error!")
       print(e)
  
   pred = model.predict(prepi)
   return PredictionOutput(prediction = pred)
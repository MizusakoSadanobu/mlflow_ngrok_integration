from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import mlflow
import os

os.environ["MLFLOW_TRACKING_USERNAME"] = "admin" #use your user name
os.environ["MLFLOW_TRACKING_PASSWORD"] = "password" #use your pass

# initialize mlflow
client = mlflow.MlflowClient()
tracking_uri = "https://close-grizzly-eternal.ngrok-free.app"
mlflow.set_tracking_uri(uri=tracking_uri)

model_name = "tracking-quickstart"
version = 1
model_uri = f'models:/{model_name}/{version}'

# load model
model = mlflow.sklearn.load_model(model_uri)

# FastAPI アプリケーションの作成
app = FastAPI()

# 入力データのバリデーション
class InputData(BaseModel):
    features: list[float]

@app.post("/predict/")
def predict(data: InputData):
    X_input = np.array(data.features).reshape(1, -1)
    if X_input.shape[1] != 4:
        raise HTTPException(status_code=400, detail="Input must have exactly 2 features")
    
    prediction = model.predict(X_input)
    return {"prediction": int(prediction[0])}
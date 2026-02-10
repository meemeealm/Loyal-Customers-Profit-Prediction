import pickle
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

class Item(BaseModel):
    customer_name: str = Field(..., alias="Customer Name")
    sub_category: str = Field(..., alias="Sub Category")
    city: str = Field(..., alias="City")
    sales: int = Field(..., alias="Sales")
    discount: int = Field(..., alias="Discount")

app = FastAPI(title="Profit Prediction")

with open('model.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

@app.post("/predict")
def predict(item:Item):
    new_sales = item.dict(by_alias=True)
    prediction = pipeline.predict([new_sales])
    return {"predicted_profit":float(prediction[0])}


if __name__== "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

new_sales = {
  "Customer Name": "Harish",
  "Sub Category": "Health Drinks",
  "City": "Vellore",
  "Discount": 4,
  "Sales": 10
}
# categorical = ["Customer Name","Sub Category","City"]
# numerical = ["Sales","Discount"]



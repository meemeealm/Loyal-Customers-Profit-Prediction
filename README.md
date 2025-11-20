## Grocery Store Loyal Customers' Profit Prediction
<img src="https://geediting.com/wp-content/uploads/2025/08/a6235bf0-ec43-47e2-afd6-9187c23ab30b.png" alt="Demo Image" width="400" height="300"/>

***Project Overview***  

This project uses machine learning models to predict the profit of loyal customer' transaction. The dataset is the grocery store sales based on historical transaction data. The goal is to build a predictive model that helps retailers forecast profits and communicate with loyal customers.

***Problem Description***  

This project focuses on predicting profit margins for loyal grocery store customers. The model uses customer purchase data (such as sales, discounts, and product categories) to estimate the expected profit from each transaction.

***Why this problem matters***  

While loyalty programs encourage repeat purchases, excessive discounts can erode profits. By predicting profit margins for loyal customers, grocery stores can strike the right balance between rewarding loyalty and maintaining healthy financial performance. This ensures sustainable growth and smarter business strategies.

***what we are predicting***  
- Target: Profit generated from loyal customers’ purchases.  
- Inputs: Customer details, product sub‑categories, city, sales amount, and discounts.  
- Output: Predicted profit value.

***Evaluation Metrics***  

To assess model performance, two regression algorithms were implemented:1) Linear Regression, 2) Random Forest Regressor.  

The following metrics were used for evaluation:  
**Root Mean Squared Error (RMSE)**: Measures the average magnitude of prediction errors, penalizing larger deviations more heavily.  
**R² Score (Coefficient of Determination)**: Indicates how well the model explains the variance in the target variable, with values closer to 1 representing better fit.  

These metrics provided a balanced view of both prediction accuracy (RMSE) and explained variance (R²), helping us determine which model generalizes better for profit prediction tasks.

***Who Benefits***  
- Grocery retailers → Gain insights into which loyal customers drive profitability.  
- Marketing and Sales teams → Optimize promotions and discounts without hurting margins.  
- Managers → Forecast revenue more accurately and plan inventory better.  

***Objectives***  
- Develop a machine learning model to predict profit margins for loyal grocery store customers.  
- Provide profit predictions to support smarter business decisions.  
- Demonstrate the integration of ML models into deployable applications using Docker.  

## Project Description  

Dataset Source: [Kaggle](https://www.kaggle.com/datasets/mohamedharris/supermart-grocery-sales-retail-analytics-dataset)

***Workflow***  

![](https://github.com/meemeealm/zoomcamp_projects/blob/main/workflow.png)

***Structure***  
```
.
├── README.md
├── Supermart Grocery Sales - Retail Analytics Dataset.csv
├── __pycache__
│   └── predict.cpython-312.pyc
├── dockerfile
├── main.py
├── model.bin
├── notebook.ipynb
├── predict.py
├── preprocessing_EDA.ipynb
├── pyproject.toml
├── sales.py
├── train.py
└── uv.lock
```

### Web Service 

example request: 
```
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Customer Name": "string",
  "Sub Category": "string",
  "City": "string",
  "Sales": 0,
  "Discount": 0
}'
```
*How to run via locally and Docker*

```
git clone https://github.com/meemeealm/Loyal-Customers-Profit-Prediction.git
cd zoomcamp-projects
```

```
docker build -t profit-prediction .
docker run -p 8000:8000 profit-prediction
```

*access the application via Fastapi*
```
http://localhost:8000/docs
```





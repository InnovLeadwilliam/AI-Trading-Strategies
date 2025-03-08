# 📊 AI-Trading-Strategies
📌 **Portafolio de estrategias de trading cuantitativo y algorítmico usando IA, Machine Learning y backtesting en Python.**

## 🚀 Contenido:
- **📂 01_Trading_Cuantitativo/** → Modelos de trading con ML.
- **📂 datasets/** → Datos históricos para entrenar modelos.
- **📂 scripts/** → Algoritmos de backtesting en Python.

## 🛠 Instalación:
Ejecuta el siguiente comando para instalar las librerías necesarias:
```bash
pip install pandas numpy scikit-learn backtrader prophet matplotlib seabornfrom prophet import Prophet
import pandas as pd

df = pd.read_csv("datasets/AAPL_5Y.csv")
df['ds'] = pd.to_datetime(df['Date'])
df['y'] = df['Close']

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)

model.plot(forecast)

# 📈 Stock Market Prediction Project

This repository demonstrates a Python-based approach to **stock market prediction** using:
- Yahoo Finance for historical stock data (price, P/E, revenue growth)
- World Bank API for GDP growth
- VIX for market volatility

## 🚀 Features
- Extract 10 years of stock price history
- Identify max/min one-day changes
- Retrieve macroeconomic indicators (GDP, VIX, revenue growth, P/E)
- Generate prediction score based on weighted factors
- Visualize comparisons with doughnut charts

## 📂 Project Structure
```
.
├── src/
│   └── stock_predictor.py
├── docs/
│   └── PROJECT_DOCUMENTATION.md
├── images/   # add screenshots of charts here
├── notebooks/  # optional Jupyter notebooks
└── README.md
```

## ⚙️ Setup
Install dependencies:
```bash
pip install yfinance requests pandas numpy matplotlib
```

Run the predictor:
```bash
python src/stock_predictor.py
```

## 📊 Example Output
```
Prediction Analysis for TSLA:
- Max One-Day Change: 21.92% on 2024-10-24
- Min One-Day Change: -21.06% on 2020-09-08
- Predicted Change for Tomorrow: 13.29%
```

## 📝 License
MIT © 2025

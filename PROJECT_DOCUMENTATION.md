# Stock Market Prediction Project

## Overview
This project predicts short-term stock price changes by combining historical data from Yahoo Finance and macroeconomic indicators such as GDP growth (World Bank API) and VIX.

## Steps
1. **Data Collection**
   - Yahoo Finance for stock history, PE ratio, revenue growth, and VIX.
   - World Bank API for GDP growth.

2. **Feature Engineering**
   - Calculated max/min one-day changes in the past 10 years.
   - Extracted PE ratio, revenue growth, GDP, and VIX values.

3. **Prediction Logic**
   - Compared historical maximum change factors against current values.
   - Weighted GDP, VIX, revenue growth, and PE equally to form a prediction score.

4. **Visualization**
   - Doughnut charts comparing current values with historical maximums.
   - Console output showing predicted change.

## Requirements
- Python 3.8+
- Libraries: `yfinance`, `requests`, `pandas`, `numpy`, `matplotlib`

Install with:
```bash
pip install yfinance requests pandas numpy matplotlib
```

## Run
```bash
python src/stock_predictor.py
```

## Example Output
```
Prediction Analysis for TSLA:
- Max One-Day Change: 21.92% on 2024-10-24
- Min One-Day Change: -21.06% on 2020-09-08
- Predicted Change for Tomorrow: 13.29%
```


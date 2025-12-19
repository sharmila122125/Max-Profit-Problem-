# 🏗️ Max Profit Visual Gallery

A Streamlit-based optimization application that computes the **optimal mix of buildings** (Theatre, Pub, Commercial Park) to **maximize total earnings** under a fixed time constraint.

---

## 📌 Problem Overview

Mr. X owns infinite land but has a limited number of **time units (n)**.  
He can construct **only one building at a time**.  
Each building starts generating revenue **after construction is completed**.

The objective is to determine the **best construction plan** that maximizes total profit.

---

## 🏢 Building Options

| Building | Build Time | Earnings per Unit Time |
|--------|-----------|------------------------|
| Theatre (T) | 5 units | $1500 |
| Pub (P) | 4 units | $1000 |
| Commercial Park (C) | 10 units | $2000 |

---

## 🧠 Solution Approach

- Modeled as a **Dynamic Programming optimization problem**
- Each DP state represents the **maximum profit achievable** at a given construction time
- Profit is calculated based on **remaining operational time**
- A deterministic **tie-breaking rule** is applied:
  
  **Theatre > Pub > Commercial**

### Profit Formula
Profit = (Total Time − Completion Time) × Revenue Rate

---

## ✨ Features

- Dynamic Programming–based optimization engine
- Deterministic tie-breaking logic
- Modular Python backend
- Professional Streamlit UI (Dark + Gold theme)
- Real-time visualization of optimal results

---

## 📂 Project Structure

├── max_profit.py # Core optimization logic
├── streamlit_max_profit.py # Streamlit UI
├── requirements.txt
└── README.md

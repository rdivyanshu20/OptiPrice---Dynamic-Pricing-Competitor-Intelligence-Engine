# OptiPrice: Dynamic Pricing & Competitor Intelligence Engine

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)

##  Overview
OptiPrice is a machine-learning-powered pricing engine designed to help e-commerce businesses maximize profit margins and remain competitive. By analyzing real-time competitor pricing, historical sales velocity, and current inventory levels, the engine automatically recommends the optimal price for any given SKU.

##  Business Value
* **Revenue Maximization:** Automatically increases prices during high demand and low competitor stock.
* **Competitive Edge:** Detects competitor price drops and suggests targeted discounts to retain market share without triggering a race to the bottom.
* **Inventory Optimization:** Lowers prices on stagnant inventory to free up warehouse space and capital.

##  Key Features
* **Competitor Tracking Pipeline:** Automated scraping of competitor URLs to track daily price changes.
* **Elasticity Modeling:** Uses historical sales data to calculate price elasticity for different product categories.
* **Recommendation Engine:** Generates a daily `.csv` report of recommended price changes based on a customizable rules engine (e.g., "Never price below 15% margin").
* **Interactive Dashboard:** A Streamlit interface for business stakeholders to review and approve price changes before they are pushed to the live storefront.

##  Tech Stack
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Random Forest Regressor for demand forecasting)
* **Web Scraping:** BeautifulSoup, Selenium (for dynamic competitor sites)
* **Frontend/Dashboard:** Streamlit

##  Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/optiprice-engine.git](https://github.com/yourusername/optiprice-engine.git)
   cd optiprice-engine

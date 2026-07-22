import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class ElasticityModel:
    def __init__(self):
        # Using 100 trees for a balance of speed and accuracy
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.is_trained = False

    def generate_synthetic_data(self):
        """Generates dummy historical data so the MVP is runnable immediately."""
        np.random.seed(42)
        n = 1000
        data = {
            'sku': np.random.choice(['SKU_A', 'SKU_B', 'SKU_C'], n),
            'price': np.random.uniform(10, 100, n),
            'competitor_price': np.random.uniform(10, 100, n),
            'inventory_level': np.random.randint(0, 500, n),
            'seasonality_index': np.random.uniform(0.8, 1.2, n)
        }
        df = pd.DataFrame(data)
        
        # Synthetic Demand Curve: Sales drop as our price rises, but rise if competitor price rises.
        df['sales_velocity'] = (
            50 - (df['price'] * 0.5) 
            + (df['competitor_price'] * 0.3) 
            + (df['inventory_level'] * 0.05)
        ) * df['seasonality_index'] + np.random.normal(0, 5, n)
        
        df['sales_velocity'] = df['sales_velocity'].clip(lower=0)
        return df

    def train(self, df):
        features = ['price', 'competitor_price', 'inventory_level', 'seasonality_index']
        X = df[features]
        y = df['sales_velocity']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        self.is_trained = True
        
        # Return R^2 score to validate accuracy
        return self.model.score(X_test, y_test)

    def predict_demand(self, X):
        if not self.is_trained:
            raise ValueError("Model must be trained before predicting.")
        return self.model.predict(X)
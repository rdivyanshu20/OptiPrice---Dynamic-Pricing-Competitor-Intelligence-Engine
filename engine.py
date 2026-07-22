import pandas as pd
import numpy as np
from model import ElasticityModel

class PricingEngine:
    def __init__(self, min_margin=0.15):
        self.min_margin = min_margin
        self.model = ElasticityModel()
        
    def train_model(self, data):
        return self.model.train(data)
        
    def generate_recommendations(self, current_inventory, cost_data, competitor_data):
        recommendations = []
        
        # Merge all data sources
        df = pd.merge(current_inventory, cost_data, on='sku')
        df = pd.merge(df, competitor_data, on='sku')
        
        for _, row in df.iterrows():
            # Apply the hard business rule: Never price below X% margin
            min_price = row['cost'] / (1 - self.min_margin)
            
            # Simulate 20 possible price points between the floor and a high ceiling
            test_prices = np.linspace(min_price, min_price * 2.5, 20)
            
            best_profit = -float('inf')
            best_price = row['current_price']
            predicted_sales = 0
            
            for price in test_prices:
                features = pd.DataFrame([{
                    'price': price,
                    'competitor_price': row['competitor_price'],
                    'inventory_level': row['inventory_level'],
                    'seasonality_index': row['seasonality_index']
                }])
                
                sales = self.model.predict_demand(features)[0]
                profit = (price - row['cost']) * sales
                
                if profit > best_profit:
                    best_profit = profit
                    best_price = price
                    predicted_sales = sales
            
            recommendations.append({
                'sku': row['sku'],
                'cost': round(row['cost'], 2),
                'current_price': round(row['current_price'], 2),
                'competitor_price': round(row['competitor_price'], 2),
                'recommended_price': round(best_price, 2),
                'predicted_demand': round(predicted_sales, 0),
                'projected_profit': round(best_profit, 2),
                'margin_pct': round((best_price - row['cost']) / best_price * 100, 2)
            })
            
        rec_df = pd.DataFrame(recommendations)
        rec_df.to_csv('recommended_prices.csv', index=False)
        return rec_df
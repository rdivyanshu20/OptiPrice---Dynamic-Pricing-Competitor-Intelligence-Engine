import pandas as pd
from model import ElasticityModel
from engine import PricingEngine

def run_pipeline():
    print("Initializing OptiPrice Engine...")
    engine = PricingEngine(min_margin=0.15)
    
    print("Training Demand Model with historical data...")
    historical_data = engine.model.generate_synthetic_data()
    r2_score = engine.train_model(historical_data)
    print(f"Model trained! R² Score: {r2_score:.2f}")
    
    print("Gathering Current State (Inventory, Costs, Competitors)...")
    # In production, you would fetch this via API or the scraper.py module
    current_inventory = pd.DataFrame({
        'sku': ['SKU_A', 'SKU_B', 'SKU_C'],
        'inventory_level': [450, 20, 150], # A is overstocked, B is scarce
        'current_price': [49.99, 89.99, 29.99],
        'seasonality_index': [1.0, 1.2, 0.9]
    })
    
    cost_data = pd.DataFrame({
        'sku': ['SKU_A', 'SKU_B', 'SKU_C'],
        'cost': [25.00, 45.00, 15.00]
    })
    
    competitor_data = pd.DataFrame({
        'sku': ['SKU_A', 'SKU_B', 'SKU_C'],
        'competitor_price': [45.00, 95.00, 28.00] 
    })
    
    print("Generating Optimization Recommendations...")
    engine.generate_recommendations(current_inventory, cost_data, competitor_data)
    print("Pipeline Complete! Run 'streamlit run app.py' to view the dashboard.")

if __name__ == "__main__":
    run_pipeline()
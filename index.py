from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np

app = FastAPI()

class PricingData(BaseModel):
    competitor_price: float
    inventory_level: int
    sales_velocity: float

@app.post("/api/optimize")
def optimize_price(data: PricingData):
    # Placeholder for your Random Forest demand forecasting model.
    # Below is your basic business rules-engine enforcing profit margins.
    
    base_price = data.competitor_price * 0.95 
    elasticity_modifier = (data.sales_velocity / 100)
    inventory_penalty = 1.0 if data.inventory_level > 50 else 1.1
    
    optimized_price = base_price * elasticity_modifier * inventory_penalty
    
    # Margin guardrail: absolute minimum price allowed
    final_price = max(optimized_price, data.competitor_price * 0.80) 
    
    return {
        "recommended_price": round(final_price, 2),
        "margin_protected": True
    }
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="OptiPrice Dashboard", layout="wide")
st.title("OptiPrice: Intelligence & Approval")
st.markdown("Review and approve daily algorithmic pricing recommendations.")

DATA_FILE = "recommended_prices.csv"

if not os.path.exists(DATA_FILE):
    st.warning("No recommendations found. Please run main.py first.")
    st.stop()

df = pd.read_csv(DATA_FILE)

# KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Total SKUs Analyzed", len(df))
col2.metric("Average Projected Margin", f"{df['margin_pct'].mean():.1f}%")
col3.metric("Projected Daily Profit", f"${df['projected_profit'].sum():,.2f}")

st.divider()

# Interactive Data Editor
st.subheader("Price Approvals")
if 'approve' not in df.columns:
    df.insert(0, 'approve', True)

edited_df = st.data_editor(
    df,
    hide_index=True,
    column_config={
        "approve": st.column_config.CheckboxColumn("Approve?", default=True),
        "current_price": st.column_config.NumberColumn("Current Price", format="$%.2f"),
        "competitor_price": st.column_config.NumberColumn("Comp. Price", format="$%.2f"),
        "recommended_price": st.column_config.NumberColumn("Suggested Price", format="$%.2f"),
        "margin_pct": st.column_config.NumberColumn("Margin", format="%.1f%%")
    },
    disabled=["sku", "cost", "current_price", "competitor_price", "predicted_demand", "projected_profit", "margin_pct"]
)

if st.button("Push Approved Prices to Storefront"):
    approved_skus = edited_df[edited_df['approve'] == True]
    if len(approved_skus) > 0:
        approved_skus.to_csv("approved_prices_export.csv", index=False)
        st.success(f"Successfully exported {len(approved_skus)} price changes to your E-commerce API!")
        st.balloons()
    else:
        st.warning("No prices approved for export.")
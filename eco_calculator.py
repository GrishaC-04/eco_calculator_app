# eco_calculator_app.py
import streamlit as st

st.title(" Eco Calculator")

st.markdown("### Diet-related Emissions")
meat_consumption = st.number_input("Enter your meat consumption (kg/week):", min_value=0.0)
dairy_consumption = st.number_input("Enter your dairy consumption (litres/week):", min_value=0.0)

st.markdown("### Travel-related Emissions")
car_distance = st.number_input("Distance travelled by car per week (km):", min_value=0.0)
flight_hours = st.number_input("Number of flight hours per year:", min_value=0.0)

if st.button("Calculate Impact"):
    # Replace these with your actual calculations
    diet_impact = meat_consumption * 27 + dairy_consumption * 3
    travel_impact = car_distance * 0.2 + flight_hours * 90
    total_impact = diet_impact + travel_impact

    st.success(f"🌍 Your estimated CO₂ impact is {total_impact:.2f} kg/week")


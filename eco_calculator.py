import streamlit as st

st.set_page_config(page_title="Eco Calculator", layout="centered")

st.title("Eco Calculator")
st.write("Estimate your weekly carbon emissions and get personalized tips to reduce your impact.")

# Input section
st.header("Enter Your Lifestyle Details")

diet_type = st.selectbox("Select your diet type:", 
    ["Vegan", "Vegetarian", "Omnivore", "Heavy Meat Eater"])

car_km_per_week = st.number_input("Kilometers you travel by car per week:", min_value=0.0, step=1.0)

electricity_kwh_per_week = st.number_input("Electricity usage per week (in kWh):", min_value=0.0, step=1.0)

flight_hours_per_month = st.number_input("Flight hours per month (approximate):", min_value=0.0, step=1.0)

# Emission factors (kg CO₂e per unit)
EMISSION_FACTORS = {
    "Vegan": 30,
    "Vegetarian": 40,
    "Omnivore": 60,
    "Heavy Meat Eater": 90,
    "Car per km": 0.21,
    "Electricity per kWh": 0.5,
    "Flight per hour": 90
}

# Diet-specific tips
DIET_TIPS = {
    "Vegan": "Your diet is already very eco-friendly. Keep exploring plant-based recipes to stay on track.",
    "Vegetarian": "You're making a positive impact. Reducing dairy and eggs further could help even more.",
    "Omnivore": "Consider reducing red meat and incorporating more plant-based meals into your week.",
    "Heavy Meat Eater": "Meat-heavy diets have a high carbon footprint. Try limiting meat to a few meals a week."
}

# Emission calculation
def calculate_emissions(diet, car_km, electricity_kwh, flight_hours):
    diet_emission = EMISSION_FACTORS[diet]
    car_emission = car_km * EMISSION_FACTORS["Car per km"]
    electricity_emission = electricity_kwh * EMISSION_FACTORS["Electricity per kWh"]
    flight_emission = (flight_hours / 4.0) * EMISSION_FACTORS["Flight per hour"]  # Weekly average
    return diet_emission + car_emission + electricity_emission + flight_emission

# Total eco tip based on emissions
def get_total_tip(total):
    if total <= 100:
        return "Your overall carbon footprint is low. Excellent progress toward a sustainable lifestyle."
    elif total <= 300:
        return "Your footprint is moderate. Small changes like reducing travel and saving energy can make a big difference."
    else:
        return "Your carbon footprint is high. Consider revisiting your travel habits, electricity use, and diet choices."

# Submit button
if st.button("Calculate My Emissions"):
    total_emissions = calculate_emissions(diet_type, car_km_per_week, electricity_kwh_per_week, flight_hours_per_month)
    st.subheader("Results")
    st.write(f"Your estimated weekly carbon footprint is **{total_emissions:.2f} kg CO₂e**.")
    
    st.subheader("Eco Advice")
    st.write(f"**Diet Tip:** {DIET_TIPS[diet_type]}")
    st.write(f"**General Tip:** {get_total_tip(total_emissions)}")

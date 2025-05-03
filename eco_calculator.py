import streamlit as st

st.set_page_config(page_title="Eco Calculator", layout="centered")

st.title(" Welcome to the Eco Calculator")

st.write("Estimate your weekly carbon emissions and get personalized eco tips!")

# User input section
st.header("Lifestyle Details")

diet_type = st.selectbox(" What best describes your diet?", 
    ["Vegan", "Vegetarian", "Omnivore", "Heavy Meat Eater"])

car_km_per_week = st.number_input(" How many kilometers do you travel by car per week?", min_value=0.0, step=1.0)

electricity_kwh_per_week = st.number_input(" How much electricity do you use per week (in kWh)?", min_value=0.0, step=1.0)

flight_hours_per_month = st.number_input(" Approximate hours you spend flying per **month**?", min_value=0.0, step=1.0)

# Emission factors (rough estimates in kg CO₂e per unit)
EMISSION_FACTORS = {
    "Vegan": 30,
    "Vegetarian": 40,
    "Omnivore": 60,
    "Heavy Meat Eater": 90,
    "Car per km": 0.21,
    "Electricity per kWh": 0.5,
    "Flight per hour": 90
}

# Calculate emissions
def calculate_emissions(diet, car_km, electricity_kwh, flight_hours):
    diet_emission = EMISSION_FACTORS[diet]
    car_emission = car_km * EMISSION_FACTORS["Car per km"]
    electricity_emission = electricity_kwh * EMISSION_FACTORS["Electricity per kWh"]
    flight_emission = (flight_hours / 4.0) * EMISSION_FACTORS["Flight per hour"]  # Weekly average
    return diet_emission + car_emission + electricity_emission + flight_emission

# Eco tips based on total emissions
def get_eco_tip(total):
    if total <= 100:
        return " Great job! You're living sustainably. Keep it up!"
    elif total <= 300:
        return " You're doing okay. Try reducing car travel and electricity use."
    else:
        return " Your carbon footprint is high. Consider switching to a plant-based diet, flying less, and using energy-efficient appliances."

# Submit button
if st.button("Calculate My Emissions"):
    total_emissions = calculate_emissions(diet_type, car_km_per_week, electricity_kwh_per_week, flight_hours_per_month)
    tip = get_eco_tip(total_emissions)

    st.success(f"Your estimated weekly carbon footprint is **{total_emissions:.2f} kg CO₂e**.")
    st.markdown(f"**Eco Tip:** {tip}")

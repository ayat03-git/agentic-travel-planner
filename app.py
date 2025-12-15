import streamlit as st
from agent import run_travel_agent, critic_validate_itinerary

st.set_page_config(page_title="Agentic Travel Planner", page_icon="✈️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #1E90FF;'>✈️ Agentic Travel Planner (MCP)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Plan your perfect trip in seconds!</p>", unsafe_allow_html=True)
st.write("---")

col1, col2, col3 = st.columns([2,1,1])

with col1:
    destination = st.text_input("📍 Destination", placeholder="e.g. Paris")
with col2:
    days = st.number_input("🗓️ Number of days", min_value=1, max_value=30, value=5)
with col3:
    budget_max = st.number_input("💰 Max Budget (USD)", min_value=50, max_value=5000, value=1000)

if st.button("Generate Travel Plan 🧳"):
    if destination:
        with st.spinner("Planning your trip..."):

            def run_agent_with_budget(destination, days, budget_max):
                output = run_travel_agent(destination, days)
                
                try:
                    total_budget = int(output.split("Total budget: ")[1].split(" USD")[0])
                except:
                    total_budget = 0  
                
                if total_budget > budget_max and days > 1:
                    days_adjusted = max(1, days - 1)
                    st.warning(f"⚠️ Total budget ({total_budget} USD) exceeds max budget ({budget_max} USD). Adjusting plan to {days_adjusted} days.")
                    return run_agent_with_budget(destination, days_adjusted, budget_max)
                
                return output

            output = run_agent_with_budget(destination, days, budget_max)

            st.success("Travel plan generated! ✅")
            
            with st.container():
                st.markdown("<h3 style='color:#FF6347;'>Your Travel Itinerary & Budget</h3>", unsafe_allow_html=True)
                st.markdown(f"<div style='background-color:#F0F8FF; padding:15px; border-radius:10px;'>{output}</div>", unsafe_allow_html=True)
            
            # ---- Critic Agent ----
            with st.expander("📝 Critic Review"):
                critique = critic_validate_itinerary(output)
                st.text(critique)

    else:
        st.warning("⚠️ Please enter a destination.")

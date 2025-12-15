import requests
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

def estimate_budget(destination: str, days: int, show_in_gui=False) -> str:
    response = requests.post(
        "http://localhost:3333/tools/estimate_budget",
        json={"destination": destination, "days": days}
    )
    data = response.json()["result"]

    budget_text = (
        f"Destination: {data['destination']}\n"
        f"Days: {data['days']}\n"
        f"Daily cost: {data['daily_cost']} USD\n"
        f"Total budget: {data['total_usd']} USD"
    )

    if show_in_gui:
        import streamlit as st
        st.info(f"💻 **Tool call**\nRequest: destination={destination}, days={days}\nResponse:\n{budget_text}")

    return budget_text


llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)

def run_travel_agent(destination: str, days: int) -> str:
    prompt = f"Plan a {days}-day trip to {destination}."

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    budget_info = estimate_budget(destination, days, show_in_gui=True)
    total_budget = int(budget_info.split("Total budget: ")[1].split(" USD")[0])


    return f"{response.content}\n\nBudget Details:\n{budget_info}"

def critic_validate_itinerary(itinerary: str) -> str:
    """
    Analyse l'itinéraire généré par le LLM et signale les incohérences ou erreurs.
    """
    prompt = f"Check this travel itinerary and highlight any mistakes or inconsistencies:\n{itinerary}"

    response = llm.invoke([HumanMessage(content=prompt)])

    return response.content

if __name__ == "__main__":
    print(run_travel_agent("Paris", 5))

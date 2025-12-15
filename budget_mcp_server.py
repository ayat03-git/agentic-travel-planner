
"""
Serveur MCP pour l'estimation de budget
Port: 3333
"""
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Budget Calculator MCP")

class BudgetRequest(BaseModel):
    destination: str
    days: int

@app.post("/tools/estimate_budget")
def estimate_budget(request: BudgetRequest):
    """Estime le budget de voyage en USD"""
    base_costs = {
        "Barcelona": 120,
        "Paris": 150,
        "Tokyo": 130,
        "Rome": 110,
        "Madrid": 100,
        "London": 140
    }
    base_cost = base_costs.get(request.destination, 100)
    total = base_cost * request.days
    
    return {
        "tool": "estimate_budget",
        "result": {
            "total_usd": total,
            "daily_cost": base_cost,
            "destination": request.destination,
            "days": request.days
        }
    }

@app.get("/tools")
def list_tools():
    return {
        "tools": [
            {
                "name": "estimate_budget",
                "description": "Estime le coût total du voyage en USD",
                "parameters": {
                    "destination": "string",
                    "days": "integer"
                }
            }
        ]
    }

if __name__ == "__main__":
    print("🚀 Budget Calculator MCP Server - Port 3333")
    uvicorn.run(app, host="0.0.0.0", port=3333)

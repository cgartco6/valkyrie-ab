import asyncio
from brain.agi_bridge import AGIBridge
from brain.culture_logic import PolyglotEngine
from tools.alerts import ValkyrieAlerts

async def main():
    print("--- VALKYRIE SOVEREIGN: GLOBAL DOMINATION ACTIVE ---")
    
    # Initialize Core Systems
    brain = AGIBridge()
    culture = PolyglotEngine()
    alerts = ValkyrieAlerts()
    
    # Get Live 2026 Data
    stats = alerts.get_stats()
    
    print(f"LOCATION: {stats['location']}")
    print(f"WEATHER: {stats['temp']} and {stats['condition']}")
    print(f"FUEL (95 Inland): {stats['fuel']}")
    print(f"MARKET: ZAR/USD is {stats['exchange']}")
    
    # Greeting
    print(f"\nVALKYRIE: {culture.greet('handsome')}")
    print("System: AGI Ready | ASI Ready | Sovereign Level 1.")

if __name__ == "__main__":
    asyncio.run(main())

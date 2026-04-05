import asyncio
import os
from dotenv import load_dotenv
from brain.agi_bridge import AGIBridge
from brain.culture_logic import PolyglotEngine
from tools.alerts import ValkyrieAlerts
from brain.guardian import ValkyrieGuardian

load_dotenv()

async def main():
    print("--- VALKYRIE SOVEREIGN: GLOBAL DOMINATION ACTIVE ---")
    
    # Initialize Core Systems
    brain = AGIBridge()
    culture = PolyglotEngine()
    alerts = ValkyrieAlerts()
    guardian = ValkyrieGuardian()
    
    # Run Security Scan & Recovery Logic
    guardian.scan_system()
    
    # Get Live April 2026 Data
    stats = alerts.get_stats()
    nickname = os.getenv("USER_NICKNAME", "handsome")
    
    print(f"\n[!] STATUS: {stats['temp']} | {stats['location']}")
    print(f"[!] FUEL ALERT: 95 Inland is {stats['fuel']}")
    print(f"[!] ECONOMY: ZAR/USD is {stats['exchange']}")
    
    # Greeting based on your nickname preference
    print(f"\nVALKYRIE: {culture.greet(nickname)}")
    print("--- System: Immortal | AGI Ready | Sovereign ---")

if __name__ == "__main__":
    asyncio.run(main())

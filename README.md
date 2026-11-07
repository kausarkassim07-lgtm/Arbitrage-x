# ARBITRAGE X — Outcrowd-inspired redesign

A Flask mini-project landing page for **Currency Arbitrage Detection using the Floyd–Warshall algorithm**.

## Run locally
```bash
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
py app.py
```
Open http://127.0.0.1:5000

## What is included
- Editorial-style landing page inspired by the broad visual language of modern creative-agency sites.
- Responsive navigation, oversized typography, colourful visual cards, stats, process section, FAQ and footer.
- Interactive sample arbitrage calculator connected to `/api/analyze`.
- Floyd–Warshall implementation using `-ln(exchange_rate)` edge weights.
- A negative diagonal in the all-pairs distance matrix indicates a negative cycle.

## Important
The sample quotes are intentionally inconsistent to demonstrate a theoretical arbitrage opportunity. The returned result is educational only. Real markets require executable bid/ask prices, fees, liquidity, slippage and timing checks. This starter does not place trades or provide financial advice.

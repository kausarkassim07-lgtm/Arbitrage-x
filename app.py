from flask import Flask, render_template, jsonify, request
import math

app = Flask(__name__)

# Demo quotes are intentionally inconsistent so the demo can show an arbitrage cycle.
SAMPLE_QUOTES = [
    ("USD", "INR", 83.00), ("INR", "EUR", 0.011),
    ("EUR", "USD", 1.12), ("USD", "EUR", 0.92),
    ("EUR", "INR", 90.0), ("INR", "USD", 1/83.0)
]

def floyd_warshall(currencies, edges):
    n = len(currencies)
    index = {c: i for i, c in enumerate(currencies)}
    inf = float("inf")
    dist = [[inf] * n for _ in range(n)]
    nxt = [[None] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for a, b, rate in edges:
        if rate <= 0:
            continue
        i, j = index[a], index[b]
        weight = -math.log(rate)
        if weight < dist[i][j]:
            dist[i][j] = weight
            nxt[i][j] = j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]
    negative = [currencies[i] for i in range(n) if dist[i][i] < -1e-12]
    return dist, negative

def find_demo_cycle():
    # A clear, known cycle for the teaching/demo screen.
    cycle = ["USD", "INR", "EUR", "USD"]
    product = 83.0 * 0.011 * 1.12
    return cycle, product

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/analyze")
def analyze():
    payload = request.get_json(silent=True) or {}
    amount = float(payload.get("amount", 1000))
    mode = payload.get("mode", "sample")
    currencies = ["USD", "INR", "EUR"]
    edges = SAMPLE_QUOTES
    dist, negative = floyd_warshall(currencies, edges)
    cycle, multiplier = find_demo_cycle()
    profit = amount * (multiplier - 1)
    return jsonify({
        "mode": mode,
        "currencies": currencies,
        "has_arbitrage": bool(negative),
        "negative_cycle": negative,
        "cycle": cycle,
        "multiplier": multiplier,
        "initial_amount": amount,
        "final_amount": amount * multiplier,
        "profit": profit,
        "profit_percent": (multiplier - 1) * 100,
        "note": "Illustrative sample quotes only. Not an executable trading signal."
    })

if __name__ == "__main__":
    app.run(debug=True)

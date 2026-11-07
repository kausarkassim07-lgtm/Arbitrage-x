const amountInput = document.getElementById("amount");
const runBtn = document.getElementById("runBtn");
const finalAmount = document.getElementById("finalAmount");
const profitAmount = document.getElementById("profitAmount");
const cycleText = document.getElementById("cycleText");
const resultStatus = document.getElementById("resultStatus");
const note = document.getElementById("note");

runBtn.addEventListener("click", async () => {
  const amount = Number(amountInput.value);
  if (!Number.isFinite(amount) || amount <= 0) {
    note.textContent = "Enter an amount greater than zero.";
    amountInput.focus();
    return;
  }
  runBtn.disabled = true;
  runBtn.innerHTML = "Analysing route <span>…</span>";
  resultStatus.textContent = "RUNNING";
  try {
    const response = await fetch("/api/analyze", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({amount, mode: "sample"})
    });
    if (!response.ok) throw new Error("The analysis service returned an error.");
    const data = await response.json();
    finalAmount.textContent = new Intl.NumberFormat("en-US", {
      style: "currency", currency: "USD"
    }).format(data.final_amount);
    profitAmount.textContent = (data.profit >= 0 ? "+" : "") +
      new Intl.NumberFormat("en-US", {style: "currency", currency: "USD"}).format(data.profit);
    cycleText.textContent = data.cycle.join("  →  ");
    resultStatus.textContent = data.has_arbitrage ? "CYCLE FOUND" : "NO CYCLE";
    note.textContent = `${data.profit_percent.toFixed(2)}% theoretical return. ${data.note}`;
  } catch (error) {
    resultStatus.textContent = "ERROR";
    note.textContent = error.message;
  } finally {
    runBtn.disabled = false;
    runBtn.innerHTML = 'Detect arbitrage <span>↗</span>';
  }
});

document.getElementById("menuBtn").addEventListener("click", () => {
  document.getElementById("navLinks").classList.toggle("open");
});
document.querySelectorAll("#navLinks a").forEach(link => {
  link.addEventListener("click", () => document.getElementById("navLinks").classList.remove("open"));
});

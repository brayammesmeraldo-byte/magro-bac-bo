async function addResult(result) {
  await fetch("/api/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ result })
  });
  fetchData();
}

async function fetchData() {
  const stats = await fetch("/api/stats").then(r => r.json());
  const streaks = await fetch("/api/streaks").then(r => r.json());
  const suggest = await fetch("/api/suggest").then(r => r.json());
  const history = await fetch("/api/history").then(r => r.json());

  document.getElementById("stats").innerHTML = `
    Rodadas: ${stats.total}<br>
    Player: ${stats.P_pct}%<br>
    Banker: ${stats.B_pct}%<br>
    Tie: ${stats.T_pct}%
  `;

  document.getElementById("streaks").innerHTML = `
    Player: ${streaks.P}<br>
    Banker: ${streaks.B}<br>
    Tie: ${streaks.T}
  `;

  document.getElementById("suggest").innerHTML = `🎯 ${suggest.suggestion}`;

  const historyDiv = document.getElementById("history");
  historyDiv.innerHTML = "";
  history.forEach(r => {
    const span = document.createElement("span");
    span.textContent = r;
    span.className = r;
    historyDiv.appendChild(span);
  });
}

setInterval(fetchData, 2000);
fetchData();
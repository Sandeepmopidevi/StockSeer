function searchStock() {
  const input = document.getElementById("tickerInput").value.toLowerCase();
  const datalist = document.getElementById("tickers");
  datalist.innerHTML = "";

  Object.keys(tickerMap)
    .filter(name => name.toLowerCase().includes(input))
    .forEach(name => {
      const option = document.createElement("option");
      option.value = name;
      datalist.appendChild(option);
    });
}

async function getPrediction() {
  const fullName = document.getElementById("tickerInput").value;
  const ticker = tickerMap[fullName];

  if (!ticker) {
    document.getElementById("result").innerHTML = `<p style="color:red;">Invalid company name.</p>`;
    return;
  }

  try {
    const res = await fetch(`http://127.0.0.1:5000/predict?ticker=${ticker}`);
    const data = await res.json();

    if (data.error) {
      document.getElementById("result").innerHTML = `<p style="color:red;">Error: ${data.error}</p>`;
      return;
    }

    document.getElementById("result").innerHTML = `
      <h4>Prediction for: ${fullName} (${data.ticker})</h4>
      <p>📉 Predicted Price: <b>${data.latest_predicted_price.toFixed(2)}</b></p>
      <p>📊 RMSE: ${data.rmse.toFixed(2)}</p>
      <p>💡 Investment Advice: <b>${data.suggestion}</b></p>
      <p>🔮 Next 10 predicted prices:</p>
      <pre>${JSON.stringify(data.prediction.map(p => p.toFixed(2)), null, 2)}</pre>
    `;
  } catch (err) {
    document.getElementById("result").innerHTML = `<p style="color:red;">Backend Error: ${err.message}</p>`;
  }
}

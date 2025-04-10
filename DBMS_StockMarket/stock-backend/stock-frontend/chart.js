<canvas id="stockChart"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
async function loadChart(symbol) {
  const response = await fetch(`http://localhost:5000/api/chart-data/${symbol}`);
  const data = await response.json();

  const ctx = document.getElementById("stockChart").getContext("2d");
  new Chart(ctx, {
    type: "line",
    data: {
      labels: data.dates,
      datasets: [
        {
          label: "Close Price",
          data: data.close,
          borderColor: "blue",
          fill: false
        },
        {
          label: "Volume",
          data: data.volume,
          type: "bar",
          backgroundColor: "rgba(0,0,0,0.1)",
          yAxisID: 'y1'
        }
      ]
    },
    options: {
      scales: {
        y: { type: 'linear', position: 'left', title: { display: true, text: 'Price' }},
        y1: { type: 'linear', position: 'right', title: { display: true, text: 'Volume' }}
      }
    }
  });
}

loadChart("RELIANCE"); // Replace with selected stock symbol
</script>

document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction-result').innerText = `Predicted Price: ₹${data.prediction.toFixed(2)} lakhs`;

        // Update bar chart
        const barChart = document.getElementById('bar-chart');
        barChart.innerHTML = '';  // Clear previous chart (if any)

        const plotData = [{
            x: data.sum_price_by_area.map(item => item.Area_type),
            y: data.sum_price_by_area.map(item => item['Price in lakhs']),
            type: 'bar'
        }];
        document.getElementById('bar-dis').innerHTML = "Bar chart based on 2022 Data(x-axis:Area type, y-axis: sum of price)"
        Plotly.newPlot('bar-chart', plotData);

        // Display top 10 results
        const pricesTableBody = document.getElementById('prices-table-body');
        pricesTableBody.innerHTML = '';  // Clear previous table rows (if any)
        
        data.results.forEach(result => {
            const row = document.createElement('tr');
            const totalSqftCell = document.createElement('td');
            totalSqftCell.innerText = result.Total_sqft;
            const actualPriceCell = document.createElement('td');
            actualPriceCell.innerText = `₹${result['Actual Price'].toFixed(2)} lakhs`;
            const predictedPriceCell = document.createElement('td');
            predictedPriceCell.innerText = `₹${result['Predicted Price'].toFixed(2)} lakhs`;

            row.appendChild(totalSqftCell);
            row.appendChild(actualPriceCell);
            row.appendChild(predictedPriceCell);
            pricesTableBody.appendChild(row);
        });
    });
});

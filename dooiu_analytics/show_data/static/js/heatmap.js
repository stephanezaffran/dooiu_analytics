

window.addEventListener('resize', function() {

        drawHeatmap();
      });
window.addEventListener('load', function() {
        drawHeatmap();
      });

var salesCheckbox = document.getElementById('salesCheckbox');
var conversationCheckbox = document.getElementById('conversationCheckbox');
var trace
var layout

salesCheckbox.addEventListener('change', function () {
    if (salesCheckbox.checked) {
        conversationCheckbox.checked = false;
        updateHeatmap('sales');
      }
});

conversationCheckbox.addEventListener('change', function () {
      if (conversationCheckbox.checked) {
        salesCheckbox.checked = false;
        updateHeatmap('calltime');
      }
});

function updateHeatmap(selectedOption) {
  trace.z = selectedOption === 'sales' ? sales : calltime;
  layout.annotations = [];
  show_text();
  Plotly.react('heatmap3', [trace], layout);
}

function show_text() {
   for (var i = 0; i < trace.y.length; i++) {
              for (var j = 0; j < trace.x.length; j++) {
                var currentValue = trace.z[i][j];
                var textColor = 'black';

                layout.annotations.push({
                  xref: 'x1',
                  yref: 'y1',
                  x: trace.x[j],
                  y: trace.y[i],
                  text: currentValue.toFixed(0),
                  showarrow: false
                });
             }
          }
}


function drawHeatmap() {
// Sample data (replace this with your actual data)

      // Set the heatmap trace
      trace = {
        x: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        y: ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'],
        z: sales,
        type: 'heatmap',
        colorscale: [[0, '#4be0eb'],[0.2, '#3ff13d'],[0.5, 'yellow'],[1, 'red']],
        reversescale: false,
        hoverongaps: false,
        xgap: 1/4,
        ygap: 1/4,
      };

      // Set the layout options
      layout = {
        annotations: [],
        paper_bgcolor: '#f6eae7',
        title: 'Weekly Heatmap',
        xaxis: { title: '' , side: 'top'},
        yaxis: { title: '' },
        displayModeBar: false,
      };

       show_text()
      // Create and draw the heatmap
      Plotly.newPlot('heatmap3', [trace], layout);

}
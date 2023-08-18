

google.charts.load('current', { 'packages': ['table'] });
google.charts.load('current', {'packages': ['geochart']});


google.charts.setOnLoadCallback(drawRegionsMap1);
google.charts.setOnLoadCallback(drawRegionsMap2);

//google.charts.setOnLoadCallback(drawChart2);
//google.charts.setOnLoadCallback(drawChart3);
//google.charts.setOnLoadCallback(drawChart4);

window.addEventListener('resize', function() {
        drawRegionsMap1();
        drawRegionsMap2();
      });

function drawRegionsMap1() {

       var data = google.visualization.arrayToDataTable(annual_revenus_per_region);

//       var data = new google.visualization.DataTable();
//            data.addColumn('string', 'Country');
//            data.addColumn('number', 'Value');
//
//      // Add the data rows
//      data.addRows([
//            ['US', 100],
//            ['CA', 80],
//            ['MX', 70],
//            ['fr', 110],
//            ['be', 110],
//            ['ca', 95],
//            ['ru', 85],
//          ]);
        var options = {
            title: 'revenus',
//            width: 600,
//            height: 400,
            region: 'world',
            colorAxis: { colors: ['yellow', 'red'] },
             legend: { position: 'bottom' }, // You can use 'right' for a legend on the right side
        // Customize the title font style
        titleTextStyle: {
          fontSize: 16,
          bold: true,
          italic: false,
          color: '#456' // Change to the desired color
        }
          };
          var chart = new google.visualization.GeoChart(document.getElementById('heatmap1'));
          chart.draw(data, options);
}


function drawRegionsMap2() {

        var data = google.visualization.arrayToDataTable(clients_per_region);

//       var data = new google.visualization.DataTable();
//            data.addColumn('string', 'Country');
//            data.addColumn('number', 'Value');
//
//      // Add the data rows
//      data.addRows([
//            ['US', 80],
//            ['CA', 30],
//            ['MX', 70],
//            ['fr', 60],
//            ['ru', 75],
//            ['ca', 85],
//          ]);
        var options = {
            title: 'sales',
//            width: 600,
//            height: 400,
             colorAxis: { colors: ['yellow', 'red'] },
//            legend: 'none',
          };
      var chart = new google.visualization.GeoChart(document.getElementById('heatmap2'));
      chart.draw(data, options);
}



//  function drawHeatmap() {
//      // Sample data (replace this with your actual data)
//      var data = google.visualization.arrayToDataTable([
//        ['m', 'Time', 'Value'],
//        ['Monday', 'Morning', 20],
//        ['Monday', 'Afternoon', 10],
//        ['Monday', 'Evening', 30],
//        ['Tuesday', 'Morning', 40],
//        ['Tuesday', 'Afternoon', 50],
//        ['Tuesday', 'Evening', 60],
//        // Add more data rows here
//      ]);
//
//      // Set chart options
//          // Calculate the minimum and maximum values in the data
//      var minValue = getMinValue(data, 2);
//      var maxValue = getMaxValue(data, 2);
//
//      // Set table options
//      var options = {
//        title: 'Table with Cell Colors',
//        // Use a number formatter to set cell colors based on values
//        allowHtml: true,
//        showRowNumber: true,
//        width: '100%',
//        height: '100%'
//      };
//
//      // Create and draw the table
//      var table = new google.visualization.Table(document.getElementById('heatmap3'));
//      var formatter = new google.visualization.ColorFormat();
//      formatter.addRange(minValue, maxValue, 'yellow', 'red');
//      formatter.format(data, 1); // Apply formatter to second column
//      table.draw(data, options);
//    }
//
// function getMinValue(data, column) {
//      var minValue = data.getValue(0, column);
//      for (var i = 1; i < data.getNumberOfRows(); i++) {
//        var value = data.getValue(i, column);
//        console.log("Hello world!" + value + minValue);
//        if (value < minValue) {
//          minValue = value;
//        }
//      }
//      return minValue;
//    }
//
//    function getMaxValue(data, column) {
//      var maxValue = data.getValue(0, column);
//      for (var i = 1; i < data.getNumberOfRows(); i++) {
//        var value = data.getValue(i, column);
//        if (value > maxValue) {
//          maxValue = value;
//        }
//      }
//      return maxValue;
//    }


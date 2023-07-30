
google.charts.load('current', {'packages': ['corechart']});
google.charts.setOnLoadCallback(drawChart1);
google.charts.setOnLoadCallback(drawChart2);
google.charts.setOnLoadCallback(drawChart3);
google.charts.setOnLoadCallback(drawChart4);

function drawChart1() {

    const  my_axis = Math.ceil(day_list.length / 5);

    var data = google.visualization.arrayToDataTable(day_list);

    var options = {
        title: 'communication per day',
        legend: { position: 'bottom' },
//         backgroundColor: '#f2f2f2',
         hAxis: {showTextEvery: my_axis},
          width:450,
        height:250,
    };
    var chart = new google.visualization.LineChart(document.getElementById('widget4'));

    chart.draw(data, options);
}


function drawChart2() {
    var data = google.visualization.arrayToDataTable(month_list);
    var options = {
        title: 'communication per month',
        width:450,
        height:250,
        legend: { position: 'none' }
    };
    var chart = new google.visualization.ColumnChart(document.getElementById('widget5'));
    chart.draw(data, options);
}


function drawChart3() {
    var data = google.visualization.arrayToDataTable(year_list);
    var options = {
        title: 'communication per year',
         width:450,
        height:250,
        legend: { position: 'top' }
    };
    var chart = new google.visualization.PieChart(document.getElementById('widget6'));
    chart.draw(data, options);
}

function drawChart4() {

    const  my_axis = Math.ceil(day_list.length / 5);

    var data = google.visualization.arrayToDataTable(news_clients_per_month);

    var options = {
        title: 'new client per month',
        legend: { position: 'bottom' },
//         backgroundColor: '#f2f2f2',
         hAxis: {showTextEvery: my_axis},
          width:450,
        height:250,
    };
    var chart = new google.visualization.LineChart(document.getElementById('widget7'));

    chart.draw(data, options);
}



//function drawChart4() {
//    var data = google.visualization.arrayToDataTable(graph_data_4);
//    var options = {
//        title: 'Sales and Expenses per Month',
//       width:450,
//        height:250,
//        curveType: 'function',
//        legend: { position: 'bottom' }
//    };
//    var chart = new google.visualization.LineChart(document.getElementById('widget7'));
//    chart.draw(data, options);
//}
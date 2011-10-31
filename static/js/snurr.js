var chart;
$(document).ready(function() {
    // define the options
    var options = {
        chart: {
            renderTo: 'container'
        },
        title: {
            text: 'Log entries'
        },
        xAxis: {
            title: {
                text: 'Date'
            },
            type: 'datetime',
            dateTimeLabelFormats: {
                hour: '%Y-%m-%d',
            }
        },
        yAxis: {
            title: {
                text: 'Number of log entries'
            },
            min: 0,
            max: 40 
        },
        legend: {
            borderWidth: 0
        },
        tooltip: {
            shared: true,
        },
        plotOptions: {
            series: {
                cursor: 'pointer',
                point: {
                    events: {
                        click: function() {
                            hs.htmlExpand(null, {
                                pageOrigin: {
                                    x: this.pageX, 
                                    y: this.pageY
                                 },
                                 headingText: this.series.name,
                                 maincontentText: Highcharts.dateFormat('%Y-%m-%d', this.x) +':<br/> '+ this.y +' entries',
                                width: 200
                           });
                        }
                    }
                },
                marker: {
                    lineWidth: 1
                }
            }
        },
        series: []
    };
    var url = 'http://localhost:8000/log/';
    $.getJSON(url, function(data) {
        $.each(data, function(user, val) {

            // convert to unixtime and fill lines array.
            var line = [];
            $.each(val, function(i, num) {
                line[i] = new Array(Date.parse(num[0]), num[1]);
            });
            options.series.push({
                name: user,
                lineWidth: 4,
                marker: {
                    radius: 4
                },
                data: line
            });
        });
        chart = new Highcharts.Chart(options);
    });
});

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
    var url = '/log/';
    $.getJSON(url, function(data) {
        var max = 0;
        $.each(data, function(user, val) {

            // convert to unixtime and fill lines array.
            var line = [];
            $.each(val, function(i, num) {
                if(num[1] > max) {
                    max = num[1];
                }
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
        options.yAxis.max = max + 5;
        chart = new Highcharts.Chart(options);
    });
});

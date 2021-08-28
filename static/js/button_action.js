$("#slam_btn").click(function() {
    $.get("http://192.168.0.6:5000/start_slam", function(data, status) {});
});

$("#navigation_btn").click(function() {
    $.get("http://192.168.0.6:5000/map_options", function(data, status) {
        if (status == 'success') {
            $("#map_list").empty();
            $("#map_list").append(data);
        }
    });
    $.get("http://192.168.0.6:5000/choose_map", function(data, status) {});
});

$("#start_navigation_btn").click(function() {
    var map_name = $('#map_list option:selected').text();
    $.get("http://192.168.0.6:5000/start_navigatoin", { 'map_name': map_name }, function(data, status) {});
});

$("#save_data_btn").click(function() {
    var map_name = $('#map_name_input').val();
    $.get("http://192.168.0.6:5000/save_data", { 'map_name': map_name }, function(data, status) {});
});

$("#exit_btn").click(function() {
    $.get("http://192.168.0.6:5000/exit", function(data, status) {});
});
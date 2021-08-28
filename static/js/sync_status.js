function update_status() {
    $.get("http://192.168.0.6:5000/status", function(data, status) {
        if (status == 'success') {
            if (data == '0') {
                $('#main_menu').show('slow');
                $('#map_slection_menu').hide('slow');
                $('#edc_menu').hide('slow');
                $('#exit_menu').hide('slow');
            }
            if (data == '1') {
                $('#main_menu').hide('slow');
                $('#map_slection_menu').show('slow');
                $('#edc_menu').hide('slow');
                $('#exit_menu').show('slow');
            }
            if (data == '2') {
                $('#main_menu').hide('slow');
                $('#map_slection_menu').hide('slow');
                $('#edc_menu').show('slow');
                $('#exit_menu').show('slow');
            }
        }
    });
}

setInterval(update_status, 500)
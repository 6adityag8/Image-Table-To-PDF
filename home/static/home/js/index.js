/* List of accepted image extensions */
const valid_image_extensions = new Set(["jpg", "jpeg", "bmp", "gif", "png"]);

/* Function to Upload the selected image */
function upload_image(event) {
    let error_div = $('#error_message');
    let image_upload_form = $('#upload_image_form');
    error_div.hide();
    let image = event.target.files[0];
    let image_extension = image.name.split('.').pop();
    if (!valid_image_extensions.has(image_extension)) {
        display_error_message('Please upload an image file.');
        return;
    }
    let image_data = new FormData(image_upload_form.get(0));
    $.ajax({
        type: 'POST',
        url: IMAGE_UPLOAD_URL,
        data: image_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (data) {
            if (data.error) {
                display_error_message(data.error);
                return;
            }
            if (data.uploaded_file) {
                $("#id_image_path").val(data.uploaded_file);
            }
            else {
                display_error_message('Something went wrong. Please try again.');
            }
        },
        error: function () {
            display_error_message('Something went wrong. Please try again.');
        }
    });
}

/* Function to display an error message */
function display_error_message(error_msg) {
    let image_upload_form = $('#upload_image_form');
    let error_div = $('#error_message');
    image_upload_form[0].reset();
    error_div.html(error_msg);
    error_div.show();
}

/* Function to display the required cells of the table */
function populate_table(selected_row, selected_column) {
    for (let row = 1; row <= selected_row; row++) {
        for (let column = 1; column <= selected_column; column++) {
            $("#table_input_" + String(row) + "_" + String(column)).show();
        }
    }
}

/* Function to hide all the cells of the table */
function hide_table() {
    for (let row = 1; row <= 3; row++) {
        for (let column = 1; column <= 3; column++) {
            $("#table_input_" + String(row) + "_" + String(column)).hide();
        }
    }
}

/* Function to fetch values in all the cells of the table */
function fetch_table_data() {
    let table_data = {};
    for (let row = 1; row <= 3; row++) {
        for (let column = 1; column <= 3; column++) {
            table_data[String(row) + "_" + String(column)] =
                $("#table_input_" + String(row) + "_" + String(column) + " input[type=text]").val();
        }
    }
    return table_data;
}

/* Function which prepares data and send to backend via AJAX POST request */
function send_data_to_backend_to_create_pdf() {
    let image_path = $("#id_image_path").val();
    let selected_table_size = $("#id_table_sizes").val();
    let row = selected_table_size.split(',')[0];
    let column = selected_table_size.split(',')[1];
    let data = {
        'image_path': image_path,
        'row': row,
        'column': column,
        'table_data': fetch_table_data(),
    };
    $.ajax({
        type: 'POST',
        url: CREATE_PDF_URL,
        data: data,
        cache: false,
        success: function (res) {
            if (res.error) {
                display_error_message(res.error);
                return;
            }
            if (res.created_pdf) {
                window.open(MEDIA_URL + res.created_pdf);
            }
            else {
                display_error_message('Something went wrong. Please try again.');
            }
        },
        error: function () {
            display_error_message('Something went wrong. Please try again.');
        }
    });
}

$(document).ready(function () {

    /* Hide the table initially */
    hide_table();

    /* Called when an image is selected to be uploaded */
    $("#id_image_upload").on("change", function (event) {
        upload_image(event);
    });

    /* Called when a Table Size is selected from the drop down*/
    $("#id_table_sizes").on("change", function () {
        hide_table();
        let selected_table_size = $("#id_table_sizes").val();
        let row = selected_table_size.split(',')[0];
        let column = selected_table_size.split(',')[1];
        populate_table(row, column);
    });

    /* Called when Submit button is clicked */
    $("#submit_button").on("click", function () {
        send_data_to_backend_to_create_pdf();
    });

});
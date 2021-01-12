const valid_image_extensions = new Set(["jpg", "jpeg", "bmp", "gif", "png"]);

function upload_image(event) {
    let error_div = $('#image_file_error');
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

function display_error_message(error_msg) {
    let image_upload_form = $('#upload_image_form');
    let error_div = $('#image_file_error');
    image_upload_form[0].reset();
    error_div.html(error_msg);
    error_div.show();
}
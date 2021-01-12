from django import forms


class UploadImageForm(forms.Form):
    """
    Form to upload image
    """
    image_upload = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'onchange': 'upload_image(event)',
                'accept': 'image/*',
            }
        )
    )
    image_path = forms.CharField(
        required=False,
        widget=forms.HiddenInput()
    )

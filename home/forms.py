from django import forms

TABLE_SIZE = 3
TABLE_SIZE_CHOICES = [('0,0', 'Select a Table Size')] + \
                     [('{0},{1}'.format(str(row), str(column)), '{0} X {1}'.format(str(row), str(column)))
                      for row in range(1, TABLE_SIZE + 1) for column in range(1, TABLE_SIZE + 1)]


class UploadImageForm(forms.Form):
    """
    Form to upload image
    """
    image_upload = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )
    image_path = forms.CharField(
        required=False,
        widget=forms.HiddenInput()
    )
    table_sizes = forms.ChoiceField(
        required=False,
        choices=TABLE_SIZE_CHOICES,
    )

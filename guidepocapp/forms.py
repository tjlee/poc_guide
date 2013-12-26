from django import forms
from guidepocapp.models import Guide


class RegisterGuideForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegisterGuideForm, self).__init__(*args, **kwargs)
        self.fields['pwd'].label = "Password"


    class Meta:
        model = Guide
        fields = ['email', 'pwd', 'surname', 'name', 'phone1', 'phone2', 'skype', 'comments']

        widgets = {
            'pwd': forms.PasswordInput()
        }

        # email = forms.EmailField(max_length=60)
        # password = forms.CharField(max_length=20, widget=forms.PasswordInput)
        # password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)
        #
        # surname = forms.CharField(max_length=60)
        # name = forms.CharField(max_length=60)
        # phone1 = forms.CharField(max_length=20, required=False)
        # phone2 = forms.CharField(max_length=20, required=False)
        # skype = forms.CharField(max_length=40, required=False)
        # comments = forms.CharField(max_length=2048, required=False)

        # places = forms.CheckboxSelectMultiple()
        # todo: need more investigation on it now just register
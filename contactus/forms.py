from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True,
    	widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    contact_email = forms.EmailField(required=True,
    	widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    contact_phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."),
                                widget=forms.TextInput(attrs={'placeholder': 'You Phone'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'We would love to hear from you!'})
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].placeholder = "Your name:"
        self.fields['contact_email'].placeholder = "Your email:"
        self.fields['contact_phone'].placeholder = "Your phone:"
        self.fields['content'].placeholder = "What do you want to say?"
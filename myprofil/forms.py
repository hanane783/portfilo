from django import forms
from .models import ContactMessage
from django.core.mail import send_mail

class ContactForm(forms.ModelForm):
    class Meta:

        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

    def send_email(self):
        subject = f"message from website: {self.cleaned_data['name']}"
        message = f"""
        name: {self.cleaned_data['name']}
        email: {self.cleaned_data['email']}
        message:
        {self.cleaned_data['message']}
        """
        send_mail(subject, message, self.cleaned_data['email'], ['messaimohammed.hanane@univ-ouargla.dz'])  # هنا الإيميل الذي سيستقبل
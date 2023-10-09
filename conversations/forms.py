from django import forms


class AddCommentForm(forms.Form):
    message = forms.CharField(
        required=True, widget=forms.Textarea(attrs={"placeholder": "Write a Message"})
    )

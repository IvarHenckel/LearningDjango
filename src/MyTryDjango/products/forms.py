from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
            label='', 
            widget=forms.TextInput(
                attrs={
                    "placeholder":"Your Title"
                }
            )
    ) # This apperently overrides the way title would have been shown if we had skipped this. (Kind of strange since this is only a field)
    email = forms.EmailField() # We can include things thaat our not in our model
    class Meta:
        model = Product # when we call form.save and so on it will be saved as a Product
        # Handle by ModelForm I assume?
        fields = [
            'title',
            'description',
            'price',
        ]
    def clean_title(self, *args, **kwargs):# with clean_<field> we can define more validations (Note that django can apply other validations as well)
        title = self.cleaned_data.get("title")
        if "slotts senap" in title:
            raise forms.ValidationError("This is an invalid title")
        else:
            return title
    #Note: we can have vaildation inside the model on the actual model fields as well, forms is jut used as an example here


class RawProductForm(forms.Form):
    title = forms.CharField(
            label='', 
            widget=forms.TextInput(
                attrs={
                    "placeholder":"Your Title"
                }
            )
    )
    description = forms.CharField(
            required=False, 
            widget=forms.Textarea(
                attrs={
                    "placeholder": "Your Description",
                    "class": "new-class-name two",
                    "id": "my-id-for-textarea",
                    "rows": 20,
                    "columns": 60
                }
            )
    )
    price = forms.DecimalField(initial=199.99)
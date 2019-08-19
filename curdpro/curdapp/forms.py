from django import forms

class ProductInsertForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter product id',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )

    product_name = forms.CharField(
        label='Enter Product Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )

    product_cost = forms.IntegerField(
        label='Enter Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )

    product_color = forms.CharField(
        label='Enter Product Color',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )

    product_class = forms.CharField(
        label='Enter Product Class',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product class'
            }
        )
    )

    customer_name = forms.CharField(
        label = 'Enter Customer Name',
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your name'
            }
        )
    )

    customer_mobile =  forms.IntegerField(
        label = 'Enter mobile number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )

    customer_email = forms.EmailField(
        label = 'Enter Email ID',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email ID'
            }
        )
    )







class ProductUpdateForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Product Id',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )

    product_cost = forms.IntegerField(
        label='Enter Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Cost'
            }
        )
    )


class ProductDeleteForm(forms.Form):
    product_id=forms.IntegerField(
        label='Enter Product id',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )





















from django import forms
from .models import Student, Address, Student3, Product

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class Student3Form(forms.ModelForm):
    class Meta:
        model = Student3
        fields = ['name', 'age', 'address']
        widgets = {
            'address': forms.CheckboxSelectMultiple()
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image']

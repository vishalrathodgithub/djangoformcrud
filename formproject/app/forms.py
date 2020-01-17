from django import forms
from .models import Book
from django.core import validators


class BookForm(forms.Form):
    bookname = forms.CharField()
    author = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(3)])
    page = forms.IntegerField()
    price = forms.IntegerField()

    # def clean_bookname(self):
    #     print("validation author")
    #     a= self.cleaned_data['bookname']
    #     if len(a) < 4:
    #         raise forms.ValidationError("the minimum length og string should be 4")
    #     return a
    # def clean_author(self):
    #     print("validation author")
    #     a= self.cleaned_data['author']
    #     if a!='vishal' :
    #         raise forms.ValidationError("name should be vishal")
    #     return a
    def clean(self): #by using super method we can do all field vaildations
        print("total validation")
        total_valid = super().clean()
        name = total_valid["bookname"]
        if name[0].lower() != "v":
            raise forms.ValidationError("name should be start with v")
        pages = total_valid["page"]
        if pages < 100:
            raise forms.ValidationError("page always gtr than 100")

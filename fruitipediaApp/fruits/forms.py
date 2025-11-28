from django import forms

from fruitipediaApp.fruits.models import Category


class CategoryBaseForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Category name'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''

    class Meta:

        model = Category
        fields = "__all__"


class CategoryCreateForm(CategoryBaseForm):
    pass
from django import forms

class presentPriceSearch(forms.Form):
    search_word = forms.CharField(label = 'Search Word')

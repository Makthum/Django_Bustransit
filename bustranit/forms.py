__author__ = 'zarroc'
from django import forms

agent=(('ttc','ttc'),('yrt','yrt'),)

class findbus(forms.Form):
    routeNo=forms.CharField(max_length=10)
    #agent=forms.ChoiceField(choices=agent,widget=forms.RadioSelect())



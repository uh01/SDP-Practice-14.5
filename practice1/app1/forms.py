from django import forms
from django.forms.widgets import NumberInput
import datetime
# from .models import MyModel

# Create your forms here.

BIRTH_YEAR_CHOICES = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005']
FAVORITE_COLORS_CHOICES = [('blue', 'Blue'), ('green', 'Green'),('black', 'Black'),]

class contactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
	comment = forms.CharField(widget=forms.Textarea)
	birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
	value = forms.DecimalField()
	email_address = forms.EmailField(required = False,)
	message = forms.CharField(max_length = 10,)
	Comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
	# first_name = forms.CharField(initial='Your name')
	Email_address = forms.EmailField(label="Please enter your email address",)
	day = forms.DateField(initial=datetime.date.today)
	favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
	# favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
	# favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
	favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")  
	user_name = forms.CharField(max_length = 200) 
	password = forms.CharField(widget = forms.PasswordInput())  
     
    
	


    # model_choice = forms.ModelChoiceField(queryset = MyModel.objects.all(),initial = 0)
	# model_choices = forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple,queryset = MyModel.objects.all(),initial = 0)
    
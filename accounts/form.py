from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,transltor,mousaqe,payer,Video,dasboardvedio,uploadtranlate
from django.contrib.auth.forms import AuthenticationForm







FAVORITE_COLORS_CHOICES =\
    [
        ('Indian', 'Indian'),
        ('Ardu', 'Ardu'),
        ('taqalu', 'taqalu'),
        ('taqalu', 'taqalu'),
        ('Bangladeshi', 'Bangladeshi'),

]




class transltorSignUpForm(UserCreationForm):
    Languages = forms.CharField(required=True)
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': ' كلمة السر',

                                          }),
    )

    password2 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'تاكيد كلمة السر',

                                          }),
    )
    username = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': '  الاسم',

                                          }),
    )



    Languages = forms.ChoiceField(
        choices=FAVORITE_COLORS_CHOICES,
   )




    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_transltor = True
        user.save()
        transltores = transltor.objects.create(user=user)
        transltores.Languages=self.cleaned_data.get('Languages')
        transltores.save()
        return user




class mousaqeSignUpForm(UserCreationForm):

    username = forms.CharField(
        label="Password",
        strip=True,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': '  اسم الجامع',

                                          }),
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                 'placeholder': ' كلمة السر',

                                          }),
    )


    password2 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                 'placeholder': 'تاكيد كلمة السر',

                                          }),
    )

    city = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': '  المدينة ',

                                          }),
    )

    eara = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': '  الحي ',

                                          }),
    )






    class Meta(UserCreationForm.Meta):
        model = User








    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_mousaqe = True
        user.save()
        employee = mousaqe.objects.create(user=user)
        employee.city=self.cleaned_data.get('city')
        employee.eara=self.cleaned_data.get('eara')

        employee.save()
        return user





class payerSignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': ' كلمة السر  ',

                                          }),
    )

    password2 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'تاكيد كلمة السر',

                                          }),
    )
    username = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': '  اسم المستخدم',

                                          }),
    )
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_payer = True
        user.save()
        employee = payer.objects.create(user=user)
        employee.save()
        return user









class Video_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'



class uploadtranlate_form(forms.ModelForm):
    class Meta:
        model = uploadtranlate
        fields = '__all__'






class dasboardvedio_form(forms.ModelForm):
    class Meta:
        model = dasboardvedio
        fields = '__all__'





class RFPAuthForm(AuthenticationForm):
        username = forms.CharField(
            label="اسم المستخدم",
            strip=False,
            widget=forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': '  اسم المستخدم',

                                              }),
        )
        password = forms.CharField(
            label="كلمة السر",
            strip=False,
            widget=forms.PasswordInput(attrs={'class': 'form-control',
                                              'placeholder': '  اسم المستخدم',

                                              }),
        )






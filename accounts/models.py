from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_transltor = models.BooleanField(default=False)
    is_mousaqe = models.BooleanField(default=False)
    is_payer=models.BooleanField(default=False)

    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)



class transltor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    Languages = models.CharField(max_length=20)
    def __str__(self):
        return self.user.username



class citys(models.Model):
    address=models.CharField(max_length=150)
    def __str__(self):
        return self.address



class earas(models.Model):
    city=models.ForeignKey(citys,on_delete=models.CASCADE)
    eara=models.CharField(max_length=150)

    def __str__(self):
            return self.eara



class mousaqe(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    city= models.CharField(max_length=200,blank=True, null=True )
    eara=models.CharField(max_length=200,blank=True, null=True)
    profile=models.ImageField(upload_to='pic' ,blank=True, default=None  )


    def __str__(self):
        return self.user.username


class mousaqeProfile(models.Model):
    mousaq = models.ForeignKey(mousaqe, on_delete=models.CASCADE)
    profile=models.ImageField(upload_to='pic' ,blank=True, default=None  )


    def __str__(self):
        return self.mousaq.user.username


class payer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    def __str__(self):
        return self.user.username


from datetime import date

class Video(models.Model):
    mousaq=models.ForeignKey(mousaqe,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    video=models.FileField(upload_to='vedio')
    date=models.DateField(default=date.today)
    states=models.BooleanField(default=False)

    def __str__(self):
        return self.title









class dasboardvedio(models.Model):
    STATAS_CHOICES = (
        ("غير مترجمة", "غير مترجم"),
        ("قيد الترجمة", "قيد مترجم"),
        (" مترجمة", " مترجمة"),

    )

    vedio=models.ForeignKey(Video,on_delete=models.CASCADE)
    translate=models.ForeignKey(transltor,on_delete=models.CASCADE)
    states=models.CharField(max_length=15,choices=STATAS_CHOICES,default=None)
    def __str__(self):
        return self.vedio.title





class uploadtranlate(models.Model):
    translate=models.OneToOneField(transltor,on_delete=transltor)
    vedio=models.OneToOneField(Video,on_delete=Video)
    pdftranslate=models.FileField(upload_to='translate')
    datetime=models.DateField(default=None)

    def __str__(self):
        return self.user.username




class file_after_tranlated(models.Model):
    title=models.CharField(max_length=150)
    mousaqe=models.ForeignKey(mousaqe,on_delete=models.CASCADE)
    pdf=models.FileField(upload_to='translated')
    language=models.CharField(max_length=150)
    date=models.DateField()
    def __str__(self):
        return self.title



class comments(models.Model):
    files=models.ForeignKey(file_after_tranlated,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    def __str__(self):
        return self.comment

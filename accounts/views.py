from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from django.views.generic import CreateView
from .form import mousaqeSignUpForm, transltorSignUpForm,payerSignUpForm,Video_form,dasboardvedio_form,uploadtranlate_form
from django.contrib.auth.forms import AuthenticationForm
from .models import citys,earas, User,Video,dasboardvedio,uploadtranlate,mousaqe,transltor,payer,file_after_tranlated
from .form import RFPAuthForm
from django.contrib.auth.models import Group
from .models import mousaqeProfile,comments







def register(request):
    return render(request, '../templates/register.html')

class customer_register(CreateView):
    model = User
    form_class = transltorSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        my_group = Group.objects.get(name='translator')
        my_group.user_set.add(user)
        login(self.request, user)
        return redirect('Home')


class employee_register(CreateView):
    model = User
    form_class = mousaqeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        my_group = Group.objects.get(name='mosaqe')
        my_group.user_set.add(user)
        login(self.request, user)
        id=self.request.user.id
        return redirect(profilemousqe ,id=id)




class payer_register(CreateView):
    model = User
    form_class = payerSignUpForm
    template_name = '../templates/payer_register.html'

    def form_valid(self, form):
        user = form.save()
        my_group = Group.objects.get(name='payer')
        my_group.user_set.add(user)

        login(self.request, user)
        return redirect('Home')



def login_request(request):
    if request.method=='POST':
        form = RFPAuthForm(data=request.POST   )

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect("Home", )
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")

    return render(request, '../templates/login.html',

    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect("Home",)



def ved(request):
    all_video=Video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
         form.save()
        return render(request, "home/index.html", )
    else:
        form=Video_form()
    return render(request,'upload.html',{"form":form,"all":all_video})




def dasboardvedioe(request):
    all_video=dasboardvedio.objects.all()
    if request.method == "POST":
        form=dasboardvedio_form(data=request.POST)
        if form.is_valid():
         form.save()
        return HttpResponse("<h1> Uploaded successfully </h1>")
    else:
        form=dasboardvedio_form()
    return render(request,'dashboard.html',{"form":form,"all":all_video})






def uploadtranlatees(request):
    all_video=uploadtranlate.objects.all()
    if request.method == "POST":
        form=uploadtranlate_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect("Home", )
    else:
        form=uploadtranlate_form()
    return render(request,'uoloadtranslate.html',{"form":form,"all":all_video})


def Home(request):
    if request.method == "POST":
        search = request.POST.get("searchMou")
        print("sssssss")
        print(search)

        mousaqesprofile = mousaqeProfile.objects.all().filter(mousaq__user__username__icontains=search)
        print(mousaqesprofile)
        return render(request, "home/index.html",  {"mousaqesprofile": mousaqesprofile})



    else:

        mousaqes=mousaqe.objects.all()
        mousaqesprofile=mousaqeProfile.objects.all()

        file_transled=file_after_tranlated.objects.all()
        print(file_transled)
        return render(request,"home/index.html",{"file_transled":file_transled , "mousaqesprofile" : mousaqesprofile ,"mousaqes":mousaqes  })


from django.db.models import Q
def mousaqeF(request,id):
    if request.method == "POST":
        search = request.POST.get("search")
        if search =="":
            files = file_after_tranlated.objects.filter(Q(mousaqe_id=id) )
            return render(request,"mousqefiles.html" ,{"files":files})

        else:
            files = file_after_tranlated.objects.filter(Q(mousaqe_id=id) & (Q(title=search) | Q(language=search)))

            return render(request,"mousqefiles.html" ,{"files":files})


    else:
        files=file_after_tranlated.objects.all().filter(mousaqe_id=id).order_by('title','-date')
        print(files)
        print("sssssss")
        return render(request,"mousqefiles.html" ,{"files":files})


def adminpanl(request):
    mousaq=mousaqe.objects.all()
    translt=transltor.objects.all()
    paye=payer.objects.all()

    print(mousaq)

    context = {
        'mousaq':mousaq,

    }
    return render(request, 'home/adminpanl.html',{ 'mousaq':mousaq,'translt':translt,'paye':paye,})



def regesitermousqe(request):
    if request.method == "POST":
        name=request.POST.get("name")

        password=request.POST.get("password")
        password1=request.POST.get("password1")
        citya=request.POST.get("city")
        ears=request.POST.get("ears")


        print("GGGGGGGGGGGG")
        print(name)
        print(password)
        print(citya)
        print(ears)

        return render(request,"mousqueRegister.html" ,{"city": city  , "eara":eara })

    else:

        eara=earas.objects.all()
        city=citys.objects.all()

        return render(request,"mousqueRegister.html" ,{"city": city  , "eara":eara })


def control(request):
    if request.method == "POST":
        dasboardvedi=dasboardvedio.objects.all()
        pdf=Video.objects.all()
        translt=transltor.objects.all()
        name=request.POST.get("mousaq")
        title=request.POST.get("tittle")
        selec=request.POST.get("selec")
        a=Video.objects.all().filter(title=title)[0]
        b=transltor.objects.all().filter(user_id=selec)[0]
        print(a)
        print(b)
        pdf2translte=dasboardvedio(vedio=a,translate=b,states="غير مترجمة" )
        pdf2translte.save()



   

        return redirect("Home", )
    else:
        dasboardvedi = dasboardvedio.objects.all()
        pdf = Video.objects.all().order_by('states')
        translt = transltor.objects.all()

        return render(request, 'control_pdf.html', {'dasboardvedi': dasboardvedi, 'pdf': pdf, 'translt': translt})



def pdf(request):
    if request.method == "POST":
        name=request.POST.get("khotba")
        pdffile=request.FILES.get("file")

        datetime=request.POST.get("datetime")

        vedio=Video(mousaq_id=request.user.id,title=name,video=pdffile,date=datetime)
        vedio.save()
        return redirect("Home", )

    else:

        return render(request,"uploadpdf.html")



from django.contrib.auth.decorators import user_passes_test








@user_passes_test(lambda u: u.groups.filter(name='translator').exists(),login_url="Home")
def transltedfile(request):
    pdf_file=dasboardvedio.objects.all().filter(translate_id=request.user.id)

    print(pdf_file)
    return render(request ,"getfile2translate.html" ,{'pdf_file':pdf_file})



def file_after_translted(request,id):
    if request.method == "POST":
        print("FFFFFFFFFFF")
        print(id)

        name = request.POST.get("title")
        mous = request.POST.get("mousaq")
        pdffile = request.FILES.get("file")
        lanuge = request.POST.get("language")
        time = request.POST.get("datetime")

        file_after=file_after_tranlated(title=name,mousaqe_id=mous,pdf=pdffile,language=lanuge,date=time)
        file_after.save()

        return redirect("Home", )



    else:
        print(id)

        dasboardvedios=dasboardvedio.objects.all().filter(id=id)

        return render(request,'upload_file_after_transleted.html',{'dasboardvedios':dasboardvedios})




def delete_file_after_transleted(request,id):
    file=dasboardvedio.objects.all().filter(id=id).delete()
    print(file)
    return redirect("Home",)


def delete_file_dashboard(request,id):
    file=dasboardvedio.objects.all().filter(id=id).delete()
    return redirect("Home",)



def updatestates(request, id):
    file = Video.objects.get(id=id)
    file.states=True
    file.save()
    print(file)
    return redirect("control",)



def profilemousqe(request, id):
    if request.method == "POST":
        mousq=mousaqe.objects.get(user_id=id)
        image = request.FILES.get("file")

        mousaqeProfiles = mousaqeProfile(mousaq=mousq,profile=image)
        mousaqeProfiles.save()

        return redirect("Home", )

    else:
        return render(request,"profile_mousqe.html")



def comment(request, id):
    if request.method == "POST":
        file=file_after_tranlated.objects.get(id=id)
        coments = request.POST.get("coments")

        savecomments=comments(files=file,comment=coments)
        savecomments.save()
        com=comments.objects.all().filter(files_id=id)

        return render(request,"comments.html",{"com":com} )


    else:
        com=comments.objects.all().filter(files_id=id)

        return render(request,"comments.html",{"com":com} )




def get_mousqe_files(request):
    files=file_after_tranlated.objects.all().filter(mousaqe__user__username__icontains=request.user.username)
    print("aaaaaaaaaaa")
    print(files)
    return render(request,"getmousqefiles.html",{"files":files})



def delete_mousaqe_files(request,id):

    file=file_after_tranlated.objects.all().filter(id=id).delete()

    files=file_after_tranlated.objects.all().filter(mousaqe__user__username__icontains=request.user.username)

    return render(request,"getmousqefiles.html",{"files":files})

from django.shortcuts import render
from myapp import forms
from django.core.files.storage import FileSystemStorage
from myapp.utilities import store_image
# Create your views here.
def builtin(request):
    if request.method=="POST":
        form=forms.SampleForm(request.POST,request.FILES)
        if form.is_valid():
            first_name= form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            pwd= form.cleaned_data.get('pwd')
            phno=form.cleaned_data.get('phno')
            birth_day=form.cleaned_data.get('birth_day')
            birth_month= form.cleaned_data.get('birth_month')
            birth_year=form.cleaned_data.get('birth_year')
            gender=form.cleaned_data.get('gender')
            image=form.cleaned_data.get('image')
            store_image(image)
            data=form.cleaned_data
            return render(request,'displaydata.html',context=data)
    form=forms.SampleForm()
    return render(request,'builtin.html',{'form':form})

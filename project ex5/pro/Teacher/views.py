from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import AddMarkForm,AddStudentForm,StudentMForm
from django.contrib import messages
from .models import StudentModel
from django.utils.decorators import method_decorator



#decorator for auth-check
def signin_required(fun):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fun(request,*args,**kwargs)
        else:
            return redirect("log")
    return wrapper            


# Create your views here.

@method_decorator(signin_required,name='dispatch')
class AddMark(View):
    def get(self,request,*args,**kwargs):
        f=AddMarkForm()
        return render(request,"addmark.html",{"form":f})
    def post(self,request,*args,**kwargs):        
        form_data=AddMarkForm(data=request.POST)
        if form_data.is_valid():
            num1=form_data.cleaned_data.get("mark1")
            num2=form_data.cleaned_data.get("mark2")
            num3=form_data.cleaned_data.get("mark3")
            num4=form_data.cleaned_data.get("mark4")
            
            res=int(num1)+int(num2)+int(num3)+int(num4)
            return render(request,"addmark.html",{"data":res})
        else:
            return render(request,"addmark.html",{"form":form_data})    


#class AddStudentView(View):
#    def get(self,request,*args,**kwargs):
 #       f=AddStudentForm()
#        return render(request,"addstu.html",{"form":f})
#    def post(self,request,*args,**kwargs):
#        form_data=AddStudentForm(data=request.POST)
#        if form_data.is_valid():
#            fn=form_data.cleaned_data.get("first_name")
 #           ln=form_data.cleaned_data.get("last_name")
 #           age=form_data.cleaned_data.get("age")
 #           address=form_data.cleaned_data.get("address")
#            email=form_data.cleaned_data.get("email")
#            phone=form_data.cleaned_data.get("phone")
#            StudentModel.objects.create(first_name=fn,last_name=ln,age=age,address=address,email=email,phone=phone)
#            messages.success(request,"STUDENT ADDED SUCCESFULLY!!")
#            return redirect("h")
 #           #return HttpResponse("username:"+request.POST.get("first_name")+"<br> lastname:"+request.POST.get("last_name")+"<br> age:"+request.POST.get("age")+"<br> address:"+request.POST.get("address")+"<br> email:"+request.POST.get("email")+"<br> phone:"+request.POST.get("phone"))
#        else:
#            messages.error(request,"Student adding failed!!")
 #           return render(request,"addstu.html",{"form":form_data})

@method_decorator(signin_required,name='dispatch')
class AddStudentMView(View):
    def get(self,request,*args,**kwargs):
        f=StudentMForm()
        return render(request,"addstu.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=StudentMForm(data=request.POST,files=request.FILES)
        if form_data.is_valid(): 
            form_data.save()  
            messages.success(request,"Student-Details Updated Successfully!!")  
            return redirect("h")
        else:
          messages.error(request,"Student adding failed!!")
          return render(request,"addstu.html",{"form":form_data})



@method_decorator(signin_required,name='dispatch')
class ViewStudentView(View):
    def get(self,request,*args,**kwargs):
        res=StudentModel.objects.all()
        return render(request,"viewstu.html",{"data":res}) 


@method_decorator(signin_required,name='dispatch')
class StudentDeleteView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get("id")
        stu=StudentModel.objects.get(id=sid)  
        stu.delete()
        return redirect("viewStudent")

#class StudentEditView(View):
   # def get(self,request,*args,**kwargs):
    #    id=kwargs.get("sid")
    #    stu=StudentModel.objects.get(id=id)
    #    f=AddStudentForm(initial={"first_name":stu.first_name,"last_name":stu.last_name,"age":stu.age,"address":stu.address,"email":stu.email,"phone":stu.phone})
    #    return render(request,"edit.html",{"form":f})
    #def post(self,request,*args,**kwargs):  
    #    form_data=AddStudentForm(data=request.POST)
    #    if form_data.is_valid():
    #        fn=form_data.cleaned_data.get("first_name")
    #        ln=form_data.cleaned_data.get("last_name")
    #        age=form_data.cleaned_data.get("age")
    #        address=form_data.cleaned_data.get("address")
    #        email=form_data.cleaned_data.get("email")
    #        phone=form_data.cleaned_data.get("phone")  
    #        id=kwargs.get("sid")
    #        stu=StudentModel.objects.get(id=id)
     #       stu.first_name=fn
    #        stu.last_name=ln
    #        stu.age=age 
    #        stu.address=address
    #        stu.email=email
    #        stu.phone=phone
    #        stu.save()
    #        messages.success(request,"Student-Details Updated Successfully!!")  
    #        return redirect("viewStudent")
    #    else:
    #        messages.error(request,"Updation Failed!!")
    #        return render(request,"edit.html",{"form":form_data})


@method_decorator(signin_required,name='dispatch')

class StudEditMView(View):
    def get(self,request,*args,**kwargs):
       id=kwargs.get("sid")
       stu=StudentModel.objects.get(id=id)
       f=StudentMForm(instance=stu)
       return render(request,"edit.html",{"form":f})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("sid")
        stu=StudentModel.objects.get(id=id)
        form_data=StudentMForm(data=request.POST,instance=stu,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Student-Details Updated Successfully!!")  
            return redirect("viewstu")
        else:
            messages.error(request,"Updation Failed!!")
            return render(request,"edit.html",{"form":form_data})       



    
    



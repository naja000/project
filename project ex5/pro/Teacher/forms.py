from django import forms
from .models import StudentModel


class AddMarkForm(forms.Form):
    mark1=forms.IntegerField(label="Enter mark of sub1")    
    mark2=forms.IntegerField(label="Enter mark of sub2")        
    mark3=forms.IntegerField(label="Enter mark of sub3")
    mark4=forms.IntegerField(label="Enter mark of sub4")
    def clean(self):
        cleaned_data=super().clean()
        m1=cleaned_data.get("mark1")
        m2=cleaned_data.get("mark2")
        m3=cleaned_data.get("mark3")
        if m1<0:
            msg="Mark less than zero.Invalid Input"
            self.add_error("mark1",msg)
        if m2<0:
            msg="mark less than zero.invalid input"   
            self.add_error("mark1",msg)
        if m3<0:
            msg="mark less than zero.Invalid Input" 
            self.add_error("mark3",msg)    

class AddStudentForm(forms.Form):
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your First name:"}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Last name:"}))
    age=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Age:"}))
    address=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Address:"}))
    email=forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Email:"}))
    phone=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your phone Number:"}))



    def clean(self):
        cleaned_data=super().clean()
        fname=cleaned_data.get("first_name")
        lname=cleaned_data.get("last_name")
        age=cleaned_data.get("age")
        phone=str(cleaned_data.get("phone"))
        if fname==lname:
        #msg="First name cannot be equal to Last name.Invalid"
            self.add_error("last_name","first name and last name are same")
        if age<5:
            self.add_error("age","Age is Invalid")
        if len(phone)!=10:
            self.add_error("phone","digits must be 10") 

class StudentMForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields="__all__"
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"First Name"}),
            "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Lat Name"}),
            "age":forms.NumberInput(attrs={"class":"form-control","placeholder":"age"}),
            "address":forms.Textarea(attrs={"class":"form-control","placeholder":"address"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"email"}),
            "phone":forms.NumberInput(attrs={"class":"form-control","placeholder":"phone"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),

        
            
        }
    def clean(self):
        cleaned_data=super().clean()
        fname=cleaned_data.get("first_name")
        lname=cleaned_data.get("last_name")
        age=cleaned_data.get("age")
        phone=str(cleaned_data.get("phone"))
        
        
        if fname==lname:    
            self.add_error("last_name","first name and last name are same")
        if age<5:
            self.add_error("age","Age is Invalid")
        if len(phone)!=10:
            self.add_error("phone","digits must be 10") 


              





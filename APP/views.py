from django.shortcuts import render, redirect
from . models import UserPersonalModel
from . forms import UserPersonalForm, UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np
import joblib


def Landing_1(request):
    return render(request, '1_Landing.html')

def Register_2(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')  # Get the username from the form
            form.save()
            messages.success(request, f'Account was successfully created. {user}')  # Use an f-string to concatenate the message
            return redirect('Login_3')

    context = {'form': form,'messages':messages}
    return render(request, '2_Register.html', context)


def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)

def Home_4(request):
    return render(request, '4_Home.html')

def Teamates_5(request):
    return render(request,'5_Teamates.html')

def Domain_Result_6(request):
    return render(request,'6_Domain_Result.html')

def Problem_Statement_7(request):
    return render(request,'7_Problem_Statement.html')
    

def Per_Info_8(request):
    if request.method == 'POST':
        fieldss = ['firstname','lastname','age','address','phone','city','state','country']
        form = UserPersonalForm(request.POST)
        if form.is_valid():
            print('Saving data in Form')
            form.save()
        return render(request, '4_Home.html', {'form':form})
    else:
        print('Else working')
        form = UserPersonalForm(request.POST)    
        return render(request, '8_Per_Info.html', {'form':form})
    
Model = joblib.load('C:/Users/SPIRO25/Desktop/PROJECT/project/ITPML22 - CIRRHOSIS/deploy/PROJECT/APP/CIRRHOSIS.pkl')
Model1 = joblib.load('C:/Users/SPIRO25/Desktop/PROJECT/project/ITPML22 - CIRRHOSIS/deploy/PROJECT/APP/KIDNEY.pkl')
def Deploy_9(request): 
    #CIRRHOSIIS
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features, dtype=object)]
        print(final_features)
        prediction = Model.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(f'output{output}')
        if output == 0:
            return render(request, '9_Deploy.html', {"prediction_text":"THE                                                                                                                                   DISEASE MIGHT NOT INFECT IN THIS CONDITION"})
        elif output == 1:
            return render(request, '9_Deploy.html', {"prediction_text":"THE CIRRHOSIS DISEASE MIGHT INFECT IN THIS CONDITION"})
    else:
        return render(request, '9_Deploy.html')


def Per_Database_10(request):
    models = UserPersonalModel.objects.all()
    return render(request, '10_Per_Database.html', {'models':models})
    
def deploy(request): 
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features, dtype=object)]
        print(final_features)
        prediction = Model1.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(f'output{output}')
        if output == 0:
            return render(request, 'deploy.html', {"prediction_text":"THE KIDNEY DISEASE MIGHT NOT AFFECT IN THIS CONDITION"})
        elif output == 1:
            return render(request, 'deploy.html', {"prediction_text":"THE KIDNEY DISEASE MIGHT  AFFECT IN THS CONDITION"})
    else:
        return render(request, 'deploy.html')



def Logout(request):
    logout(request)
    return redirect('3_Login')

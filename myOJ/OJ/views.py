from datetime import datetime
from json import load
from multiprocessing import context
from re import template
from unittest import loader
from django.shortcuts import render,redirect,get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .forms import SubmitedCode
from .compilingFunc import compiler
from .forms import NewUserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .models import Problem,Test_cases,Submission, User_score

def problems(request):
    problem_list = Problem.objects.all()
    template = loader.get_template('OJ/problems.html')
    score = User_score.objects.get(pk = request.user.id).score
    context = {'problem_list': problem_list,'score':score}
    return HttpResponse(template.render(context,request))

def problem_details(request, question_name):
    problem = get_object_or_404(Problem,prob_name=question_name)
    if request.method == 'POST':
        form = SubmitedCode(request.POST)
        if form.is_valid():
            code = form.cleaned_data['solution']
            # testcases = Test_cases.objects.filter(probId=problem.pk)
            # print(testcases)
            # if(compiler(code)):
            #     print("accepted")
            # else:
            #     print("Wrong Answer")
            # print(compiler(code,problem.pk))
            # print(request.user.username)
            # user = User.objects.get()
            submission = Submission()
            submission.user_Id = request.user
            submission.probId = problem
            # submission.timestrap = datetime.now
            submission.verdict = compiler(code,problem.pk)    
            submission.save()
            try: 
                userscore =User_score.objects.get(user_Id__pk= request.user.id )
                userscore.score = userscore.score + problem.score
                userscore.save()
            except:
                userscore = User_score(user_Id=request.user,score = problem.score)    
                userscore.save()
    else:
        form = SubmitedCode()
    template = loader.get_template('OJ/detail.html')
    context = {'problem':problem,'form':form}
    return HttpResponse(template.render(context,request))

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("OJ:problem")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="OJ/register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}.")
                return redirect('OJ:problem')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="OJ/login.html", context={"login_form":form})

def user_submission(request):
    submission_list = Submission.objects.filter(user_Id =request.user)

    template = loader.get_template('OJ/submission.html')
    context = {'submission_list': submission_list}
    return HttpResponse(template.render(context,request))
    
def user_logout(request):
    logout(request)
    return redirect('OJ:login')
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpRequest
from .forms import formModels
from .models import dataFormModels


def createMessageView(request: HttpRequest):
    if request.method == 'POST':
        myForm = formModels(request.POST)
        if myForm.is_valid():
            myForm.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('forms:Home')
        else:
            messages.error(request, 'Erro ao enviar mensagem. Verifique os campos.')
            context = {"form": myForm}
            return render(request, 'homePage/index.html', context)
    
    context = {
        "form": formModels()
    }
    return render(request, 'homePage/index.html', context)

def getAllMessagesView(request):
    context = {
        "forms":dataFormModels.objects.all()
    }
    return render(request, 'adminPanel/adminPanel.html', context)

def deleteMessageByIdView(request:HttpRequest, id):
    form = get_object_or_404(dataFormModels, id=id)
    form.delete()
    return redirect('forms:mensagens')

def editMessageByIdView(request: HttpRequest, id):
    form_instance = get_object_or_404(dataFormModels, id=id)
    
    if request.method == "POST":
        form_obj = formModels(request.POST, instance=form_instance)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('forms:mensagens')
    else:
        form_obj = formModels(instance=form_instance)
    
    context = {
        'form': form_obj
    }
    return render(request, 'editForm/editMessage.html', context)

def loginPage(request):
    return render(request, 'login/login.html')

def registerPage(request):
    return render(request, 'login/register.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm


# Create your views here.



def home(request):

    template_name = 'main/home.html'
    if request.method == 'POST':

        form = ContactForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            messages.info(request, f"Your message has been sended.")
            return redirect('main:homepage')
        else:
            messages.error(request, "Invalid Form.")
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            for field, items in form.errors.items():
                for item in items:
                    messages.error(request, f"{field}: {item}")
    else:
        
        form = ContactForm()
        context = {
            "title": "Contact",
            "body": "Body: HELLO WORLD!!! How to Contact ME",
            "content": "*Email require*",
            "form": form
        }
    return render(request, template_name, context)


def projects(request):

    template_name = 'main/projects.html'
    context = {
        "title": "Projects",
        "body": "Body: My Projects"
    }
    return render(request, template_name, context)
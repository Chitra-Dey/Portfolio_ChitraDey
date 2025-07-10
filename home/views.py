from django.shortcuts import render , HttpResponse , redirect
from .forms import ContactForm
from .models import Project
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for contacting me! I’ll reach back to you soon.")
            return redirect('home')  # make a thank-you page or use messages
    else:
        form = ContactForm()
    projects = Project.objects.all().order_by('-date_added')
    return render(request, 'home/index.html', {'form': form , 'projects': projects})
    return render(request, 'home/index.html')
def myform(request):
    #return HttpResponse("This is my formpage (/)")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # make a thank-you page or use messages
    else:
        form = ContactForm()

    return render(request, 'home/index.html', {'form': form})


# def portfolio_view(request):
#     projects = Project.objects.all().order_by('-date_added')  # newest first
#     return render(request, 'home/index.html', {'projects': projects})

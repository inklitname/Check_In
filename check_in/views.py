from django.shortcuts import render
from .forms import UsersForm


def check_in(request):
    form = UsersForm(request.POST or None)

    if request.method == "POST":
        print (request.POST)

        new_form = form.save()


    return render(request, 'check_in/check_in.html', locals())
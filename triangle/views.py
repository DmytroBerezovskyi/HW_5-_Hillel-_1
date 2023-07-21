from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .forms import Triangls
from .forms import Person
from .models import Person_model



def triangle(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Triangls(request.POST)
        # check whether it's valid:
        if form.is_valid():
            katet_1 = form.cleaned_data["katet_1"]
            katet_2 = form.cleaned_data["katet_2"]
            if katet_2 > 0 and katet_1 > 0:
                gip = round((((katet_1) ** 2) + ((katet_2) ** 2)) ** 0.5, 3)
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return render(request, "form.html", {"form": form, "gip": gip})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Triangls()

    return render(request, "form.html", {"form": form})



# class DetailView(generic.DetailView):
#     model = Person_model
#     template_name = 'detail.html'
#
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Person_model.objects.filter()


def person(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Person(request.POST)
        # check whether it's valid:
        person_1 = get_object_or_404(Person_model, first_name_1="Oleg1")
        if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                # first_name_1 = get_object_or_404(Person_model, first_name_1=form.cleaned_data["first_name_1"])
                # print(first_name_1)
            return render(request, "detail.html", {"person_1": person_1})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Person()

    return render(request, "person_form.html", {"form": form})

# def detail(request):
#     first_name_1 = get_object_or_404(Person_model, id=1)
#     return render(request, 'detail.html', {'first_name_1': first_name_1})

def create_person(request):
    if request.method == "POST":
        form = Person(request.POST)
        if form.is_valid():
            if Person_model.objects.filter(first_name_1=form.cleaned_data.get("first_name_1")) and Person_model.objects.filter(last_name_1=form.cleaned_data.get("last_name_1")) and Person_model.objects.filter(email_1=form.cleaned_data.get("email_1")):
                raise ValidationError("User already registered")
            else:
                person_1 = Person_model.objects.create(first_name_1=form.cleaned_data["first_name_1"], last_name_1=form.cleaned_data["last_name_1"], email_1=form.cleaned_data["email_1"])
        return render(request, "create_person.html", {"form": form})

    else:
        form = Person()
    # first_name_1 = get_object_or_404(Person_model, id=1)
    # print(first_name_1)
    return render(request, "create_person.html", {"form": form})



def update_person(request):
    person = get_object_or_404(Person_model, first_name_1="Oleg")
    if request.method == "POST":
        form = Person(request.POST)
        if form.is_valid():
            person.first_name_1 = form.cleaned_data["first_name_1"]
            person.save()
            #person_1 = Person_model.objects.update(first_name_1=form.cleaned_data["first_name_1"], last_name_1=form.cleaned_data["last_name_1"], email_1=form.cleaned_data["email_1"])
        return render(request, "update_person.html", {"form": form})

    else:
        form = Person(initial={"firs_name_1": person.first_name_1})
    # first_name_1 = get_object_or_404(Person_model, id=1)
    # print(first_name_1)
    return render(request, "update_person.html", {"form": form})

class QuestionDetailView(generic.DetailView):
    model = Person_model
    template_name = "detail.html"
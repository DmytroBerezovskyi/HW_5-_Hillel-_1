from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .forms import Triangls
from .forms import PersonModelForm
from .models import Person


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


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "latest_person_list"
    paginate_by = 5

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Person.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:20]


class PersonDetailView(generic.DetailView):
    model = Person
    template_name = "detail.html"


class PersonResultsView(generic.DetailView):
    model = Person
    template_name = "results.html"


def create_person(request):
    if request.method == "POST":
        form = PersonModelForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")

            # In case if user already registered, will redirect to person:detail of user
            if Person.objects.filter(first_name=first_name, last_name=last_name, email=email).exists():
                person = get_object_or_404(Person, first_name=first_name, last_name=last_name, email=email)
                return redirect(reverse("person:detail", args=(person.id,)))

            person = form.save(commit=False)
            person.pub_date = datetime.now()
            person.save()
            return redirect(reverse("person:detail", args=(person.id,)))
    else:
        form = PersonModelForm(initial={"pub_date": datetime.now()})
    return render(request, "person_form.html", {"form": form})


def update_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonModelForm(request.POST, instance=person)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            # In case if user have same detail, will be ValidationError
            if Person.objects.filter(first_name=first_name, last_name=last_name, email=email).exists():
                raise ValidationError("Person already have same datail")
            form.save()
            return redirect(reverse("person:detail", args=(person.id,)))
    else:
        form = PersonModelForm(instance=person)
    return render(request, "person_form.html", {"form": form, "person": person})


def delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person = Person.objects.get(id=pk)
    person.delete()
    return redirect("person:index")

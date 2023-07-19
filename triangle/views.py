from django.shortcuts import render
from .forms import Triangls


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

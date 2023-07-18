from django.shortcuts import render

# Create your views here.


def triangle(request):
    if request.method == "POST":
        fside = request.POST.get("fside")
        sside = request.POST.get("sside")
        if fside != "" and sside != "":
            gip = round(((int(fside) ** 2) + (int(sside) ** 2)) ** 0.5, 3)
            return render(request, "results.html", {"gip": gip})
    return render(request, "triangle.html")

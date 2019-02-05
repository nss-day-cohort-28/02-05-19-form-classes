from django.shortcuts import render
from .forms import DogForm
# from .models import *

def index(request):
  return render(request, "minisite/index.html")

def dogNew(request):
  if request.method == "GET":
    print("Fetching the form")
    dog_form = DogForm()
    return render(request, 'minisite/dog_form.html', {"form": dog_form.as_p()})

  if request.method == "POST":
    print("Form stuff!", request.POST)
    # make sure the form inputs are kosher
    form = DogForm(request.POST)
    if form.is_valid():
      cleaned = form.cleaned_data
      cleaned["dog_name"]

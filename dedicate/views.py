from django.shortcuts import render
import subprocess

# Create your views here.


def home_page(request):
    return render(request, "home.html")


def extract(request):
    command = 'unzip server.zip'
    output = subprocess.check_output(command, shell=True)
    print(output.decode('utf-8'))

    return render(request, "home.html")


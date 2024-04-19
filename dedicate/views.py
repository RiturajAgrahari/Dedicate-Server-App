from django.shortcuts import render
import subprocess

# Create your views here.


def home_page(request):
    return render(request, "home.html")


def extract(request):
    command = 'unzip media/server/server.zip -d DedicateServers/server001'
    output = subprocess.check_output(command, shell=True)
    print(output.decode('utf-8'))

    return render(request, "home.html")


def list_directory(request):
    command = 'ls'
    output = subprocess.check_output(command, shell=True)
    print(output.decode('utf-8'))

    return render(request, "home.html")


def enable_execution(request):
    command = 'chmod +x DedicateServers/server001/LinuxServer/LinuxDedicateTeot.x86_64'
    output = subprocess.check_output(command, shell=True)
    print(output.decode('utf-8'))

    return render(request, "home.html")


def execute(request):
    command = 'nohup ./DedicateServers/server001/LinuxServer/LinuxDedicateTeot.x86_64 &'
    output = subprocess.check_output(command, shell=True)
    print(output.decode('utf-8'))


    return render(request, "home.html")


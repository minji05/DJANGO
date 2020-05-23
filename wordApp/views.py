from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):

    computer = random.randint(1,3)
    data = ["", "Rock", "Scissor", "Paper"]
    print("\n1.Rock 2.scissor 3. Paper")
    print("1-3 Number input?")
    text = request.GET['fulltext']
    return render(request, 'result.html', {'full': text, 'computer' : computer})


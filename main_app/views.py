from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'index.html', {'treasures': treasures})


class Treasure:
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location


treasures = [
    Treasure('Gold nuggets', 100, 'gold', 'silicon valley'),
    Treasure('silver nuggets', 50, 'silver', 'london'),
    Treasure('coffee gold', 100, 'gold', 'silicon valley')
]

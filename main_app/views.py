from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'index.html', {'treasures': treasures})


class Treasure:
    def __init__(self, name, value, material, location, image_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.image_url = image_url


treasures = [
    Treasure(' Coffee can', 100.00, ' Brass', ' silicon valley', 'http://139.59.68.161/media/treasure_images/Coffee%20Can/treasuregram-brand-coffee-can.png'),
    Treasure(' Gold nuggets', 50.00, ' Gold', 'london', 'http://139.59.68.161/media/treasure_images/Gold%20nugget/treasuregram-brand-gold-nugget.png'),
    Treasure(' Arrow head', 0.00, ' Iron', ' Germany', 'http://139.59.68.161/media/treasure_images/Arrowhead/treasuregram-brand-arrowhead.png'),
    Treasure(' Fools gold', 120.00, 'German silver', 'USA', 'http://139.59.68.161/media/treasure_images/Gold%20nugget/monkey_sitting_tall.png')
]

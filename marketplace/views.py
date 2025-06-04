from django.shortcuts import render
from .models import Item
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def listing(request):
    """
    Render the marketplace listing page.
    """
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'marketplace/listing.html', context)

@login_required
def upload(request):
    """
    Render the marketplace upload page.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        semester = request.POST.get('semester')
        image = request.FILES.get('image')
        user = request.user
        if name and description and price and image and user:
            item = Item(
                user=user,
                name=name,
                description=description,
                price=price,
                image=image,
                semester=semester if semester else 'none',
            )
            item.save()
            return redirect('listing')
        else:
            print("Error: All fields are required.")
            return render(request, 'marketplace/upload.html', {'error': 'All fields are required.'})
    return render(request, 'marketplace/upload.html')
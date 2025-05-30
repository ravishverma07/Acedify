from django.shortcuts import render

def listing(request):
    """
    Render the marketplace listing page.
    """
    return render(request, 'marketplace/listing.html')

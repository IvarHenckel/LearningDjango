from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm
from.models import Product
# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST or None) # IH ??
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     if request.method == "POST":
#         # The first time the url is loaded there will be no POST, it's only when we hit our save button that we actually POST
#         my_new_title = request.POST.get('title')
#         # If we had all fields we could save the product with 
#         # Product.objects.create(title=my_new_title, ....)
#     # We also want to check that the data that is posted is valid data!
#     context = {}
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     my_form  = RawProductForm() # default
#     if request.method == "POST":
#         my_form  = RawProductForm(request.POST) # This will create a RawProductForm based on our POST request
#         # When doing it this way Django includes a lot of validation. It checks the RawProductForm model and requires that the data we get is correct, it even outputs validation warnings to the view when we use form.as_p
#         # Not sure how this works forms.Form as input to the classis probably very relevant
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)


#IH: is *args always optional??
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # } This way of doing things is not that flexible, adding things in the model requires changes in the view
    context = {
        'object': obj
    }# Now we send the object forward from the db in a flexible way 
    # Hmm this works but shouldn't it actually search for the template in <root>/templates/ instead of products/templates/products/product_detail.html ?
    # It actually tries multiple places. You can see places in the debg message with incorrect.
    # Seems like it tries with different BASE_DIR (see settings.py)
    # We can place all templates under <root>/templates but this is a more modular way especially good if we want to use products in another project.
    return render(request, "products/product_detail.html", context)

def render_initial_data(request):
    initial_data = {
        'title': "Not showing title"
    }
    obj = Product.objects.get(id=5)
    print('here we go')
    form  = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    # We hand the product form data, partly with an  object of the model
    # and partly with a dict as initial data.
    # If I understand correctly we create the form from the POST if there is one.
    # Otherwise we go with initial data
    # How come this doesn't change our value in the database to "Not showing title" unless we click save?
    # Maybe we need to POST the ProductForm for saving to occur?
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)

def dynamic_lookup_view(request, id):
    #obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object":obj
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    #POST request
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)
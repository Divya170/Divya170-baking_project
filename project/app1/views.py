from django.shortcuts import render, redirect
from .models import Product, AboutContent, Order, table
from app1.forms import OrderForm, ContactForm
from django.core.mail import send_mail

# Home Page View: Displays Banner, About Section, and Product Gallery
def home_view(request):
    # Fetch products for the gallery
    products = Product.objects.all()  # Get all products from the database
    
    # Fetch about section content
    about_content = AboutContent.objects.first()  # Get the first (or only) About content object
    
    # Render home page with products and about section
    return render(request, 'home.html', {'products': products, 'about_content': about_content})

# Product Gallery View: Displays all products in a gallery
def product_gallery(request):
    # Fetch all products for the gallery
    products = Product.objects.all()
    return render(request, 'product_gallery.html', {'products': products})

# Order Form View: Displays the order form and handles submission
def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Save the order to the database
            form.save()
            return redirect('thank_you')  # Redirect to a thank-you page after successful order
    else:
        form = OrderForm()  # Initialize the empty form
    
    # Render order form page with form context
    return render(request, 'order_form.html', {'form': form})

# About Section View: Displays content for the About section
def about_view(request):
    # Fetch about section content
    about_content = AboutContent.objects.first()  # Get the first About content object
    return render(request, 'about.html', {'about_content': about_content})

# Contact Form View: Displays the contact form and handles email submission
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send the contact email
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                ['your_email@example.com'],  # Replace with your email address
            )
            # Render contact thanks page after submission
            return render(request, 'contact_thanks.html')
    else:
        form = ContactForm()  # Initialize the empty form

    # Render contact form page with form context
    return render(request, 'contact_form.html', {'form': form})

# Example Thank You Page after Order Submission
def thank_you_view(request):
    return render(request, 'thank_you.html')

# Feedback Form View: Saves feedback from users
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mn']
        address = request.POST['address']
        mail = request.POST['email']
        feedback = request.POST['fb']
        table.objects.create(name=name, mn=mobile, address=address, email=mail, feedback=feedback)
    
    return render(request, "index.html")

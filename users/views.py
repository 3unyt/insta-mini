# users/views.py
from .forms import CustomUserCreationForm
from django.views.generic import DetailView
from django.urls import reverse_lazy 
from django.views import generic
from .models import CustomUser

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserDetailView(DetailView):       # video8.2
    model = CustomUser
    template = 'user_detail.html'
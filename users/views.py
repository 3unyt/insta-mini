# users/views.py
from .forms import CustomUserCreationForm
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy 
from django.views import generic
from .models import CustomUser, UserConnection

from annoying.decorators import ajax_request
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserDetailView(LoginRequiredMixin, generic.DetailView):       # video8.2
    model = CustomUser
    login_utl = 'login'
    # template file: ./templates/users/customuser_detail.html

@ajax_request
def toggleFollow(request):
    current_user = CustomUser.objects.get(pk=request.user.pk)
    follow_user_pk = request.POST.get('follow_user_pk')
    follow_user = CustomUser.objects.get(pk=follow_user_pk)

    try:
        if current_user != follow_user:
            if request.POST.get('type') == 'follow':
                connection = UserConnection(creator=current_user, following=follow_user)
                connection.save()
            elif request.POST.get('type') == 'unfollow':
                UserConnection.objects.filter(creator=current_user, following=follow_user).delete()
            result = 1
        else:
            result = 0
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'type': request.POST.get('type'),
        'follow_user_pk': follow_user_pk
    }
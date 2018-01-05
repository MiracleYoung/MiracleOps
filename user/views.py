from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserCreateForm, UserLoginForm
from .models.user import User
from common.utils import gen_token

class UserLoginView(FormView):
    template_name = "user/login.html"
    form_class = UserLoginForm

    def form_invalid(self, form):
        if form.is_valid():
            u = User.objects.get(email=form.email)
            if u.check_password(form.password) and u.is_authenticated:
                # TODO
                # create token
                # add token to request.cookie
                # return redirect(self.get_success_url())
                pass




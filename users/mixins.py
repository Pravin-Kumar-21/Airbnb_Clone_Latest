from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http.response import HttpResponseRedirect


class LoggedOutOnlyView(UserPassesTestMixin):
    permission_denied_message = "Erorr 404 Page Does Not Exist"

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("core:home")

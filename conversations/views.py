from django.db.models import Q
from django.shortcuts import render
from users import models as user_models
from . import models
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView


def go_converstion(request, a_pk, b_pk):
    user_one = user_models.User.objects.get(pk=a_pk)
    user_two = user_models.User.objects.get(pk=b_pk)
    if user_one is not None and user_two is not None:
        try:
            conversation = models.Conversation.objects.get(
                Q(participants=user_one) & Q(participants=user_two)
            )
        except models.Conversation.DoesNotExist:
            conversation = models.Conversation.objects.create()
            conversation.participants.add(user_one, user_two)
        return redirect(reverse("conversations:detail", kwargs={"pk": conversation.pk}))


class ConversationDetailView(DetailView):
    model = models.Conversation
    template_name = "conversations/conversation_detail.html"


class UserProfileView(DetailView):
    model = user_models.User
    context_object_name = "user_obj"

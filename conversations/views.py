from django.db.models import Q
from django.shortcuts import render
from users import models as user_models
from . import models
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, View
from django.http import Http404
from . import models, forms


def go_conversation(request, a_pk, b_pk):
    user_one = user_models.User.objects.get(pk=a_pk)
    print(user_one)
    user_two = user_models.User.objects.get(pk=b_pk)
    print(user_two)
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

    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        if not conversation:
            raise Http404()
        return render(
            self.request,
            "conversations/conversation_detail.html",
            {"conversation": conversation},
        )

    def post(self, *args, **kwargs):
        message = self.request.POST.get("Message", None)
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        if not conversation:
            raise Http404()
        if message is not None:
            models.Message.objects.create(
                message=message, user=self.request.user, conversation=conversation
            )
        return redirect(reverse("conversations:detail", kwargs={"pk": pk}))


class UserProfileView(DetailView):
    model = user_models.User
    context_object_name = "user_obj"

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from .models import Group, GroupMember
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.contrib import messages  # 34
from . import models

# Create your views here.

# VIEW FOR CREATING A GROUP
class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Group


# DETAIL VIEW OF THE GROUP LIKE POSTS
class SingleGroup(generic.DetailView):
    model = Group


# LIST OF GROUPS
class ListGroup(generic.ListView):
    model = Group


# JoinGroup
class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # 35
        return reverse("groups:single", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        # 36
        group = get_object_or_404(Group, slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(group=group, user=self.request.user)
        except IntegrityError:
            messages.warning(self.request, "Already a member of this group")
        else:
            messages.success(self.request, "You are now a member!")

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:
            membership = GroupMember.objects.filter(
                user=self.request.user, group__slug=self.kwargs.get("slug")
            ).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request, "Sorry you are not in this group")
        else:
            membership.delete()
            messages.success(self.request, "You have left the group!!")
        return super().get(request, *args, **kwargs)

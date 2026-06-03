from django.contrib import admin
from .models import Event, Participant, Team

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "location", "price")
    search_fields = ("name", "location")
    list_filter = ("date", "location")


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "age", "event")
    search_fields = ("name", "email")
    list_filter = ("event",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "color")
    search_fields = ("name", "color")
    filter_horizontal = ("participants",)
from django.contrib import admin

from workouts.models import Workout, Lap


class LapInline(admin.TabularInline):
    model = Lap
    extra = 0


class WorkoutAdmin(admin.ModelAdmin):
    inlines = [LapInline, ]


class LapAdmin(admin.ModelAdmin):
    pass


admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Lap, LapAdmin)

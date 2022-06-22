from django.contrib import admin
from .models import Update, tdm, tdmtournament, classic, classictournament

class updates(admin.ModelAdmin):
    list_display = ('title', 'description', 'time')
admin.site.register(Update, updates)

class TEAMDEATHMATCH(admin.ModelAdmin):
    list_display = ("name", "email", "mobile_no", "pubg_id", "time")
    list_filter = ("name", "time")
admin.site.register(tdm, TEAMDEATHMATCH)

class TDMTournament(admin.ModelAdmin):
    list_display = ('time', )
admin.site.register(tdmtournament, TDMTournament)

class CLASSICMATCH(admin.ModelAdmin):
    list_display = ("name", "email", "mobile_no", "pubg_id", "time")
    list_filter = ("name", "time")
admin.site.register(classic, CLASSICMATCH)

class ClassicTournament(admin.ModelAdmin):
    list_display = ('time', )
admin.site.register(classictournament, ClassicTournament)
from django.contrib import admin
from hc.models import Sprint

class SprintAdmin(admin.ModelAdmin):
    list_display = [
        "id", "index", "name", "totalPoints", "pointsMerged", "extraDeploys", "delayed"
    ]
    search_fields = ["id", "index", "name"]

admin.site.register(Sprint, SprintAdmin)

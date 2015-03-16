from django.contrib import admin

import nfsmain.models

# Register your models here.
admin.site.register(nfsmain.models.Organisation)
admin.site.register(nfsmain.models.Speech)
admin.site.register(nfsmain.models.Interview)
admin.site.register(nfsmain.models.Event)
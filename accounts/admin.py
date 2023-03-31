from django.contrib import admin
from .models import User, mousaqe, transltor,payer
from .models import Video,dasboardvedio,uploadtranlate
from .models import file_after_tranlated
from .models import earas,citys,mousaqeProfile,comments

admin.site.register(file_after_tranlated)
admin.site.register(Video)
admin.site.register(User)
admin.site.register(transltor)
admin.site.register(mousaqe)
admin.site.register(payer)
admin.site.register(dasboardvedio)
admin.site.register(uploadtranlate)
admin.site.register(mousaqeProfile)
admin.site.register(comments)




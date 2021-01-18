from django.contrib import admin
from .models import contestModel
from .models import submissionModel
from .models import User
from contest.models import CustomUser
# Register your models here.
admin.site.register(contestModel)
admin.site.register(submissionModel)
admin.site.register(CustomUser)
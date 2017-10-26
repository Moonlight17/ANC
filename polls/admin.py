from django.contrib import admin

from .models import Spisok
from .models import TitleList
from .models import LaunchOperationTypes
from .models import EventTypes
from .models import PayloadClasses
from .models import DocSources




admin.site.register(Spisok)
admin.site.register(TitleList)
admin.site.register(LaunchOperationTypes)
admin.site.register(EventTypes)
admin.site.register(PayloadClasses)
admin.site.register(DocSources)
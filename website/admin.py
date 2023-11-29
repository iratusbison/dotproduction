from django.contrib import admin

from website.models import Service , Product , About , Experimental_Projects


admin.site.register(Service)

admin.site.register(Product)

admin.site.register(About)

admin.site.register(Experimental_Projects)
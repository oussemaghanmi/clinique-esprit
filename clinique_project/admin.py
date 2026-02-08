kfrom django.contrib import admin

admin.site.site_header = "Administration de la Clinique"
admin.site.site_title = "Administration de la Clinique"
admin.site.index_title = "Espace réservé aux administrateurs de notre clinique"


class CliniqueAdminSite(admin.AdminSite):
    site_header = admin.site.site_header
    site_title = admin.site.site_title
    index_title = admin.site.index_title

    class Media:
        css = {
            "all": ("css/admin_custom.css",)
        }


# Remplace le site admin global par celui-ci
admin.site.__class__ = CliniqueAdminSite


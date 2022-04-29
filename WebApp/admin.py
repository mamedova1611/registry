from django.contrib import admin
from .models import VHD, Predpriyatie, PB, PVD, Bank, BS, FO, FP, NK


class VHD_Admin(admin.ModelAdmin):
    list_display = ['id', 'name']


class Predpriyatie_Admin(admin.ModelAdmin):
    list_display = ['bin_id', 'full_name', 'address', 'fio_ruk', 'phone', 'date', 'vid_hoz_d', 'form_org']
    list_filter = ['form_org__name']
    search_fields = ['bin_id', 'full_name', 'vid_hoz_d__name']
    date_hierarchy = 'date'


class PB_Admin(admin.ModelAdmin):
    list_display = ['bin_pb', 'bank', 'schet']
    list_filter = ['bank__name']


class PVD_Admin(admin.ModelAdmin):
    list_display = ['bin_pvd', 'vid_hoz_d']
    list_filter = ['vid_hoz_d__name']


class Bank_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address']


class BS_Admin(admin.ModelAdmin):
    list_display = ['kod', 'name']


class FO_Admin(admin.ModelAdmin):
    list_display = ['id', 'name']


class FP_Admin(admin.ModelAdmin):
    list_display = ['bin_fp', 'kvartal', 'date', 'bs', 'summa', 'priznak']
    list_filter = ['priznak']


class NK_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address']


admin.site.register(VHD, VHD_Admin)
admin.site.register(Predpriyatie, Predpriyatie_Admin)
admin.site.register(PB, PB_Admin)
admin.site.register(PVD, PVD_Admin)
admin.site.register(Bank, Bank_Admin)
admin.site.register(BS, BS_Admin)
admin.site.register(FO, FO_Admin)
admin.site.register(FP, FP_Admin)
admin.site.register(NK, NK_Admin)

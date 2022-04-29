from django.urls import path, include


from WebApp.views import *
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
    path('base/', basic, name='base'),
    path('vhd/', VHDListView.as_view(), name='vhd'),
    path('vhd/add/', VHDFormView.as_view(), name='vhd_form'),
    path('vhd/edit/<int:pk>', VHDEditFormView.as_view(), name='vhd_form_edit'),
    path('vhd/del/<int:pk>', VHDDelFormView.as_view(), name='vhd_form_del'),
    path('fo/', FOListView.as_view(), name='fo'),
    path('nk/', NKListView.as_view(), name='nk'),
    path('nk/add/', NKFormView.as_view(), name='nk_form'),
    path('nk/edit/<int:pk>', NKEditFormView.as_view(), name='nk_form_edit'),
    path('nk/del/<int:pk>', NKDelFormView.as_view(), name='nk_form_del'),
    path('bank/', BankListView.as_view(), name='bank'),
    path('bank/add/', BankFormView.as_view(), name='bank_form'),
    path('bank/edit/<int:pk>', BankEditFormView.as_view(), name='bank_form_edit'),
    path('bank/del/<int:pk>', BankDelFormView.as_view(), name='bank_form_del'),
    path('predpriyatie/', PredpriyatieListView.as_view(), name='predpriyatie'),
    path('predpriyatie/add/', PredpriyatieFormView.as_view(), name='predpriyatie_form'),
    path('predpriyatie/edit/<int:pk>', PredpriyatieEditFormView.as_view(), name='predpriyatie_form_edit'),
    path('predpriyatie/del/<int:pk>', PredpriyatieDelFormView.as_view(), name='predpriyatie_form_del'),
    path('pb/', PBListView.as_view(), name='pb'),
    path('pb/add/', PBFormView.as_view(), name='pb_form'),
    path('pb/edit/<int:pk>', PBEditFormView.as_view(), name='pb_form_edit'),
    path('pb/del/<int:pk>', PBDelFormView.as_view(), name='pb_form_del'),
    path('pvd/', PVDListView.as_view(), name='pvd'),
    path('bs/', BSListView.as_view(), name='bs'),
    path('bs/add/', BSFormView.as_view(), name='bs_form'),
    path('bs/edit/<int:pk>', BSEditFormView.as_view(), name='bs_form_edit'),
    path('bs/del/<int:pk>', BSDelFormView.as_view(), name='bs_form_del'),
    path('fp/', FPListView.as_view(), name='fp'),
    path('fp/add/', FPFormView.as_view(), name='fp_form'),
    path('fp/edit/<int:pk>', FPEditFormView.as_view(), name='fp_form_edit'),
    path('fp/del/<int:pk>', FPDelFormView.as_view(), name='fp_form_del'),
    path('guery1/', Query1View.as_view(), name='q1'),
    path('guery2/', Query2View.as_view(), name='q2'),
    path('guery3/', Query3View.as_view(), name='q3'),
    path('guery4/', Query4View.as_view(), name='q4'),
    path('guery5/', Query5View.as_view(), name='q5'),
    path('report1/', Report1View.as_view(), name='r1'),
    path('report2/', Report2View.as_view(), name='r2'),
    path('report3/', Report3View.as_view(), name='r3'),
    path('hp1/', HP1View.as_view(), name='hp1'),
    path('hp2/', HP2View.as_view(), name='hp2'),
    path('hp3/', HP3View.as_view(), name='hp3'),
    path('hp3/age', HP31View.as_view(), name='hp3_1'),
    # path('export_predpriyatie_xls/', export_predpriyatie_xls)
]

from datetime import date

import xlwt as xlwt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic, View

from WebApp.forms import VHD_Form, NK_Form, Bank_Form, Predpriyatie_Form, PB_Form, BS_Form, FP_Form
from WebApp.models import VHD, Predpriyatie, NK, Bank, FO, PB, PVD, BS, FP


def index(request):
    companies = Predpriyatie.objects.all()
    nk = NK.objects.all()
    banki = Bank.objects.all()

    return render(request, "index.html", {"companies": companies, "nk": nk, "banki": banki})


def basic(request):
    return render(request, "base.html")


class VHDListView(generic.ListView):
    model = VHD
    template_name = 'WebApp/vhd.html'
    context_object_name = 'vhd'


class VHDFormView(View):
    def get(self, request):
        vhd_form = VHD_Form()
        return render(request, 'WebApp/vhd_form.html', {'vhd_form': vhd_form})

    def post(self, request):
        vhd_form = VHD_Form(request.POST)
        if vhd_form.is_valid():
            VHD.objects.create(**vhd_form.cleaned_data)
            return render(request, "base.html")
        return render(request, 'WebApp/vhd_form.html', {'vhd_form': vhd_form})


class VHDEditFormView(View):
    def get(self, request, pk):
        vhd = VHD.objects.get(pk=pk)
        vhd_form = VHD_Form(instance=vhd)
        return render(request, 'WebApp/vhd_edit.html', {'vhd_form': vhd_form, 'vhd_id': pk})

    def post(self, request, pk):
        vhd = VHD.objects.get(pk=pk)
        vhd_form = VHD_Form(request.POST, instance=vhd)
        if vhd_form.is_valid():
            vhd.save()
        return render(request, 'WebApp/vhd_edit.html', {'vhd_form': vhd_form, 'vhd_id': pk})


class VHDDelFormView(View):
    def post(self, request, pk):
        vhd = VHD.objects.filter(pk=pk).delete()
        return render(request, "base.html")


class FOListView(generic.ListView):
    model = FO
    template_name = 'WebApp/fo.html'
    context_object_name = 'fo'


class NKListView(generic.ListView):
    model = NK
    template_name = 'WebApp/nk.html'
    context_object_name = 'nk'


class NKFormView(View):
    def get(self, request):
        nk_form = NK_Form()
        return render(request, 'WebApp/nk_form.html', {'nk_form': nk_form})

    def post(self, request):
        nk_form = NK_Form(request.POST)
        if nk_form.is_valid():
            NK.objects.create(**nk_form.cleaned_data)
            return render(request, "base.html")
        return render(request, 'WebApp/nk_form.html', {'nk_form': nk_form})


class NKEditFormView(View):
    def get(self, request, pk):
        nk = NK.objects.get(pk=pk)
        nk_form = NK_Form(instance=nk)
        return render(request, 'WebApp/nk_edit.html', {'nk_form': nk_form, 'nk_id': pk})

    def post(self, request, pk):
        nk = NK.objects.get(pk=pk)
        nk_form = NK_Form(request.POST, instance=nk)
        if nk_form.is_valid():
            nk.save()
        return render(request, 'WebApp/nk_edit.html', {'nk_form': nk_form, 'nk_id': pk})


class NKDelFormView(View):
    def post(self, request, pk):
        nk = NK.objects.filter(pk=pk).delete()
        return render(request, "base.html")


class BankListView(generic.ListView):
    model = Bank
    template_name = 'WebApp/bank.html'
    context_object_name = 'bank'


class BankFormView(View):
    def get(self, request):
        bank_form = Bank_Form()
        return render(request, 'WebApp/bank_form.html', {'bank_form': bank_form})

    def post(self, request):
        bank_form = Bank_Form(request.POST)
        if bank_form.is_valid():
            Bank.objects.create(**bank_form.cleaned_data)
            return render(request, "base.html")
        return render(request, 'WebApp/bank_form.html', {'bank_form': bank_form})


class BankEditFormView(View):
    def get(self, request, pk):
        bank = Bank.objects.get(pk=pk)
        bank_form = Bank_Form(instance=bank)
        return render(request, 'WebApp/bank_edit.html', {'bank_form': bank_form, 'bank_id': pk})

    def post(self, request, pk):
        bank = Bank.objects.get(pk=pk)
        bank_form = Bank_Form(request.POST, instance=bank)
        if bank_form.is_valid():
            bank.save()
        return render(request, 'WebApp/bank_edit.html', {'bank_form': bank_form, 'bank_id': pk})


class BankDelFormView(View):
    def post(self, request, pk):
        bank = Bank.objects.filter(pk=pk).delete()
        return render(request, "base.html")


class PredpriyatieListView(generic.ListView):
    model = Predpriyatie
    template_name = 'WebApp/predpriyatie.html'
    context_object_name = 'predpriyatie'

    def get_queryset(self):
        try:
            queryset = super().get_queryset()
            word = self.request.GET.get('word')
            if word:
                queryset = queryset.filter(full_name__contains=word)
            year = self.request.GET.get('year')
            if year:
                queryset = queryset.filter(date__year=year)
            ot = self.request.GET.get('ot')
            do = self.request.GET.get('do')
            if ot and do:
                queryset = queryset.filter(chislo_rab__lte=do).filter(chislo_rab__gte=ot)
            bin = self.request.GET.get('bin')
            if bin:
                queryset = queryset.filter(bin_id__contains=bin)
            return queryset
        except:
            return HttpResponse('Вы ввели запрос с ошибкой')


class Query3View(generic.ListView):
    model = Predpriyatie
    template_name = 'action/q3.html'


class Query4View(generic.ListView):
    model = Predpriyatie
    template_name = 'action/q4.html'


class Query5View(generic.ListView):
    model = Predpriyatie
    template_name = 'action/q5.html'


class Report2View(generic.ListView):
    model = Predpriyatie
    template_name = 'action/r2.html'

def export_predpriyatie_xls(request, pk):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="predpriyatie.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Predpriyatie')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['БИН', 'Полное наименование', 'Сокрощенное наименование', 'Адрес', 'Телефон', 'ФИО руководителя',
                   'Форма организации', 'Вид хоз деят', 'Налоговый комитет', 'Число работников', 'Учредители' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        rows = Predpriyatie.objects.filter(bin_id__contains=pk).values_list('bin_id', 'full_name', 'sh_name', 'address', 'phone', 'fio_ruk',
                                                      'form_org__name', 'vid_hoz_d__name', 'nalog_kom__name', 'chislo_rab', 'uchrediteli')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response


class PredpriyatieFormView(View):
    def get(self, request):
        predpriyatie_form = Predpriyatie_Form()
        return render(request, 'WebApp/predpriyatie_form.html', {'predpriyatie_form': predpriyatie_form})

    def post(self, request):
        predpriyatie_form = Predpriyatie_Form(request.POST)
        if predpriyatie_form.is_valid():
            Predpriyatie.objects.create(**predpriyatie_form.cleaned_data)
            return render(request, "base.html")
        return render(request, 'WebApp/predpriyatie_form.html', {'predpriyatie_form': predpriyatie_form})


class PredpriyatieEditFormView(View):
    def get(self, request, pk):
        predpriyatie = Predpriyatie.objects.get(bin_id__contains=pk)
        predpriyatie_form = Predpriyatie_Form(instance=predpriyatie)
        return render(request, 'WebApp/predpriyatie_edit.html',
                      {'predpriyatie_form': predpriyatie_form, 'predpriyatie_id': pk})

    def post(self, request, pk):
        predpriyatie = Predpriyatie.objects.get(bin_id__contains=pk)
        predpriyatie_form = Predpriyatie_Form(request.POST, instance=predpriyatie)
        if predpriyatie_form.is_valid():
            predpriyatie.save()
        return render(request, 'WebApp/predpriyatie_edit.html',
                      {'predpriyatie_form': predpriyatie_form, 'predpriyatie_id': pk})


class PredpriyatieDelFormView(View):
    def post(self, request, pk):
        predpriyatie = Predpriyatie.objects.filter(bin_id=pk).delete()
        return render(request, "base.html")


class HP3View(generic.ListView):
    model = Predpriyatie
    template_name = 'action/hp3.html'
    context_object_name = 'predpriyatie'


class HP31View(generic.ListView):
    model = Predpriyatie
    template_name = 'action/hp3_1.html'
    context_object_name = 'predpriyatie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        print(name)
        predpriyatie = Predpriyatie.objects.get(full_name__contains=name)
        age = int(date.today().year - predpriyatie.date.year)
        context['predpriyatie'] = predpriyatie
        context['age'] = age
        return context


class PBListView(generic.ListView):
    model = PB
    template_name = 'WebApp/pb.html'
    context_object_name = 'pb'

    def get_queryset(self):
        try:
            queryset = super().get_queryset()
            day = self.request.GET.get('day')

            if day:
                queryset = queryset.filter(bin_pb__date__day=day)
            return queryset
        except:
            return HttpResponse('Вы ввели запрос с ошибкой')


class Query2View(generic.ListView):
    model = PB
    template_name = 'action/q2.html'


class PBFormView(View):
    def get(self, request):
        pb_form = PB_Form()
        return render(request, 'WebApp/pb_form.html', {'pb_form': pb_form})

    def post(self, request):
        pb_form = PB_Form(request.POST)
        if pb_form.is_valid():
            PB.objects.create(**pb_form.cleaned_data)
            return render(request, "base.html")
        return render(request, 'WebApp/pb_form.html', {'pb_form': pb_form})


class PBEditFormView(View):
    def get(self, request, pk):
        pb = PB.objects.get(bin_pb__bin_id__contains=pk)
        pb_form = PB_Form(instance=pb)
        return render(request, 'WebApp/pb_edit.html', {'pb_form': pb_form, 'pb_id': pk})

    def post(self, request, pk):
        pb = PB.objects.get(bin_pb__bin_id__contains=pk)
        pb_form = PB_Form(request.POST, instance=pb)
        if pb_form.is_valid():
            pb.save()
        return render(request, 'WebApp/pb_edit.html', {'pb_form': pb_form, 'pb_id': pk})


class PBDelFormView(View):
    def post(self, request, pk):
        pb = PB.objects.filter(bin_pb=pk).delete()
        return render(request, "base.html")


class PVDListView(generic.ListView):
    model = PVD
    template_name = 'WebApp/pvd.html'
    context_object_name = 'pvd'

    def get_queryset(self):
        try:
            queryset = super().get_queryset()
            vhd = self.request.GET.get('vhd')
            if vhd:
                queryset = queryset.filter(vid_hoz_d__name=vhd)
            return queryset
        except:
            return HttpResponse('Вы ввели запрос с ошибкой')


class Report3View(generic.ListView):
    model = VHD
    template_name = 'action/r3.html'
    context_object_name = 'vhd'


class BSListView(generic.ListView):
    model = BS
    template_name = 'WebApp/bs.html'
    context_object_name = 'bs'


class Query1View(generic.ListView):
    model = BS
    template_name = 'action/q1.html'
    context_object_name = 'bs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bs = BS.objects.all()
        fp = FP.objects.all()
        summa = []
        for i in bs:
            sum = 0
            for j in fp:
                if i.kod == j.bs.kod:
                    sum += j.summa
            summa.append([i.kod, sum])
        context['bs'] = bs
        context['summa'] = summa
        return context


class BSFormView(View):
    def get(self, request):
        bs_form = BS_Form()
        return render(request, 'WebApp/bs_form.html', {'bs_form': bs_form})

    def post(self, request):
        bs_form = BS_Form(request.POST)
        if bs_form.is_valid():
            BS.objects.create(**bs_form.cleaned_data)
            return render(request, "base.html")
        return render(request, 'WebApp/bs_form.html', {'bs_form': bs_form})


class BSEditFormView(View):
    def get(self, request, pk):
        bs = BS.objects.get(kod=pk)
        bs_form = BS_Form(instance=bs)
        return render(request, 'WebApp/bs_edit.html', {'bs_form': bs_form, 'bs_id': pk})

    def post(self, request, pk):
        bs = BS.objects.get(kod=pk)
        bs_form = BS_Form(request.POST, instance=bs)
        if bs_form.is_valid():
            bs.save()
        return render(request, 'WebApp/bs_edit.html', {'bs_form': bs_form, 'bs_id': pk})


class BSDelFormView(View):
    def post(self, request, pk):
        bs = BS.objects.filter(kod=pk).delete()
        return render(request, "base.html")


class FPListView(generic.ListView):
    model = FP
    template_name = 'WebApp/fp.html'
    context_object_name = 'fp'

    # queryset = FP.objects.filter()

    def get_queryset(self):
        try:
            queryset = super().get_queryset()
            fp_bin = self.request.GET.get('fp-bin')
            fp_year = self.request.GET.get('fp-year')
            if fp_bin and fp_year:
                queryset = queryset.filter(bin_fp__full_name__contains=fp_bin).filter(date=fp_year)
            priznak = self.request.GET.get('priznak')
            if priznak:
                queryset = queryset.filter(priznak=priznak)
            kvartal = self.request.GET.get('kvartal')
            if fp_bin and kvartal:
                queryset = queryset.filter(bin_fp__full_name__contains=fp_bin).filter(kvartal=kvartal)
            return queryset
        except:
            return HttpResponse('Вы ввели запрос с ошибкой')


class Report1View(generic.ListView):
    model = FP
    template_name = 'action/r1.html'
    context_object_name = 'fp'


class HP1View(generic.ListView):
    model = FP
    template_name = 'action/hp1.html'
    context_object_name = 'fp'


class HP2View(generic.ListView):
    model = FP
    template_name = 'action/hp2.html'
    context_object_name = 'fp'


class FPFormView(View):
    def get(self, request):
        fp_form = FP_Form()
        return render(request, 'WebApp/fp_form.html', {'fp_form': fp_form})

    def post(self, request):
        fp_form = FP_Form(request.POST)
        if fp_form.is_valid():
            FP.objects.create(**fp_form.cleaned_data)
            return render(request, "base.html")
        return render(request, 'WebApp/fp_form.html', {'fp_form': fp_form})


class FPEditFormView(View):
    def get(self, request, pk):
        fp = FP.objects.get(bin_fp__bin_id__contains=pk)
        fp_form = FP_Form(instance=fp)
        return render(request, 'WebApp/fp_edit.html', {'fp_form': fp_form, 'fp_id': pk})

    def post(self, request, pk):
        fp = FP.objects.get(bin_fp__bin_id__contains=pk)
        fp_form = FP_Form(request.POST, instance=fp)
        if fp_form.is_valid():
            fp.save()
        return render(request, 'WebApp/fp_edit.html', {'fp_form': fp_form, 'fp_id': pk})


class FPDelFormView(View):
    def post(self, request, pk):
        fp = FP.objects.filter(bin_fp__bin_id__contains=pk).delete()
        return render(request, "base.html")

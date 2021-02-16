import csv
import os

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.shortcuts import render
from django.db.models import Sum
from num2words import num2words

from .models import Csvbase


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        upload_data(filename)
        return render(request, 'site/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'site/upload.html')


def upload_data(path):
    file = 'media/'+path
    date = path.partition('.')[0]
    with open(file, encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:

            if row[0].isdigit() == False or row[0] == '':
                pass
            # if line_count == 0:
            #     line_count += 1
            # elif row[0] == '':
            #     pass
            else:
                numb_lot = row[0]
                p_lot = row[1]
                seller = row[2]
                product_name = row[3]
                product_type = row[4]
                product_kind = row[5]
                product_diameter = row[6]
                product_length = row[7]
                storehouse = row[8]
                product_size = row[9]
                start_product_price = row[10]
                start_lot_price = row[11]
                end_product_price = row[12]
                end_lot_price = row[13]
                buyer = row[14]
                EDRPOU = row[15]
                PDV_certificate = row[16]
                IPN = row[17]
                buyer_address = row[18]
                contact = row[19]
                line_count += 1

                Csvbase.objects.create(date=date, numb_lot=numb_lot, p_lot=p_lot, seller=seller, product_name=product_name,
                                       product_type=product_type, product_kind=product_kind,
                                       product_diameter=product_diameter, product_length=product_length,
                                       storehouse=storehouse, product_size=product_size,
                                       start_product_price=start_product_price, start_lot_price=start_lot_price,
                                       end_product_price=end_product_price, end_lot_price=end_lot_price, buyer=buyer,
                                       EDRPOU=EDRPOU, PDV_certificate=PDV_certificate, IPN=IPN,
                                       buyer_address=buyer_address, contact=contact)
                Csvbase.save
    os.remove(file)


def filter(request):
   message = request.POST
   return render(request, "site/line_csvbase.html", {'message_list': message})



def print_act(request):
    date = request.POST['date']
    EDRPOU = request.POST['EDRPOU']
    csvbase = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date))

    resultsum = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date)).aggregate(Sum('end_lot_price'))['end_lot_price__sum']

    total_sum = round(resultsum, 2)
    before = str(total_sum).partition('.')[0]
    after = str(total_sum).partition('.')[2]
    uah = before
    if after == '':
        kop = 0
    elif len(after) == 1:
        kop = after + '0'
    else:
        kop = after
    grn_leters = num2words(int(uah), lang='uk')
    if int(kop) > 0:
        kop_leters = num2words(int(kop), lang='uk')
    else:
        kop_leters = "0"
    grn_text = 'грн.'
    kop_text = 'коп.'
    total_numbers = str(uah) + '.' + str(kop)
    total_leters = str(grn_leters) + ' ' + str(grn_text) + ' ' + str(kop_leters) + ' ' + str(kop_text)

    return render(request, "site/post.html", {'EDRPOU_list': EDRPOU,
                                              'date_list': date,
                                              'csvbase_list': csvbase,
                                              'resultsum_list': total_numbers,
                                              'resultsum_in_words_list':total_leters})


def print_dogovor(request):
    date = request.POST['date']
    EDRPOU = request.POST['EDRPOU']
    csvbase = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date))

    resultsum = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date)).aggregate(Sum('end_lot_price'))['end_lot_price__sum']

    total_sum = round(resultsum, 2)
    before = str(total_sum).partition('.')[0]
    after = str(total_sum).partition('.')[2]
    uah = before
    if after == '':
        kop = 0
    elif len(after) == 1:
        kop = after + '0'
    else:
        kop = after
    grn_leters = num2words(int(uah), lang='uk')
    if int(kop) > 0:
        kop_leters = num2words(int(kop), lang='uk')
    else:
        kop_leters = "0"
    grn_text = 'грн.'
    kop_text = 'коп.'
    total_numbers = str(uah) + '.' + str(kop)
    total_leters = str(grn_leters) + ' ' + str(grn_text) + ' ' + str(kop_leters) + ' ' + str(kop_text)

    return render(request, "site/dogovor.html", {'EDRPOU_list': EDRPOU,
                                              'date_list': date,
                                              'csvbase_list': csvbase,
                                              'resultsum_list': total_numbers,
                                              'resultsum_in_words_list':total_leters})

# def filter_result(request):
#    message = request.POST
#    return render(request, "site/post.html", {'message_list': message})


# # Create your views here.
# def home_view(request):
#     print(request.POST)
#     return render(request, "home.html")

# class CsvBase(View):
#     def get(self, request):
#         csvbase = Csvbase.objects.all().order_by('desc')
#         return render(request, "site/line_csvbase.html", {"csvbase_list": csvbase,})
#


import csv
import os

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.shortcuts import render
from django.db.models import Sum
from num2words import num2words

from .models import Csvbase, Agrhouse


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
                commission = row[20]

                line_count += 1

                Csvbase.objects.create(date=date, numb_lot=numb_lot, p_lot=p_lot, seller=seller, product_name=product_name,
                                       product_type=product_type, product_kind=product_kind,
                                       product_diameter=product_diameter, product_length=product_length,
                                       storehouse=storehouse, product_size=product_size,
                                       start_product_price=start_product_price, start_lot_price=start_lot_price,
                                       end_product_price=end_product_price, end_lot_price=end_lot_price, buyer=buyer,
                                       EDRPOU=EDRPOU, PDV_certificate=PDV_certificate, IPN=IPN,
                                       buyer_address=buyer_address, contact=contact, commission=commission)
                Csvbase.save
    os.remove(file)


def filter(request):
   message = request.POST
   agrhouse = Agrhouse.objects.all().order_by('name')
   csvbase = Csvbase.objects.all()
   return render(request, "site/line_csvbase.html", {'message_list': message,
                                                     'agrhouse_list': agrhouse,
                                                     'csvbase_list': csvbase})



def print_act(request):
    date = request.POST['date']
    EDRPOU = request.POST['EDRPOU']
    garantv = request.POST['garantv']

    buyer2 = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date)).values_list('buyer')[0]
    buyer = buyer2[0]

    commission2 = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date)).values_list('commission')[0]
    commission = commission2[0]

    quarter = get_quarter(date)
    quarter2 = get_quarter2(date)
    #seller2 = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date)).values_list('seller').order_by('seller')
    # seller = get_uniq_seller(seller2)


    csvbase = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date))

    product_sizesum = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date)).aggregate(Sum('product_size'))[
        'product_size__sum']

    summa = Csvbase.objects.filter(EDRPOU=EDRPOU, date=date).values('seller').annotate(sum=Sum('end_lot_price'))

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

    date_text = get_text_date(date)

    return render(request, "site/post.html", {'EDRPOU_list': EDRPOU,
                                              'date_list': date,
                                              'buyer_list': buyer,
                                              'garantv_list': garantv,
                                              'csvbase_list': csvbase,
                                              'resultsum_list': total_numbers,
                                              'resultsum_in_words_list': total_leters,
                                              'product_sizesum_list': product_sizesum,
                                              'summa_list': summa,
                                              'date_text_list': date_text,
                                              'quarter_list': quarter,
                                              'quarter_list2': quarter2,
                                              'commission_list': commission,

                                              })


def print_dogovor(request):
    date = request.POST['date']
    EDRPOU = request.POST['EDRPOU']
    garantv = request.POST['garantv']
    lisgosp = request.POST['lisgosp']

    buyer2 = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date)).values_list('buyer')[0]
    buyer = buyer2[0]

    buyer_address2 = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date)).values_list('buyer_address')[0]
    buyer_address = buyer_address2[0]

    buyer_contact2 = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date)).values_list('contact')[0]
    buyer_contact = buyer_contact2[0]

    buyer_IPN2 = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date)).values_list('IPN')[0]
    buyer_IPN = buyer_IPN2[0]

    seller_name2 = Agrhouse.objects.all().filter(Q(name=lisgosp)).values_list('name')[0]
    seller_name = seller_name2[0]

    seller_cod2 = Agrhouse.objects.all().filter(Q(name=lisgosp)).values_list('cod')[0]
    seller_cod = seller_cod2[0]
    seller_adress2 = Agrhouse.objects.all().filter(Q(name=lisgosp)).values_list('adress')[0]
    seller_adress = seller_adress2[0]
    seller_score2 = Agrhouse.objects.all().filter(Q(name=lisgosp)).values_list('score')[0]
    seller_score = seller_score2[0]
    seller_phone2 = Agrhouse.objects.all().filter(Q(name=lisgosp)).values_list('phone')[0]
    seller_phone = seller_phone2[0]
    seller_individual_number2 = Agrhouse.objects.all().filter(Q(name=lisgosp)).values_list('individual_number')[0]
    seller_individual_number = seller_individual_number2[0]
    seller_fio2 = Agrhouse.objects.all().filter(Q(name=lisgosp)).values_list('fio')[0]
    seller_fio = seller_fio2[0]


    commission2 = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date)).values_list('commission')[0]
    commission = commission2[0]

    quarter = get_quarter(date)

    quarter2 = get_quarter2(date)

    #seller2 = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date)).values_list('seller').order_by('seller')
    # seller = get_uniq_seller(seller2)


    csvbase = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date), Q(seller=lisgosp))

    product_sizesum = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date), Q(seller=lisgosp)).aggregate(Sum('product_size'))[
        'product_size__sum']
    if product_sizesum == None:
        product_sizesum = '0'
    else:
        pass

    summa = Csvbase.objects.filter(EDRPOU=EDRPOU, date=date).values('seller').annotate(sum=Sum('end_lot_price'))

    resultsum = Csvbase.objects.all().filter(Q(EDRPOU=EDRPOU), Q(date=date), Q(seller=lisgosp)).aggregate(Sum('end_lot_price'))['end_lot_price__sum']
    try:
        total_sum = round(resultsum, 2)
    except:
        total_sum = None
    if total_sum == None:
        total_numbers = '0'
        total_leters = '0'
    else:
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

    date_text = get_text_date(date)

    return render(request, "site/dogovor.html", {'EDRPOU_list': EDRPOU,
                                              'date_list': date,
                                              'buyer_list': buyer,
                                              'garantv_list': garantv,
                                              'csvbase_list': csvbase,
                                              'resultsum_list': total_numbers,
                                              'resultsum_in_words_list': total_leters,
                                              'product_sizesum_list': product_sizesum,
                                              'summa_list': summa,
                                              'date_text_list': date_text,
                                              'quarter_list': quarter,
                                              'quarter_list2': quarter2,
                                              'commission_list': commission,
                                              'lisgosp_list':lisgosp,
                                              'buyer_address_list': buyer_address,
                                              'buyer_contact_list': buyer_contact,
                                              'buyer_IPN_list': buyer_IPN,
                                                 'seller_name_list': seller_name,
                                                 'seller_cod_list': seller_cod,
                                                 'seller_adress_list': seller_adress,
                                                 'seller_score_lsit': seller_score,
                                                 'seller_phone_list': seller_phone,
                                                 'seller_individual_number_list': seller_individual_number,
                                                 'seller_fio_list': seller_fio

                                                 })





# def get_uniq_seller(request):
#     seller = []
#     uniq_seller = set(request)
#     for request in uniq_seller:
#         seller.append(request)
#     return seller

def get_quarter(input):
    year, month, date = input.split('-')
    if month == '01' or '02' or '03':
        month = 'I квартал ' + year
    elif month == '04' or '05' or '06':
        month = 'II квартал' + year
    elif month == '07' or '08' or '09':
        month = 'III квартал'
    elif month == '10' or '11' or '12':
        month = 'IV квартал' + year
    quarter = month
    return quarter

def get_quarter2(input):
    year, month, date = input.split('-')
    if month == '01' or '02' or '03':
        month = 'I кварталi ' + year
    elif month == '04' or '05' or '06':
        month = 'II кварталi' + year
    elif month == '07' or '08' or '09':
        month = 'III кварталi'
    elif month == '10' or '11' or '12':
        month = 'IV кварталi' + year
    quarter = month
    return quarter



def get_text_date(input):
    year, month, date = input.split('-')
    if month == '01':
        month = 'січеня'
    elif month == '02':
        month = 'лютого'
    elif month == '03':
        month = 'березня'
    elif month == '04':
        month = 'квітеня'
    elif month == '05':
        month = 'травеня'
    elif month == '06':
        month = 'червеня'
    elif month == '07':
        month = 'липеня'
    elif month == '08':
        month = 'серпеня'
    elif month == '09':
        month = 'вересеня'
    elif month == '10':
        month = 'жовтеня'
    elif month == '11':
        month = 'листопада'
    elif month == '12':
        month = 'груденя'
    print_date=date + ' ' + month + ' ' + year + ' року'
    return print_date


# def filter_result(request):
#    message = request.POST
#    return render(request, "site/post.html", {'message_list': message})


# # Create your views here.
# def home_view(request):
#     print(request.POST)
#     return render(request, "home.html")
#
# def agrhouse(request):
#     agrhouse = Agrhouse.objects.all()
#     return render(request, "site/line_csvbase.html", {"agrhouse_list": agrhouse})



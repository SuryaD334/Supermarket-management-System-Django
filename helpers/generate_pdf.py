from datetime import datetime
from company.models import Company


def generate_report(context, dataset, title):
    comp = Company.objects.values('name', 'address', 'company_tel')
    company_name = comp[0]['name'].upper()
    address = comp[0]['address']
    tel = comp[0]['company_tel']
    today = datetime.now()

    context['data'] = dataset
    company = {"name": company_name, "address": address, "tel": tel, "date": today, "title": title}
    titles = []
    for data in dataset[0].keys():
        if '_' in data:
            data = data.split('_')[0] + ' ' + data.split('_')[1]
            titles.append(data.upper())
        else:
            titles.append(data.upper())
    context['titles'] = titles
    context['company'] = company

    return context


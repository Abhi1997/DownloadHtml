import urllib.request
import bs4
import re
import csv


def name(filename):
    file = urllib.request.urlopen('file:///home/wello-tirthahalli/Documents/A_HTML/' + filename)
    soup = bs4.BeautifulSoup(file, 'lxml')
    Name = soup.b.text
    return Name


def href(filename):
    file = urllib.request.urlopen('file:///home/wello-tirthahalli/Documents/A_HTML/' + filename)
    soup = bs4.BeautifulSoup(file, 'lxml')
    for HTML in soup.find_all('link', attrs={'rel': 'canonical'}):
        return HTML.get('href')


def dosage(filename):
    file = urllib.request.urlopen('file:///home/wello-tirthahalli/Documents/A_HTML/' + filename)
    soup = bs4.BeautifulSoup(file, 'lxml')
    # for a in soup.findAll('p', limit=3):
    a = soup.body.text
    b = a.replace('\n', '').replace("  ", '')
    if re.search(r'Dosage form:', b, re.M | re.I):
        replace = re.sub(r'Ingredients:', " Ingredients:", b)
        replace = re.sub(r'Labeler:', " Labeler:", replace)
        find = re.search(r'Dosage form: (.*) Ingredients: (.*?) Labeler', replace, re.M | re.I)
        return find.group(1)

    elif re.search(r'Name: ', b, re.M | re.I):
        replace = re.sub(r'Form:', " Form:", b)
        replace = re.sub(r'Ingredients:', " Ingredients:", b)
        replace = re.sub(r'Date:', " Date:", replace)
        find = re.search(r'Form: (.*) Ingredients: (.*?) Date', replace, re.M | re.I)
        return find.group(1)


def ingd(filename):
    file = urllib.request.urlopen('file:///home/wello-tirthahalli/Documents/A_HTML/' + filename)
    soup = bs4.BeautifulSoup(file, 'lxml')
    a = soup.body.text
    b = a.replace('\n', '').replace("  ", '')
    # for a in soup.findAll('p', limit=3):
    if re.search(r'Dosage form:', b, re.M | re.I):
        replace = re.sub(r'Ingredients:', " Ingredients:", b)
        replace = re.sub(r'Labeler:', " Labeler:", replace)
        find = re.search(r'Dosage form: (.*) Ingredients: (.*?) Labeler', replace, re.M | re.I)
        return find.group(2)

    elif re.search(r'Name: ', b, re.M | re.I):
        replace = re.sub(r'Form:', " Form:", b)
        replace = re.sub(r'Ingredients:', " Ingredients:", b)
        replace = re.sub(r'Date:', " Date:", replace)
        find = re.search(r'Form: (.*) Ingredients: (.*?) Date', replace, re.M | re.I)
        return find.group(2)


def purpose(filename):
    file = urllib.request.urlopen('file:///home/wello-tirthahalli/Documents/A_HTML/' + filename)
    soup = bs4.BeautifulSoup(file, 'lxml')
    if soup.findAll('tbody', attrs={'class': 'Headless'}) is False:
        if soup.findAll('tr', attrs={'class': 'First Toprule'}):
            for a in soup.findAll('tr', attrs={'class': 'First Toprule'}):
                for p in a.select('td'):
                    print('')
                return p.text

        elif soup.findAll('tr', attrs={'class': 'Botrule Last'}):
            for x in soup.findAll('tr', attrs={'class': 'First Toprule'}):
                for y in x.select('td'):
                    print('')
                return y.text

    else:
        t = soup.body.text
        s = t.replace('\n', '').replace("  ", '')
        replace = s.replace('USES', ' USES ').replace('WARNINGS', ' WARNINGS ').replace('PURPOSE', ' PURPOSE ').replace(
            'Uses', ' Uses ').replace('Purpose', ' Purpose ').replace('Warnings', ' Warnings ').replace('Uses:',
                                                                                                        ' Uses: ').replace(
            'Purpose:', ' Purpose: ').replace('Warnings:', ' Warnings: ').replace('WARNING', ' WARNINGS').replace(
            'Warning', ' Warnings ')
        find = re.search(r'.* purpose (.*?) uses (.*?) warnings', replace, re.I | re.M)
        find1 = re.search(r'.* purpose (.*?) warnings', replace, re.I | re.M)
        if find:
            return find.group(1)  # PURPOSE
            print(find.group(1))
        elif find1:
            return find1.group(1)
        else:
            print('NONE')


def uses(filename):
    file = urllib.request.urlopen('file:///home/wello-tirthahalli/Documents/A_HTML/' + filename)
    soup = bs4.BeautifulSoup(file, 'lxml')
    t = soup.body.text
    s = t.replace('\n', '').replace("  ", '')
    replace = s.replace('USES', ' USES ').replace('WARNINGS', ' WARNINGS ').replace('PURPOSE', ' PURPOSE ').replace(
        'Uses', ' Uses ').replace('Purpose', ' Purpose ').replace('Warnings', ' Warnings ').replace('Uses:',
                                                                                                    ' Uses: ').replace(
        'Purpose:', ' Purpose: ').replace('Warnings:', ' Warnings: ').replace('WARNING', ' WARNINGS').replace('Warning',
                                                                                                              ' Warnings ')
    find = re.search(r'.* purpose (.*?) uses (.*?) warnings', replace, re.I | re.M)
    find1 = re.search(r'.* uses (.*?) indications', replace, re.I | re.M)
    find2 = re.search(r'.* uses (.*?) warnings', replace, re.I | re.M)
    if find:
        return find.group(2)  # USES
    elif find1:
        return find1.group(1)  # USES
    elif find2:
        return find2.group(1)
    else:
        print('NONE')


def linker():
    with open('Otc_Offline_Demo.csv', 'a', newline="")as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['NAME', 'LINKS', 'DOSAGE', 'INGREDIENT', 'PURPOSE', 'USES'])
        for a in range(1, 11):
            print(a)
            x = 'A%d' % a
            reduce = x + '.html'
            writer.writerow([name(reduce), href(reduce), dosage(reduce), ingd(reduce), purpose(reduce),uses(reduce)])


linker()

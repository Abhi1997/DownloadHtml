import requests
import bs4
import csv
import os.path


def download(x, y):
    url1 = ('A%d') % y                                                      #Giving A new FileName
    url = 'https://www.drugs.com' + x
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    save_path = '/home/Documents/A_links'                                    #directory Path
    completeName = os.path.join(save_path, url1 + '.html')
    file = open(completeName, "w+")
    print('here')
    file.write(soup.prettify())
    file.close()


def reference():
        file_obj = open('link.csv', 'r')                                     # Read Links From Csv File
        for r in csv.reader(file_obj):
            r = list(csv.reader(file_obj))
            for a in range(1, 2926):
                print(a)
                reduce = str(r[a]).replace('[', '').replace(']', '').replace("'", "")
                download(reduce, a)


reference()

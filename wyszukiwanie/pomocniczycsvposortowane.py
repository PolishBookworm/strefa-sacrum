import csv
#id parafii to numer wiersza w którym ta parafia sie znajduje, numerujemy od 0

with open('posortowane.csv', 'w', newline='', encoding='utf-8') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    listakolumnzgodzinamimszy = [3,5,9]# z palca
    for kolumna in listakolumnzgodzinamimszy:
        csv_file = csv.reader(open('zwztdaneboze2.csv', "r", encoding='utf-8'), delimiter=';')
        lista_mszy = []
        idparafii = -1
        for row in csv_file:
            idparafii +=1
            for godzina in row[kolumna].split(','):
                dodatek = ''
                if godzina[-1]=='*':
                    dodatek = '*'
                    godzina = godzina[:-1]
                lista_mszy.append([int(godzina.split(':')[0])*100+int(godzina.split(':')[1]),dodatek,idparafii] )
        #print(lista_mszy)
        nowa_lista_mszy=sorted(lista_mszy, key=lambda x: x[0], reverse=False)
        tekst=[]
        for element in nowa_lista_mszy:
            tekst.append(str(element[0])+','+element[1]+','+str(element[2]))
        #print(tekst)



        spamwriter.writerow(tekst)
with open('posortowane.csv', 'a', newline='', encoding='utf-8') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    listakolumnzgodzinamimszy = [7]# z palca kolumny z typem adoracji
    for kolumna in listakolumnzgodzinamimszy:
        csv_file = csv.reader(open('zwztdaneboze2.csv', "r", encoding='utf-8'), delimiter=';')
        lista_mszy = []
        idparafii = -1
        for row in csv_file:
            idparafii +=1
            #print(row[kolumna].split('–'))
            godzina = (row[kolumna].split('–')[1])
            dodatek = ''
            if godzina[-1]=='*':
                dodatek = '*'
                godzina = godzina[:-1]
            #print(godzina, idparafii)
            lista_mszy.append([int(godzina.split(':')[0])*100+int(godzina.split(':')[1]),dodatek,idparafii] )
        #print(lista_mszy)
        nowa_lista_mszy=sorted(lista_mszy, key=lambda x: x[0], reverse=False)
        tekst=[]
        for element in nowa_lista_mszy:
            tekst.append(str(element[0])+','+element[1]+','+str(element[2]))
        #print(tekst)
        spamwriter.writerow(tekst)



csv_file = csv.reader(open('posortowane.csv', "r", encoding='utf-8'), delimiter=';')
for line in csv_file:
    print (line)

# kolumny to godziny mszy BSO w tygodzniu, mszy w niedziele i święta, majówek, zakończenia adoracji

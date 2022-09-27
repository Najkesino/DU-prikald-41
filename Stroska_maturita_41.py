import tkinter
canvas = tkinter.Canvas(width=600, height=300, bg='white')
canvas.pack() #importujem platno na kresleniee

farby = ['green', 'red', 'blue', 'orange'] #definujem zoznam s farbami

def stvorce(): #funkcia na vykreslenie stvorcov
    open('vyber_jedla.txt', 'w').close() #prikaz na otvorenie suboru a okamzitim zavretim, vymazem tym obsah suboru
    x = 5 #premenna x
    canvas.create_text(300, 50, text='VYBER JEDLA', font='Arial 30') #vypisem nazov nad stvorce
    for i in range(4): #for cyklus na vytvorenie stvorcov
        canvas.create_rectangle(x, 75, x+145, 250, fill=farby[i], tags='obdlznik_'+str(farby[i])) #vykreslim stvorce s danymi vlastnostami a pomocou zoznamu a cyklus pridavam farbu
        x+=150 #zvacsim premennu x o 150 aby sa posuvali stvorce

def klik(event): #funkcia na reagovanie kliknutia
    x = 5 #premenna x
    obed = None #premenna obed na zistenie farby obeda 
    subor = open('vyber_jedla.txt', 'a', encoding='UTF-8') #otvorim si subor na pridavanie informacii donho
    if entry1.get()!='': #podmienkou if zistim ci nie je vstupne pole entry prazdne a ak nie je pokracujem dalej 
        for i in range(4): #for cyklus na zistenie na ktory stvorec som klikol 
            if x+145>event.x>x and 250>event.y>75: #podmienka ktorou to zistim
                obed = farby[i] #ak je podmienka pravdiva zapisem danu farbu do premennej obed
                if obed=='green': #pomocou ifu zadam do premennej obed prve pismenko farby obeda
                    obed = 'z'
                elif obed=='red':
                    obed = 'c'
                elif obed=='blue':
                    obed = 'm'
                else:
                    obed = 'o'
                subor.write(entry1.get()+' '+str(obed)+'\n') #zapisem do suboru cislo studenta plus akej farby si vybral obed
            x+=150 # zmenim premennu x o 150
    subor.close() #zavriem subor aby sa mi spravne ulozil
    
stvorce() #zavolam funkciu stvorce na ich vykreslenie

entry1 = tkinter.Entry() #pridam si do programu vstupne pole kde zadam kod studenta
entry1.pack()
label1 = tkinter.Label(text='Kod studenta') #vypise mi text 'kod studenta' aby som vedel co tam mam zadat
label1.pack()
canvas.bind_all('<Button-1>', klik) #nabindujem si lave tlacitdlo mysi a pri jeho kliknuti sputim funkciu klik



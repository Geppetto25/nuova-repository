### APPUNTI DI PYTHON ###


    ### SINTASSI ###

# commento

print()

input()

if True:
    print('vero') #indentazione
elif False:
    print('falso')
else:
    print('non so')

    ### VARIABILI ###

x = 5
y = 3.14
z = 'ciao'
print(x, y, z)

# nomi non validi
#1x = 5
#x-1 = 5
#x y = 5 

    ### TIPI DI DATI ###

a = 'ciao' #str
b = [1, 2, 3] #list
c = (1, 2, 3) #tuple
d = {'nome': 'Mario', 'cognome': 'Rossi'} #dict
e = {1, 2, 3} #set
f = range(5) #range
x = 5 #int
y = 3.14 #float
z = True #bool

print(type(a), type(x), type(y), type(z), type(b), type(c), type(d), type(e), type(f))

    ### CASTING ###
x = 5
y = float(x) #casting da int a float

    ### STRINGHE ###
s = 'ciao'
smr = '''ciao
sono
kekko''' #stringa multilinea
print(s[0]) #c
print(s[1:3]) #ia
print(s[-1]) #o
print(s.upper()) #CIAO
print(s.lower()) #ciao
print(s.replace('a', 'o')) #cioo
print(s.split('a')) #['ci', 'o']
print(smr.splitlines()) #['ciao', 'sono', 'kekko']
print(len(s)) #4
print(s.strip()) #rimuove spazi bianchi all'inizio e alla fine

    ### BOOLEANI ###
x = True
bool(x) #True
bool(False) #False
bool(0) #False
bool(None) #False
bool('') #False
bool([]) #False
bool({}) #False
bool(()) #False

    ### LISTE ###

# ordinate, mutabili, indicizzate, duplicabili
x = [1, 2, 3]
len(x) #4
type(x) #list
list('ciao') #['c', 'i', 'a', 'o']
x[0] #1
x[0] = 0 #modifica il primo elemento della lista
x.append(4) #aggiunge 4 alla fine della lista
x.insert(0, -1) #inserisce -1 all'inizio della lista
x.remove(2) #rimuove il primo elemento con valore 2
x.pop() #rimuove e restituisce l'ultimo elemento della lista
x.clear() #rimuove tutti gli elementi della lista
x.extend(y) #aggiunge gli elementi di y alla fine della lista
x.append('6') #aggiunge '6' come elemento alla fine della lista
x.sort() #ordina la lista in ordine crescente
y = x.copy() #copia la lista x in y

    ### TUPLE ###
# ordinate, immutabili, indicizzate, duplicabili
x = (1, 2, 3)
y = ('ciao',)
(a, b, c) = x #unpacking

    ### SET ###

# non ordinate, mutabili, non indicizzate, non duplicabili
x = {'roma', 'milano', 'napoli'}
for citta in x:
    print(citta)
x.add('torino') #aggiunge 'torino' al set
x.update({'firenze', 'bologna'}) #unisce due set
x.remove('milano') #rimuove 'milano' dal set
x.discard('milano') #rimuove 'milano' dal set senza generare errore se non esiste
x.pop() #rimuove e restituisce un elemento casuale del set
z = x.union({'genova', 'palermo'}) #unisce due set senza modificare x
z = x.intersection({'roma', 'firenze'}) #restituisce un nuovo set con gli elementi comuni a x e all'altro set
z = x.difference({'roma', 'firenze'}) #restituisce un nuovo set con gli elementi di x che non sono nell'altro set
z = x.symmetric_difference({'roma', 'firenze'}) #restituisce un nuovo set con gli elementi di x che non sono nell'altro set e viceversa

    ### DIZIONARI ###

# ordinate, mutabili, indicizzati per chiave, non duplicabili
x = {'nome': 'Mario', 'età': 30}
print(x['nome']) #stampa 'Mario'
x['città'] = 'Roma' #aggiunge una nuova coppia chiave-valore
x.get('nome') #stampa 'Mario'
x.keys() #restituisce le chiavi del dizionario
x.values() #restituisce i valori del dizionario
x.items() #restituisce le coppie chiave-valore del dizionario

    ### FUNZIONI ###

def saluta(nome):
    print('Ciao ' + nome)

saluta('carlo')

def somma(a, b):
    return a + b

risultato = somma(5, 3)
print(risultato)

def saluta(nome='Mario'):
    print('Ciao ' + nome)

def somma(*args):
    return sum(args)

risultato = somma(1, 2, 3, 4, 5)
print(risultato)

    ### CICLI ###
    ### FOR ###
for i in range(5):
    print(i)

for citta in ['roma', 'milano', 'napoli']:
    print(citta)

    ### WHILE ###

x = 0
while x < 5:
    print(x)
    x += 1

    ### CONDIZIONI ###
if x > 3:
    print("x è maggiore di 3")
elif x == 3:
    print("x è uguale a 3")
else:
    print("x non è maggiore di 3")

    ### CLASSI ###
class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    def saluta(self):
        print('Ciao, mi chiamo ' + self.nome)

persona1 = Persona('Mario', 30)
persona1.saluta()
print(persona1.nome) #stampa 'Mario'

    ### EREDITARIETÀ ###
class Studente(Persona):
    def __init__(self, nome, età, matricola):
        super().__init__(nome, età)
        self.matricola = matricola

    ### SCOPE ###
x = 5 #variabile globale
def funzione():
    x = 3 #variabile locale
    print(x) #stampa 3

funzione() #stampa 3
print(x) #stampa 5

def funzione2():
    global x
    print(x) #stampa 5

    ### MODULI ###
import modulo.py
modulo.funzione()
modulo.classe()
x = modulo.variabile
import modulo.py as m
m.funzione()

import math
print(dir(math)) #stampa tutti gli attributi del modulo math

from math import sqrt
print(sqrt(16)) #stampa 4.0

    ### DATA E ORA ###

import datetime
x = (datetime.datetime.now())
print(x) #stampa la data e l'ora corrente

x = datetime.datetime(2023, 10, 1, 12, 0, 0)

x = datetime.datetime.now()
print(x.strftime("%Y-%m-%d %H:%M:%S")) #stampa la data e l'ora corrente in formato stringa

# %Y - anno con 4 cifre
# %m - mese con 2 cifre
# %d - giorno con 2 cifre
# %H - ora con 2 cifre
# %M - minuti con 2 cifre
# %S - secondi con 2 cifre
# %f - microsecondi con 6 cifre
# %a - giorno della settimana abbreviato
# %A - giorno della settimana completo
# %b - mese abbreviato
# %B - mese completo
# %c - data e ora locale
# %x - data locale
# %X - ora locale
# %j - giorno dell'anno con 3 cifre
# %U - numero della settimana con 2 cifre (domenica come primo giorno della settimana)
# %W - numero della settimana con 2 cifre (lunedì come primo giorno della settimana)
# %Z - fuso orario
# %z - offset del fuso orario
# %G - anno ISO con 4 cifre
# %u - giorno della settimana ISO (1-7)
# %V - numero della settimana ISO con 2 cifre

    ### MATH ###
import math

x = min(5, 10) #5
x = max(5, 10) #10
x = abs(-7.25) #7.25
x = pow(4, 3) #64
x = math.sqrt(64) #8.0
x = math.ceil(1.4) #2
x = math.floor(1.4) #1
x = math.pi #3.141592653589793

    ### JSON ###

import json
dizionario = '{ "nome": "Mario", "età": 30 }'
y = json.loads(dizionario) #converte la stringa JSON in un dizionario Python
print(y['nome']) #stampa 'Mario'

x = {'nome': 'Mario', 'età': 30}
json_string = json.dumps(x) #converte il dizionario Python in una stringa JSON
print(json_string) #stampa '{"nome": "Mario", "età": 30}' (stringa JSON)

# convertibili: str, int, float, bool, list, tuple, dict, set, None

json_string = json.dumps(x, indent=4, sort_keys=True) #converte il dizionario Python in una stringa JSON con indentazione di 4 spazi

    ### PIP ### (su terminale) pip è un gestore di pacchetti 
# pip install nome_pacchetto
# pip install --upgrade nome_pacchetto
# pip uninstall nome_pacchetto
# pip list

    ### TRY EXCEPT ###
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Non puoi dividere per zero!")

try:
    print(qwerty)
except NameError:
    print("Si è verificato un errore!")
except:
    print("Si è verificato un errore!")
else:
    print("Nessun errore!")
finally:
    print("Esecuzione del blocco finally!") # viene eseguito sempre, anche se non c'è un errore

x = -1
if x < 0:
    raise Exception("x non può essere negativo!") #genera un'errore se x è negativo

    ### FORMATTAZIONE STRINGHE ###

nome = "Mario"
età = 30
print("Ciao, mi chiamo " + nome + " e ho " + str(età) + " anni.") #concatenazione di stringhe
print("Ciao, mi chiamo {0} e ho {1:.2f} anni.".format(nome, età)) #formattazione con il metodo format
print(f"Ciao, mi chiamo {nome} e ho {età} anni.") #formattazione con f-string

    ### LAVORARE CON FILE ###

# r - lettura, errore se non esiste
# a - aggiunta, crea il file se non esiste
# w - scrittura, crea il file se non esiste, sovrascrive il contenuto se esiste
# x - creazione, errore se non esiste

x = open("file.txt", "r")
print(x.read()) #legge tutto il contenuto del file
print(x.readline()) #legge una riga del file
print(x.readlines()) #legge tutte le righe del file e le restituisce come lista
print(x.read(5)) #legge i primi 5 caratteri del file
x.close() #chiude il file

file = open("file.txt", "a")
file.write("Ciao, sono un nuovo testo!\n") #aggiunge una nuova riga al file
file.close() #chiude il file

file = open("file.txt", "w") #sovrascrive il contenuto del file

file = open("file.txt", "x")

import os
os.remove("file.txt") #elimina il file

if os.path.exists("file.txt"):
    os.remove("file.txt") #elimina il file se esiste
else:
    print("Il file non esiste")

os.rmdir("cartella") #elimina la cartella se è vuota

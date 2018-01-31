from bottle import *


frett=[

    {'title':'Er Trump Trump?',
     'text':'Er Trump í raun og veru ann sjálpur. Getur hann verið einhver annar í dulagervi. Það þarf að ransaka þetta einhvað betur. Þessvegna höfum við hjá pésafréttum ráðið mann í vinnu sem rassar bara þetta mál. Hann verður sendu út til að komast í botns í því.',
     'pictur':'trump.jpg',
     'auther':'Ólafur Sverrisson',
     },

    {'title':'Krakki fastur í leikfangavél',
     'text':'Það var fundið strák í leikfangavél eftir að hann reindi að ná sér í bangsa. Pilturinn heitir Pétur Steinn og skreið inn í vélina eftir að hann fékk ekki bangsann sinn. Það er allt í lagi með strákinn en var feiminn þegar við komum á staðin og tókum viðtal við föreldra hann.',
     'pictur':'petur.jpg',
     'auther':'Steinar Bergson',
     },

    {'title':'Nizzan með nýjan bíl',
     'text':'Nizzan er kominn með nýjan bíl á markaðinn. Þetta er endur gerð af nizzan leaf. Þetta er rafmags bíll. Hann fékk nýtt útlit og lítur betur út i okkar mati. Bíllinn bætist í rafmagsbíla flota hja nizzan ',
     'pictur':'nizzan.jpg',
     'auther':'BMW Fordson',
     },

    {'title':'Hvort er betri appel eða windos',
     'text':'Umhverfis- og auðlindaráðuneytið hefur skilað Strætó bs áliti sínu varðandi undanþágu á reglugerð um hollustuhætti sem myndi leyfa gæludýr í Strætó í eitt ár. Um er að ræða tilraunaverkefni og verður bréf ráðuneytisins tekið fyrir á fundi stjórnar Strætó á föstudag..',
     'pictur':'straeto.jpg',
     'auther':'Ég sveinsson',
     },

    {'title':'Koma þessir til landsins?',
     'text':'Mercedes-Benz hyggst setja í gang í lok næsta árs fram­leiðslu á Mercedes-Benz Cit­aro-stræt­is­vagni sem mun ganga ein­göngu fyr­ir raf­magni. Eng­inn út­blást­ur gróður­húsalofts verður frá hon­um og hann verður sér­lega hljóðlát­ur..',
     'pictur':'straeto1.jpg',
     'auther':'Pétur Steinar',
     }

]

@route('/')
def index():
    return template('verk_3')

@route('/verk1')
def verk():
    return template('verk_3_a')

@route('/kt/<kennitala>')
def kt(kennitala):
    return template('verk3_kt',kennitala=kennitala)

@route('/verk2')
def verk2():
    return template('verk_b', frett[0])

@route('/frettir/<n>')
def frettir(n):
    return template('verk_b_frettir', frett[int(n)])




@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./resources')

@error(404)
def error404(error):
    return '<h1>Þessi siða er ekki til</h1>' \
           '<a href="/verk2">Til baka</a>'

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

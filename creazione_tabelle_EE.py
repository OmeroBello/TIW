import sqlite3

url = "Database_EE"

#---------- creazione tabelle ----------

def crea_tabelle():
    crea_tabella_paesi()
    crea_tabella_università()
    crea_tabella_lingue()
    crea_tabella_gradiStudio()
    crea_tabella_semestri()
    crea_tabella_campiDiStudio()
    crea_tabella_corsi()

def crea_tabella_paesi():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.execute("DROP TABLE IF EXISTS TABELLA_PAESI")
    cursore.execute("CREATE TABLE TABELLA_PAESI(ID varchar(50) PRIMARY KEY, \
                    PAESE varchar(50) NOT NULL)")
    connessione.commit()
    cursore.close()
    connessione.close()

def crea_tabella_università():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.execute("DROP TABLE IF EXISTS TABELLA_UNIVERSITÀ")
    cursore.execute("CREATE TABLE TABELLA_UNIVERSITÀ(ID integer PRIMARY KEY AUTOINCREMENT, \
                    NOME_UNIVERSITÀ varchar(50) NOT NULL, PAESE varchar(50) NOT NULL, \
                    FOREIGN KEY (PAESE) REFERENCES TABELLA_PAESI(ID) )" )
    connessione.commit()
    cursore.close()
    connessione.close()

def crea_tabella_lingue():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.execute("DROP TABLE IF EXISTS TABELLA_LINGUE")
    cursore.execute("CREATE TABLE TABELLA_LINGUE(ID varchar(50) PRIMARY KEY, LINGUA varchar(50) NOT NULL)")
    connessione.commit()
    cursore.close()
    connessione.close()

def crea_tabella_gradiStudio():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.execute("DROP TABLE IF EXISTS TABELLA_GRADI")
    cursore.execute("CREATE TABLE TABELLA_GRADI(ID integer PRIMARY KEY, GRADO varchar(50) NOT NULL)")
    connessione.commit()
    cursore.close()
    connessione.close()

def crea_tabella_semestri():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.execute("DROP TABLE IF EXISTS TABELLA_SEMESTRI")
    cursore.execute("CREATE TABLE TABELLA_SEMESTRI(ID integer PRIMARY KEY, SEMESTRE varchar(50) NOT NULL)")
    connessione.commit()
    cursore.close()
    connessione.close()

def crea_tabella_campiDiStudio():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.execute("DROP TABLE IF EXISTS TABELLA_CAMPI")
    cursore.execute("CREATE TABLE TABELLA_CAMPI(ID integer PRIMARY KEY, CAMPO varchar(50) NOT NULL)")
    connessione.commit()
    cursore.close()
    connessione.close()

def crea_tabella_corsi():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.execute("DROP TABLE IF EXISTS TABELLA_CORSI")
    cursore.execute("CREATE TABLE TABELLA_CORSI(ID integer PRIMARY KEY AUTOINCREMENT, \
                    NOME_CORSO varchar(50) NOT NULL, \
                    ID_UNIVERSITÀ integer NOT NULL, \
                    ID_CAMPO integer NOT NULL, \
                    ID_GRADO inetegr NOT NULL, \
                    ID_SEMESTRE integer NOT NULL, \
                    ID_LINGUA varchar(50) NOT NULL, \
                    ECTS integer NOT NULL, \
                    LINK varchar(50) NOT NULL, \
                    FOREIGN KEY (ID_UNIVERSITÀ) REFERENCES TABELLA_UNIVERSITÀ(ID), \
                    FOREIGN KEY (ID_CAMPO) REFERENCES TABELLA_CAMPI(ID), \
                    FOREIGN KEY (ID_GRADO) REFERENCES TABELLA_GRADI(ID), \
                    FOREIGN KEY (ID_SEMESTRE) REFERENCES TABELLA_SEMESTRI(ID), \
                    FOREIGN KEY (ID_LINGUA) REFERENCES TABELLA_LINGUE(ID))" )
    connessione.commit()
    cursore.close()
    connessione.close()

#---------- inserimento dati nelle tabelle ----------

università = [("Norges teknisk-naturvitenskapelige universitet", "NO"),
              ("Università degli Studi di Modena e Reggio Emilia", "IT"),
              ("VIA University College", "DK")]

paesi = [('AF', 'Afghanistan'),
        ('AL', 'Albania'),
        ('DZ', 'Algeria'),
        ('AS', 'American Samoa'),
        ('AD', 'Andorra'),
        ('AO', 'Angola'),
        ('AI', 'Anguilla'),
        ('AQ', 'Antarctica'),
        ('AG', 'Antigua And Barbuda'),
        ('AR', 'Argentina'),
        ('AM', 'Armenia'),
        ('AW', 'Aruba'),
        ('AU', 'Australia'),
        ('AT', 'Austria'),
        ('AZ', 'Azerbaijan'),
        ('BS', 'Bahamas'),
        ('BH', 'Bahrain'),
        ('BD', 'Bangladesh'),
        ('BB', 'Barbados'),
        ('BY', 'Belarus'),
        ('BE', 'Belgium'),
        ('BZ', 'Belize'),
        ('BJ', 'Benin'),
        ('BM', 'Bermuda'),
        ('BT', 'Bhutan'),
        ('BO', 'Bolivia'),
        ('BA', 'Bosnia And Herzegowina'),
        ('BW', 'Botswana'),
        ('BV', 'Bouvet Island'),
        ('BR', 'Brazil'),
        ('BN', 'Brunei Darussalam'),
        ('BG', 'Bulgaria'),
        ('BF', 'Burkina Faso'),
        ('BI', 'Burundi'),
        ('KH', 'Cambodia'),
        ('CM', 'Cameroon'),
        ('CA', 'Canada'),
        ('CV', 'Cape Verde'),
        ('KY', 'Cayman Islands'),
        ('CF', 'Central African Rep'),
        ('TD', 'Chad'),
        ('CL', 'Chile'),
        ('CN', 'China'),
        ('CX', 'Christmas Island'),
        ('CC', 'Cocos Islands'),
        ('CO', 'Colombia'),
        ('KM', 'Comoros'),
        ('CG', 'Congo'),
        ('CK', 'Cook Islands'),
        ('CR', 'Costa Rica'),
        ('CI', 'Cote D`ivoire'),
        ('HR', 'Croatia'),
        ('CU', 'Cuba'),
        ('CY', 'Cyprus'),
        ('CZ', 'Czech Republic'),
        ('DK', 'Denmark'),
        ('DJ', 'Djibouti'),
        ('DM', 'Dominica'),
        ('DO', 'Dominican Republic'),
        ('TP', 'East Timor'),
        ('EC', 'Ecuador'),
        ('EG', 'Egypt'),
        ('SV', 'El Salvador'),
        ('GQ', 'Equatorial Guinea'),
        ('ER', 'Eritrea'),
        ('EE', 'Estonia'),
        ('ET', 'Ethiopia'),
        ('FK', 'Falkland Islands (Malvinas)'),
        ('FO', 'Faroe Islands'),
        ('FJ', 'Fiji'),
        ('FI', 'Finland'),
        ('FR', 'France'),
        ('GF', 'French Guiana'),
        ('PF', 'French Polynesia'),
        ('TF', 'French S. Territories'),
        ('GA', 'Gabon'),
        ('GM', 'Gambia'),
        ('GE', 'Georgia'),
        ('DE', 'Germany'),
        ('GH', 'Ghana'),
        ('GI', 'Gibraltar'),
        ('GR', 'Greece'),
        ('GL', 'Greenland'),
        ('GD', 'Grenada'),
        ('GP', 'Guadeloupe'),
        ('GU', 'Guam'),
        ('GT', 'Guatemala'),
        ('GN', 'Guinea'),
        ('GW', 'Guinea-bissau'),
        ('GY', 'Guyana'),
        ('HT', 'Haiti'),
        ('HN', 'Honduras'),
        ('HK', 'Hong Kong'),
        ('HU', 'Hungary'),
        ('IS', 'Iceland'),
        ('IN', 'India'),
        ('ID', 'Indonesia'),
        ('IR', 'Iran'),
        ('IQ', 'Iraq'),
        ('IE', 'Ireland'),
        ('IL', 'Israel'),
        ('IT', 'Italy'),
        ('JM', 'Jamaica'),
        ('JP', 'Japan'),
        ('JO', 'Jordan'),
        ('KZ', 'Kazakhstan'),
        ('KE', 'Kenya'),
        ('KI', 'Kiribati'),
        ('KP', 'Korea (North)'),
        ('KR', 'Korea (South)'),
        ('KW', 'Kuwait'),
        ('KG', 'Kyrgyzstan'),
        ('LA', 'Laos'),
        ('LV', 'Latvia'),
        ('LB', 'Lebanon'),
        ('LS', 'Lesotho'),
        ('LR', 'Liberia'),
        ('LY', 'Libya'),
        ('LI', 'Liechtenstein'),
        ('LT', 'Lithuania'),
        ('LU', 'Luxembourg'),
        ('MO', 'Macau'),
        ('MK', 'Macedonia'),
        ('MG', 'Madagascar'),
        ('MW', 'Malawi'),
        ('MY', 'Malaysia'),
        ('MV', 'Maldives'),
        ('ML', 'Mali'),
        ('MT', 'Malta'),
        ('MH', 'Marshall Islands'),
        ('MQ', 'Martinique'),
        ('MR', 'Mauritania'),
        ('MU', 'Mauritius'),
        ('YT', 'Mayotte'),
        ('MX', 'Mexico'),
        ('FM', 'Micronesia'),
        ('MD', 'Moldova'),
        ('MC', 'Monaco'),
        ('MN', 'Mongolia'),
        ('MS', 'Montserrat'),
        ('MA', 'Morocco'),
        ('MZ', 'Mozambique'),
        ('MM', 'Myanmar'),
        ('NA', 'Namibia'),
        ('NR', 'Nauru'),
        ('NP', 'Nepal'),
        ('NL', 'Netherlands'),
        ('AN', 'Netherlands Antilles'),
        ('NC', 'New Caledonia'),
        ('NZ', 'New Zealand'),
        ('NI', 'Nicaragua'),
        ('NE', 'Niger'),
        ('NG', 'Nigeria'),
        ('NU', 'Niue'),
        ('NF', 'Norfolk Island'),
        ('MP', 'Northern Mariana Islands'),
        ('NO', 'Norway'),
        ('OM', 'Oman'),
        ('PK', 'Pakistan'),
        ('PW', 'Palau'),
        ('PA', 'Panama'),
        ('PG', 'Papua New Guinea'),
        ('PY', 'Paraguay'),
        ('PE', 'Peru'),
        ('PH', 'Philippines'),
        ('PN', 'Pitcairn'),
        ('PL', 'Poland'),
        ('PT', 'Portugal'),
        ('PR', 'Puerto Rico'),
        ('QA', 'Qatar'),
        ('RE', 'Reunion'),
        ('RO', 'Romania'),
        ('RU', 'Russian Federation'),
        ('RW', 'Rwanda'),
        ('KN', 'Saint Kitts And Nevis'),
        ('LC', 'Saint Lucia'),
        ('VC', 'St Vincent/Grenadines'),
        ('WS', 'Samoa'),
        ('SM', 'San Marino'),
        ('ST', 'Sao Tome'),
        ('SA', 'Saudi Arabia'),
        ('SN', 'Senegal'),
        ('SC', 'Seychelles'),
        ('SL', 'Sierra Leone'),
        ('SG', 'Singapore'),
        ('SK', 'Slovakia'),
        ('SI', 'Slovenia'),
        ('SB', 'Solomon Islands'),
        ('SO', 'Somalia'),
        ('ZA', 'South Africa'),
        ('ES', 'Spain'),
        ('LK', 'Sri Lanka'),
        ('SH', 'St. Helena'),
        ('PM', 'St.Pierre'),
        ('SD', 'Sudan'),
        ('SR', 'Suriname'),
        ('SZ', 'Swaziland'),
        ('SE', 'Sweden'),
        ('CH', 'Switzerland'),
        ('SY', 'Syrian Arab Republic'),
        ('TW', 'Taiwan'),
        ('TJ', 'Tajikistan'),
        ('TZ', 'Tanzania'),
        ('TH', 'Thailand'),
        ('TG', 'Togo'),
        ('TK', 'Tokelau'),
        ('TO', 'Tonga'),
        ('TT', 'Trinidad And Tobago'),
        ('TN', 'Tunisia'),
        ('TR', 'Turkey'),
        ('TM', 'Turkmenistan'),
        ('TV', 'Tuvalu'),
        ('UG', 'Uganda'),
        ('UA', 'Ukraine'),
        ('AE', 'United Arab Emirates'),
        ('UK', 'United Kingdom'),
        ('US', 'United States'),
        ('UY', 'Uruguay'),
        ('UZ', 'Uzbekistan'),
        ('VU', 'Vanuatu'),
        ('VA', 'Vatican City State'),
        ('VE', 'Venezuela'),
        ('VN', 'Viet Nam'),
        ('VG', 'Virgin Islands (British)'),
        ('VI', 'Virgin Islands (U.S.)'),
        ('EH', 'Western Sahara'),
        ('YE', 'Yemen'),
        ('YU', 'Yugoslavia'),
        ('ZR', 'Zaire'),
        ('ZM', 'Zambia'),
        ('ZW', 'Zimbabwe')
        ]

lingue = [('aa', 'Afar'),
        ('ab', 'Abkhazian'),
        ('af', 'Afrikaans'),
        ('ak', 'Akan'),
        ('sq', 'Albanian'),
        ('am', 'Amharic'),
        ('ar', 'Arabic'),
        ('an', 'Aragonese'),
        ('hy', 'Armenian'),
        ('as', 'Assamese'),
        ('av', 'Avaric'),
        ('ae', 'Avestan'),
        ('ay', 'Aymara'),
        ('az', 'Azerbaijani'),
        ('ba', 'Bashkir'),
        ('bm', 'Bambara'),
        ('eu', 'Basque'),
        ('be', 'Belarusian'),
        ('bn', 'Bengali'),
        ('bh', 'Bihari languages'),
        ('bi', 'Bislama'),
        ('bs', 'Bosnian'),
        ('br', 'Breton'),
        ('bg', 'Bulgarian'),
        ('my', 'Burmese'),
        ('ca', 'Catalan; Valencian'),
        ('ch', 'Chamorro'),
        ('ce', 'Chechen'),
        ('zh', 'Chinese'),
        ('cu', 'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic'),
        ('cv', 'Chuvash'),
        ('kw', 'Cornish'),
        ('co', 'Corsican'),
        ('cr', 'Cree'),
        ('cs', 'Czech'),
        ('da', 'Danish'),
        ('dv', 'Divehi; Dhivehi; Maldivian'),
        ('nl', 'Dutch; Flemish'),
        ('dz', 'Dzongkha'),
        ('en', 'English'),
        ('eo', 'Esperanto'),
        ('et', 'Estonian'),
        ('ee', 'Ewe'),
        ('fo', 'Faroese'),
        ('fj', 'Fijian'),
        ('fi', 'Finnish'),
        ('fr', 'French'),
        ('fy', 'Western Frisian'),
        ('ff', 'Fulah'),
        ('Ga', 'Georgian'),
        ('de', 'German'),
        ('gd', 'Gaelic; Scottish Gaelic'),
        ('ga', 'Irish'),
        ('gl', 'Galician'),
        ('gv', 'Manx'),
        ('el', 'Greek, Modern (1453-)'),
        ('gn', 'Guarani'),
        ('gu', 'Gujarati'),
        ('ht', 'Haitian; Haitian Creole'),
        ('ha', 'Hausa'),
        ('he', 'Hebrew'),
        ('hz', 'Herero'),
        ('hi', 'Hindi'),
        ('ho', 'Hiri Motu'),
        ('hr', 'Croatian'),
        ('hu', 'Hungarian'),
        ('ig', 'Igbo'),
        ('io', 'Ido'),
        ('ii', 'Sichuan Yi; Nuosu'),
        ('iu', 'Inuktitut'),
        ('ie', 'Interlingue; Occidental'),
        ('ia', 'Interlingua (International Auxiliary Language Association)'),
        ('id', 'Indonesian'),
        ('ik', 'Inupiaq'),
        ('is', 'Icelandic'),
        ('it', 'Italian'),
        ('jv', 'Javanese'),
        ('ja', 'Japanese'),
        ('kl', 'Kalaallisut; Greenlandic'),
        ('kn', 'Kannada'),
        ('ks', 'Kashmiri'),
        ('ka', 'Georgian'),
        ('kr', 'Kanuri'),
        ('kk', 'Kazakh'),
        ('km', 'Central Khmer'),
        ('ki', 'Kikuyu; Gikuyu'),
        ('rw', 'Kinyarwanda'),
        ('ky', 'Kirghiz; Kyrgyz'),
        ('kv', 'Komi'),
        ('kg', 'Kongo'),
        ('ko', 'Korean'),
        ('kj', 'Kuanyama; Kwanyama'),
        ('ku', 'Kurdish'),
        ('lo', 'Lao'),
        ('la', 'Latin'),
        ('lv', 'Latvian'),
        ('li', 'Limburgan; Limburger; Limburgish'),
        ('ln', 'Lingala'),
        ('lt', 'Lithuanian'),
        ('lb', 'Luxembourgish; Letzeburgesch'),
        ('lu', 'Luba-Katanga'),
        ('lg', 'Ganda'),
        ('mk', 'Macedonian'),
        ('mh', 'Marshallese'),
        ('ml', 'Malayalam'),
        ('mi', 'Maori'),
        ('mr', 'Marathi'),
        ('ms', 'Malay'),
        ('Mi', 'Micmac'),
        ('mg', 'Malagasy'),
        ('mt', 'Maltese'),
        ('mn', 'Mongolian'),
        ('na', 'Nauru'),
        ('nv', 'Navajo; Navaho'),
        ('nr', 'Ndebele, South; South Ndebele'),
        ('nd', 'Ndebele, North; North Ndebele'),
        ('ng', 'Ndonga'),
        ('ne', 'Nepali'),
        ('nn', 'Norwegian Nynorsk; Nynorsk, Norwegian'),
        ('nb', 'Bokmål, Norwegian; Norwegian Bokmål'),
        ('no', 'Norwegian'),
        ('oc', 'Occitan (post 1500)'),
        ('oj', 'Ojibwa'),
        ('or', 'Oriya'),
        ('om', 'Oromo'),
        ('os', 'Ossetian; Ossetic'),
        ('pa', 'Panjabi; Punjabi'),
        ('fa', 'Persian'),
        ('pi', 'Pali'),
        ('pl', 'Polish'),
        ('pt', 'Portuguese'),
        ('ps', 'Pushto; Pashto'),
        ('qu', 'Quechua'),
        ('rm', 'Romansh'),
        ('ro', 'Romanian; Moldavian; Moldovan'),
        ('rn', 'Rundi'),
        ('ru', 'Russian'),
        ('sg', 'Sango'),
        ('sa', 'Sanskrit'),
        ('si', 'Sinhala; Sinhalese'),
        ('sk', 'Slovak'),
        ('sl', 'Slovenian'),
        ('se', 'Northern Sami'),
        ('sm', 'Samoan'),
        ('sn', 'Shona'),
        ('sd', 'Sindhi'),
        ('so', 'Somali'),
        ('st', 'Sotho, Southern'),
        ('es', 'Spanish; Castilian'),
        ('sc', 'Sardinian'),
        ('sr', 'Serbian'),
        ('ss', 'Swati'),
        ('su', 'Sundanese'),
        ('sw', 'Swahili'),
        ('sv', 'Swedish'),
        ('ty', 'Tahitian'),
        ('ta', 'Tamil'),
        ('tt', 'Tatar'),
        ('te', 'Telugu'),
        ('tg', 'Tajik'),
        ('tl', 'Tagalog'),
        ('th', 'Thai'),
        ('bo', 'Tibetan'),
        ('ti', 'Tigrinya'),
        ('to', 'Tonga (Tonga Islands)'),
        ('tn', 'Tswana'),
        ('ts', 'Tsonga'),
        ('tk', 'Turkmen'),
        ('tr', 'Turkish'),
        ('tw', 'Twi'),
        ('ug', 'Uighur; Uyghur'),
        ('uk', 'Ukrainian'),
        ('ur', 'Urdu'),
        ('uz', 'Uzbek'),
        ('ve', 'Venda'),
        ('vi', 'Vietnamese'),
        ('vo', 'Volapük'),
        ('cy', 'Welsh'),
        ('wa', 'Walloon'),
        ('wo', 'Wolof'),
        ('xh', 'Xhosa'),
        ('yi', 'Yiddish'),
        ('yo', 'Yoruba'),
        ('za', 'Zhuang; Chuang'),
        ('zu', 'Zulu')
        ]

gradi = [(1, "Bachelor"),(2, "Master")]

semestri = [(1, "Autumn semester"), (2, "Spring semester")]

campiDiStudio = [(1, "Economics and Management"),
                 (2, "Architecture and Design"),
                 (3, "Humanities"),
                 (4, "Engineering"),
                 (5, "Sciences and Natural Sciences"),
                 (6, "Medicine and Health Sciences"),
                 (7, "Social and Educational Sciences")]

corsi = [("Functional Materials", 1, 4, 2, 2, "en", 7.5, "https://www.ntnu.edu/studies/courses/TMT4245/2021/1#tab=omEmnet"),
         ("Industrial Systems Engineering", 1, 4, 2, 2, "en", 7.5, "https://www.ntnu.edu/studies/courses/TPK4185/2021/1#tab=omEmnet"),
         ("Tecnologie Web e Internet of Things", 2, 4, 2, 1, "it", 6, "https://offertaformativa.unimore.it/corso/insegnamento?cds_cod=1-260&aa_ord_id=2009&pds_cod=1-260-5&aa_off_id=2021&lang=ita&ad_cod=IGM-28&aa_corso=2&fac_id=10008&coorte=2020&anno_corrente=2020&durata=2")
         ]

def inserisci_elementi():
    inserisci_paesi()
    inserisci_università()
    inserisci_lingue()
    inserisci_gradi()
    inserisci_semestri()
    inserisci_campiDiStudio()
    inserisci_corsi()
    
def inserisci_università():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.executemany("INSERT INTO TABELLA_UNIVERSITÀ(NOME_UNIVERSITÀ, PAESE) VALUES(?, ?)", università)
    connessione.commit()
    cursore.close()
    connessione.close()

def inserisci_paesi():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.executemany("INSERT INTO TABELLA_PAESI(ID, PAESE) VALUES(?, ?)", paesi)
    connessione.commit()
    cursore.close()
    connessione.close()

def inserisci_lingue():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.executemany("INSERT INTO TABELLA_LINGUE(ID, LINGUA) VALUES(?, ?)", lingue)
    connessione.commit()
    cursore.close()
    connessione.close()

def inserisci_gradi():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.executemany("INSERT INTO TABELLA_GRADI(ID, GRADO) VALUES(?, ?)", gradi)
    connessione.commit()
    cursore.close()
    connessione.close()

def inserisci_semestri():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.executemany("INSERT INTO TABELLA_SEMESTRI(ID, SEMESTRE) VALUES(?, ?)", semestri)
    connessione.commit()
    cursore.close()
    connessione.close()

def inserisci_campiDiStudio():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.executemany("INSERT INTO TABELLA_CAMPI(ID, CAMPO) VALUES(?, ?)", campiDiStudio)
    connessione.commit()
    cursore.close()
    connessione.close()

def inserisci_corsi():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    cursore.executemany("INSERT INTO TABELLA_CORSI(NOME_CORSO, ID_UNIVERSITÀ, ID_CAMPO, ID_GRADO, ID_SEMESTRE, ID_LINGUA, ECTS, LINK) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", corsi)
    connessione.commit()
    cursore.close()
    connessione.close()

#---------- stampaggio tabelle ----------

def stampa():
    connessione = sqlite3.connect(url)
    cursore = connessione.cursor()
    
    print("\n---------- Università ----------")
    cursore.execute("SELECT * FROM TABELLA_UNIVERSITÀ")
    tuple_università = cursore.fetchall()
    for elemento in tuple_università:
        print(elemento)
    
    print("\n---------- Paesi ----------")
    cursore.execute("SELECT * FROM TABELLA_PAESI")
    tuple_paesi = cursore.fetchall()
    for elemento in tuple_paesi:
        print(elemento)

    print("\n---------- Lingue ----------")
    cursore.execute("SELECT * FROM TABELLA_LINGUE")
    tuple_lingue = cursore.fetchall()
    for elemento in tuple_lingue:
        print(elemento)

    print("\n---------- Gradi ----------")
    cursore.execute("SELECT * FROM TABELLA_GRADI")
    tuple_gradi = cursore.fetchall()
    for elemento in tuple_gradi:
        print(elemento)

    print("\n---------- Semestri ----------")
    cursore.execute("SELECT * FROM TABELLA_SEMESTRI")
    tuple_semestri = cursore.fetchall()
    for elemento in tuple_semestri:
        print(elemento)

    print("\n---------- Campi di studio ----------")
    cursore.execute("SELECT * FROM TABELLA_CAMPI")
    tuple_campi = cursore.fetchall()
    for elemento in tuple_campi:
        print(elemento)

    print("\n---------- Corsi ----------")
    cursore.execute("SELECT * FROM TABELLA_CORSI")
    tuple_corsi = cursore.fetchall()
    for elemento in tuple_corsi:
        print(elemento)

    connessione.commit()
    cursore.close()
    connessione.close()

#---------- main ----------
        
if __name__ == "__main__":
    crea_tabelle()
    inserisci_elementi()
    stampa()



    

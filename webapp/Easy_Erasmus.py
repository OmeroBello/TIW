from flask import Flask
from flask import render_template
from flask import request
import sqlite3

stringa_connessione = "database/Database_EE"

applicazione = Flask(__name__)

# -------------------- HOMEPAGE

# --- Flask - homepage
@applicazione.route("/")
@applicazione.route("/homepage")
def homepage():
    return render_template("homepage.html")

# ------------------------------------------------------------ INFO

# --- Flask - info
@applicazione.route("/info")
def info():
    return render_template("info.html")

# ------------------------------------------------------------ UNIVERSITY

# --- Flask - university
@applicazione.route("/university")
def university():
    return render_template("university.html")

# ------------------------------------------------------------ ADD-UNIVERSITY

# --- Flask - add-university
@applicazione.route("/add-university-page")
def add_university(messaggio = ""):
    dizionario_università = elenco_università()
    dizionario_paesi = elenco_paesi()
    return render_template("add-university.html", elenco_università = dizionario_università, elenco_paesi = dizionario_paesi, messaggio = messaggio)

# --- DB - elenco dei paesi presenti nel DB
def elenco_paesi():
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()
    cursore.execute("SELECT * FROM TABELLA_PAESI")

    lista_paesi = []
    for singolo_paese in cursore:
        paese = {
            "id_paese": singolo_paese[0],
            "nome_paese": singolo_paese[1]
            }
        lista_paesi.append(paese)

    connessione.commit()
    cursore.close()
    connessione.close()
    
    return lista_paesi

# --- Flask - funzione aggiunta università. Crea il dato dell'università nuova da inserire ed esegui add_university
@applicazione.route("/add-university", methods = ['POST'])
def aggiunti_università():
    nome_università = request.form["university_name"]
    paese_università = request.form["university_country"]
    messaggio = "University correctly added!"
    
    inserimento_università_database(nome_università, paese_università)
    
    return add_university(messaggio)

# --- DB - inserimento università nel database. Inserisci effettivamente la nuova università nel DB
def inserimento_università_database(nome_università, paese_università):
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    #inserimento università
    cursore.execute("INSERT INTO TABELLA_UNIVERSITÀ(NOME_UNIVERSITÀ, PAESE) VALUES(?, ?)", \
                    (nome_università, paese_università))
    
    connessione.commit()
    cursore.close()
    connessione.close()

# --- DB - Elenco delle università. Crea una lista delle università presenti nel DB da mostrare
def elenco_università():
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    cursore.execute("SELECT * FROM TABELLA_UNIVERSITÀ")
    lista_università = []
    for singola_università in cursore:
        università = {
            "id_università": singola_università[0],
            "nome_università": singola_università[1],
            "paese_università": singola_università[2]
            }
        lista_università.append(università)

    connessione.commit()
    cursore.close()
    connessione.close()
    
    return lista_università

# ------------------------------------------------------------ EDIT-UNIVERSITY

# --- Flask - apri la pagina di modifica ricevendo le informazioni dell'università che si vuole modificare
@applicazione.route("/edit-university-page", methods = ['POST'])
def modifica_università():
    id_università = request.form["id_università"]
    università = dettagli_università(id_università)
    dizionario_paesi = elenco_paesi()
    
    return render_template("modify-university.html", università = università, elenco_paesi = dizionario_paesi)

# --- DB - dettagli di una specifica università
def dettagli_università(id_università):
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    cursore.execute("SELECT * FROM TABELLA_UNIVERSITÀ WHERE ID = ?", (id_università,))

    università_selezionata = cursore.fetchone()
    
    università = {
            "id_università": università_selezionata[0],
            "nome_università": università_selezionata[1],
            "paese_università": università_selezionata[2]
            }
    
    return università

    connessione.commit()
    cursore.close()
    connessione.close()

# --- Flask - riceve i dati di modifica dell'utente ed esegui la relativa funzione
@applicazione.route("/edit-university", methods = ['POST'])
def edit_university():
    id_università = request.form["id_università"]
    nome_università_nuovo = request.form["new_university_name"]
    paese_università_nuovo = request.form["new_university_country"]
    messaggio = "University correctly edited!"

    modifica_università_database(id_università, nome_università_nuovo, paese_università_nuovo)

    return add_university(messaggio)

# --- DB - si vada a modificare l'università all'interno del DB
def modifica_università_database(id_università, nome_università_nuovo, paese_università_nuovo):
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    cursore.execute("UPDATE TABELLA_UNIVERSITÀ SET NOME_UNIVERSITÀ = ?, \
                    PAESE = ? WHERE ID = ?", \
                    (nome_università_nuovo, paese_università_nuovo, id_università))

    connessione.commit()
    cursore.close()
    connessione.close()

# ------------------------------------------------------------ DELETE UNIVERSITY

# --- Flask - riporta alla pagina di eliminazione di una specifica università
@applicazione.route("/delete-university-page", methods = ['POST'])
def elimina_università():
    id_università = request.form["id_università"]
    università = dettagli_università(id_università)
    dizionario_paesi = elenco_paesi()
    lista_corsi = corsi_università(id_università)
    lista_lingue = elenco_lingue()
    lista_gradi = elenco_gradi()
    lista_semestri = elenco_semestri()
    lista_campi = elenco_campi()

    return render_template("delete-university.html", università = università, elenco_paesi = dizionario_paesi,
                           corsi_università = lista_corsi,
                           elenco_lingue = lista_lingue,
                           elenco_gradi = lista_gradi,
                           elenco_semestri = lista_semestri,
                           elenco_campi = lista_campi)

# --- Flask - raccoglie i dati per l'eliminazione dell'università e 
@applicazione.route("/delete-university", methods = ["POST"])
def delete_university():
    id_università = request.form["id_università"]
    elimina_università_database(id_università)
    messaggio = "University correctly deleted!"

    return add_university(messaggio)

# --- DB - elimina definitivamente l'università selezionata dal DB e relativi corsi
def elimina_università_database(id_università):
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    cursore.execute("DELETE FROM TABELLA_UNIVERSITÀ WHERE ID = ?", (id_università,) )
    cursore.execute("DELETE FROM TABELLA_CORSI WHERE ID_UNIVERSITÀ = ?", (id_università,) )

    cursore.execute("SELECT * FROM TABELLA_CORSI")

    corsi = cursore.fetchall()
    for corso in corsi:
        print(corso)

    #quando sarà il momento, dovrò fare in modo di eliminare anche i corsi associati

    connessione.commit()
    cursore.close()
    connessione.close()

# ------------------------------------------------------------ MANAGE COURSES

# --- Flask - vai nella sezione di scelta dell'università per l'aggiunta dei suoi corsi
@applicazione.route("/choose-university")
def scelta_università():
    
    dizionario_università = elenco_università()
    dizionario_paesi = elenco_paesi()
    dizionario_corsi = elenco_corsi()
    numero_corsi_per_università = conta_corsi_università()
    
    return render_template("select-university.html", elenco_università = dizionario_università,
                           elenco_paesi = dizionario_paesi, elenco_corsi = dizionario_corsi,
                           elenco_numero_corsi_per_università = numero_corsi_per_università)

# --- DB - conta il numero di corsi di una specifica università
def conta_corsi_università():
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    cursore.execute("SELECT * FROM TABELLA_UNIVERSITÀ")
    lista_università = [] #lista di id delle università
    for singola_università in cursore:
        università = {"id_università": singola_università[0]}
        lista_università.append(università)
        print(università.get("id_università"))

    print(lista_università)
    
    numero_corsi_per_università = []
    
    for singola_università in lista_università:
        numero = cursore.execute("SELECT COUNT(*) FROM TABELLA_CORSI WHERE ID_UNIVERSITÀ = ?", (singola_università.get("id_università"),)) 
        for numerino in numero:
            print(numerino)
            università_numero_corsi = {"id_università": singola_università.get("id_università"),
                                       "numero_corsi": numerino[0]
                                       }
            numero_corsi_per_università.append(università_numero_corsi)

    print(numero_corsi_per_università)

    return numero_corsi_per_università
    
    connessione.commit()
    cursore.close()
    connessione.close()

# --- Flask - riporta alla pagina di gestione dei corsi di una specifica università
@applicazione.route("/manage-university-courses", methods = ['POST'])
def gestisci_corsi_università(messaggio = ""):
    id_università = request.form["id_università"]
    università = dettagli_università(id_università)
    lista_corsi = corsi_università(id_università)
    lista_lingue = elenco_lingue()
    lista_gradi = elenco_gradi()
    lista_semestri = elenco_semestri()
    lista_campi = elenco_campi()

    return render_template("manage-courses.html", università = università, corsi_università = lista_corsi,
                           elenco_lingue = lista_lingue,
                           elenco_gradi = lista_gradi,
                           elenco_semestri = lista_semestri,
                           elenco_campi = lista_campi,
                           messaggio = messaggio)
    
# --- DB - Elenco corsi. Crea una lista dei corsi presenti nel database
def elenco_corsi():
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    cursore.execute("SELECT * FROM TABELLA_CORSI")
    lista_corsi = []
    for singolo_corso in cursore:
        corso = {
            "id_corso": singolo_corso[0],
            "nome_corso": singolo_corso[1],
            "id_università": singolo_corso[2],
            "id_campo": singolo_corso[3],
            "id_grado": singolo_corso[4],
            "id_semestre": singolo_corso[5],
            "id_lingua": singolo_corso[6],
            "ects": singolo_corso[7],
            "link": singolo_corso[8]
            }
        lista_corsi.append(corso)

    cursore.execute("SELECT * FROM TABELLA_CORSI")
    
    corsi = cursore.fetchall()
    for corso in corsi:
        print(corso)
    
    connessione.commit()
    cursore.close()
    connessione.close()

    return lista_corsi

# --- DB - Elenco lingue. Crea una lista delle lingue presenti nel DB
def elenco_lingue():
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    cursore.execute("SELECT * FROM TABELLA_LINGUE")
    lista_lingue = []
    for singola_lingua in cursore:
        lingua = {
            "id_lingua": singola_lingua[0],
            "nome_lingua": singola_lingua[1]
            }
        lista_lingue.append(lingua)

    connessione.commit()
    cursore.close()
    connessione.close()
    
    return lista_lingue

# --- DB - Elenco dei gradi di studio. Crea una lista dei gradi presenti nel DB
def elenco_gradi():
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    cursore.execute("SELECT * FROM TABELLA_GRADI")
    lista_gradi = []
    for singolo_grado in cursore:
        grado = {
            "id_grado": singolo_grado[0],
            "nome_grado": singolo_grado[1]
            }
        lista_gradi.append(grado)

    connessione.commit()
    cursore.close()
    connessione.close()

    return lista_gradi

# --- DB - Elenco dei semestri. Crea una lista dei semestri presenti nel DB
def elenco_semestri():
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    cursore.execute("SELECT * FROM TABELLA_SEMESTRI")
    lista_semestri = []
    for singolo_semestre in cursore:
        semestre = {
            "id_semestre": singolo_semestre[0],
            "nome_semestre": singolo_semestre[1]
            }
        lista_semestri.append(semestre)

    connessione.commit()
    cursore.close()
    connessione.close()

    return lista_semestri

# --- DB - Elenco dei campi di studio. Crea una lista dei campi di studio presenti nel DB
def elenco_campi():
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    cursore.execute("SELECT * FROM TABELLA_CAMPI")
    lista_campi = []
    for singolo_campo in cursore:
        campo = {
            "id_campo": singolo_campo[0],
            "nome_campo": singolo_campo[1]
            }
        lista_campi.append(campo)

    connessione.commit()
    cursore.close()
    connessione.close()

    return lista_campi

# --- DB - ricavare i corsi di una specifica università
def corsi_università(id_università):
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()
    
    cursore.execute("SELECT * FROM TABELLA_CORSI WHERE ID_UNIVERSITÀ = ?", (id_università,))
    
    corsi_selezionati = []
    
    for singolo_corso in cursore:
        corso_selezionato = {
            "id_corso": singolo_corso[0],
            "nome_corso": singolo_corso[1],
            "id_università": singolo_corso[2],
            "id_campo": singolo_corso[3],
            "id_grado": singolo_corso[4],
            "id_semestre": singolo_corso[5],
            "id_lingua": singolo_corso[6],
            "ects": singolo_corso[7],
            "link": singolo_corso[8]
            }
        corsi_selezionati.append(corso_selezionato)
    
    return corsi_selezionati
    
    connessione.commit()
    cursore.close()
    connessione.close()

# --- Flask - funzione aggiunta corso. Crea il dato del corso nuovo da inserire ed esegui add_course
@applicazione.route("/add-course", methods = ['POST'])
def aggiungi_corso():
    nome_corso = request.form["course_name"]
    università_corso = request.form["id_università"]
    campo_corso = request.form["course_field"]
    grado_corso = request.form["course_level"]
    semestre_corso = request.form["course_semester"]
    lingua_corso = request.form["course_language"]
    ects_corso = request.form["course_ects"]
    link_corso = request.form["course_link"]
    messaggio = "Course correctly added!"
    
    inserimento_corso_database(nome_corso, università_corso, campo_corso, grado_corso,
                               semestre_corso, lingua_corso, ects_corso, link_corso)
    
    return gestisci_corsi_università(messaggio)

# --- DB - inserimento corso nel database. Inserisci effettivamente il nuovo corso nel DB
def inserimento_corso_database(nome_corso, università_corso, campo_corso, grado_corso, semestre_corso,
                               lingua_corso, ects_corso, link_corso):
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    #inserimento corso
    cursore.execute("INSERT INTO TABELLA_CORSI(NOME_CORSO, ID_UNIVERSITÀ, ID_CAMPO, ID_GRADO, \
                    ID_SEMESTRE, ID_LINGUA, ECTS, LINK) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                    (nome_corso, università_corso, campo_corso, grado_corso, semestre_corso, lingua_corso,
                     ects_corso, link_corso) )
    
    connessione.commit()
    cursore.close()
    connessione.close()

# ------------------------------------------------------------ EDIT-COURSE

# --- Flask - apri la pagina di modifica ricevendo le informazioni del corso che si vuole modificare
@applicazione.route("/edit-course-page", methods = ['POST'])
def modifica_corso():
    id_corso = request.form["id_corso"]
    corso = dettagli_corso(id_corso)
    lista_lingue = elenco_lingue()
    lista_gradi = elenco_gradi()
    lista_semestri = elenco_semestri()
    lista_campi = elenco_campi()
    lista_università = elenco_università()
    
    return render_template("modify-course.html", corso = corso, elenco_lingue = lista_lingue, elenco_gradi = lista_gradi,
                           elenco_semestri = lista_semestri, elenco_campi = lista_campi, elenco_università = lista_università)

# --- Flask - riceve i dati di modifica del corso dall'utente ed esegui la relativa funzione
@applicazione.route("/edit-course", methods = ['POST'])
def edit_course():
    id_corso = request.form["id_corso"]
    nome_corso_nuovo = request.form["new_name_corso"]
    campo_corso_nuovo = request.form["new_field_corso"]
    grado_corso_nuovo = request.form["new_level_corso"]
    semestre_corso_nuovo = request.form["new_semester_corso"]
    lingua_corso_nuova = request.form["new_language_corso"]
    ects_corso_nuovo = request.form["new_ects_corso"]
    link_corso_nuovo = request.form["new_link_corso"]
    università_corso = request.form["id_università"]
    messaggio = "Course correctly edited!"

    modifica_corso_database(id_corso, nome_corso_nuovo, campo_corso_nuovo, grado_corso_nuovo, semestre_corso_nuovo,
                            lingua_corso_nuova, ects_corso_nuovo, link_corso_nuovo, università_corso)

    return gestisci_corsi_università(messaggio)

# --- DB - si vada a modificare il corso all'interno del DB
def modifica_corso_database(id_corso, nome_corso_nuovo, campo_corso_nuovo, grado_corso_nuovo, semestre_corso_nuovo,
                            lingua_corso_nuova, ects_corso_nuovo, link_corso_nuovo, università_corso):
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    cursore.execute("UPDATE TABELLA_CORSI SET NOME_CORSO = ?, ID_UNIVERSITÀ = ?, \
                    ID_CAMPO = ?, ID_GRADO = ?, ID_SEMESTRE = ?, ID_LINGUA = ?, ECTS = ?, \
                    LINK = ? WHERE ID = ?", (nome_corso_nuovo, università_corso, campo_corso_nuovo,
                                              grado_corso_nuovo, semestre_corso_nuovo, lingua_corso_nuova,
                                              ects_corso_nuovo, link_corso_nuovo, id_corso))

    connessione.commit()
    cursore.close()
    connessione.close()

# ------------------------------------------------------------ DELETE COURSE

# --- Flask - riporta alla pagina di eliminazione di uno specifico corso
@applicazione.route("/delete-course-page", methods = ['POST'])
def elimina_corso():
    id_corso = request.form["id_corso"]
    corso = dettagli_corso(id_corso)
    lista_lingue = elenco_lingue()
    lista_gradi = elenco_gradi()
    lista_semestri = elenco_semestri()
    lista_campi = elenco_campi()
    lista_università = elenco_università()
    print(id_corso)
    return render_template("delete-course.html", corso = corso, elenco_lingue = lista_lingue, elenco_gradi = lista_gradi,
                           elenco_semestri = lista_semestri, elenco_campi = lista_campi, elenco_università = lista_università)

# --- Flask - raccoglie i dati per l'eliminazione del corso
@applicazione.route("/delete-course", methods = ["POST"])
def delete_corso():
    id_corso = request.form["id_corso"]
    id_università = request.form["id_università"]
    print(id_corso)
    elimina_corso_database(id_corso)
    messaggio = "Course correctly deleted!"
    
    return gestisci_corsi_università(messaggio)

# --- DB - elimina definitivamente il corso selezionata dal DB
def elimina_corso_database(id_corso):
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    cursore.execute("DELETE FROM TABELLA_CORSI WHERE ID = ?", (id_corso,) )
    
    connessione.commit()
    cursore.close()
    connessione.close()

# --- DB - dettagli di uno specifico corso
def dettagli_corso(id_corso):
    connessione = sqlite3.connect(stringa_connessione)
    cursore = connessione.cursor()

    cursore.execute("SELECT * FROM TABELLA_CORSI WHERE ID = ?", (id_corso,))

    corso_selezionato = cursore.fetchone()
    
    corso = {
            "id_corso": corso_selezionato[0],
            "nome_corso": corso_selezionato[1],
            "id_università": corso_selezionato[2],
            "id_campo": corso_selezionato[3],
            "id_grado": corso_selezionato[4],
            "id_semestre": corso_selezionato[5],
            "id_lingua": corso_selezionato[6],
            "ects": corso_selezionato[7],
            "link": corso_selezionato[8]
            }
    
    return corso

    connessione.commit()
    cursore.close()
    connessione.close()

# --------------------------------------------------------------------------- STUDENTI!

# --- Flask - student
@applicazione.route("/student")
def student_homepage():
    return render_template("student.html")

# --- Flask - vai nella sezione di scelta dell'università per studenti
@applicazione.route("/choose-university-student")
def scelta_università_studente():
    
    dizionario_università = elenco_università()
    dizionario_paesi = elenco_paesi()
    dizionario_corsi = elenco_corsi()
    numero_corsi_per_università = conta_corsi_università()
    
    return render_template("browse-university-student.html", elenco_università = dizionario_università,
                           elenco_numero_corsi_per_università = numero_corsi_per_università,
                           elenco_paesi = dizionario_paesi, elenco_corsi = dizionario_corsi)

# --- Flask - riporta alla pagina di visualizzazione dei corsi di una specifica università
@applicazione.route("/see-courses-student", methods = ['POST'])
def visualizza_corsi_studente():
    id_università = request.form["id_università"]
    università = dettagli_università(id_università)
    lista_corsi = corsi_università(id_università)
    lista_lingue = elenco_lingue()
    lista_gradi = elenco_gradi()
    lista_semestri = elenco_semestri()
    lista_campi = elenco_campi()

    return render_template("browse-courses-student.html", università = università, corsi_università = lista_corsi,
                           elenco_lingue = lista_lingue,
                           elenco_gradi = lista_gradi,
                           elenco_semestri = lista_semestri,
                           elenco_campi = lista_campi)

# --- Flask - LA
@applicazione.route("/LA")
def LA():
    lista_università = elenco_università()
    lista_corsi = elenco_corsi()
    
    return render_template("LA.html", elenco_università = lista_università, elenco_corsi = lista_corsi)

# --- Flask - prende in pasto le università scelte dallo studente e dà la possibilità di scegliere tra i loro corsi
@applicazione.route("/set-LA-universities", methods = ['POST'])
def corsi_sending_receiving():
    id_università_sending = int(request.form["sending_university"]) #ho dovuto convertire in integer perché il dato preso dalla select non è int, mentre l'id dell'uni è int, quindi non riuscivo a confrontarli
    id_università_receiving = int(request.form["receiving_university"])
    lista_corsi_sending = corsi_università(id_università_sending)
    lista_corsi_receiving = corsi_università(id_università_receiving)
    lista_università = elenco_università()
    lista_corsi = elenco_corsi()
    print(id_università_sending)
    print(id_università_receiving)
    print(lista_università)

    return render_template("LA-setted.html", elenco_corsi_sending = lista_corsi_sending,
                           elenco_corsi_receiving = lista_corsi_receiving,
                           id_sending = id_università_sending,
                           id_receiving = id_università_receiving,
                           elenco_università = lista_università,
                           elenco_corsi = lista_corsi)

if __name__ == "__main__":
    applicazione.run()

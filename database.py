import psycopg2



try:

    connexion = psycopg2.connect(
        host="localhost",
        dbname="etudiants",
        user="postgres",
        password="postgres",
        port="5432"
    )

    curseur = connexion.cursor()

    print("Connexion réussie")

except Exception as erreur:

    print("Erreur de connexion :", erreur)


#creation des tables

requete="""
create table IF NOT EXISTS classe (
id_classe serial NOT NULL PRIMARY KEY,
nom_classe VARCHAR(30)
)
"""
curseur.execute(requete)
requete="""
create table IF NOT EXISTS etudiant(
id_etudiant SERIAL NOT NULL PRIMARY KEY,
nom varchar(10) NOT NULL,prenom varchar(10) NOT NULL,
numero varchar(7) UNIQUE NOT NULL,
id_classe int, 
foreign key(id_classe) references classe(id_classe),
est_archive BOOLEAN
)
"""
curseur.execute(requete)
requete="""
create table IF NOT EXISTS matiere(
id_matiere SERIAL NOT NULL PRIMARY KEY,
nom_matiere VARCHAR(50)NOT NULL)
)
"""
curseur.execute(requete)
requete="""
create table IF NOT EXISTS Note(
id_note SERIAL NOT NULL PRIMARY KEY,
note_examen float NOT NULL default 0.0,
id_etudiant int ,foreign key(id_etudiant) references etudiant(id_etudiant),
id_matiere int,
foreign key(id_matiere) references matiere(id_matiere)
)
"""
curseur.execute(requete)
requete="""
create table IF NOT EXISTS devoir(
id_devoir SERIAL NOT NULL PRIMARY KEY,
id_note int,
foreign key (id_note) references Note(id_note),
note_devoir float NOT NULL default 0.0
)
"""
curseur.execute(requete)
connexion .commit()
curseur.close() 
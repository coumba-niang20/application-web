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


#mmethode 
requete="create table matiere(id SERIAL, nom varchar(10),prenom varchar(10))"
curseur.execute(requete)
#meth
curseur.execute("dcs,bfqdjknfqkfbqdj;frkfjbbfkjsdnkg,glksn")



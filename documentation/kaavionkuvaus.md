## LIIKESEURANTA-PALVELU |TIETOKANTASOVELLUS - TIETOKANTAKAAVION KUVAUS
#### Vuorenmaa, Kaisla M
#### Helsingin Yliopisto | 1. periodi 2019

### Kuvaus Sovelluksen Tietokantakaaviosta

Tietokanta koostuu viidestä tietokantataulusta, joista yksi on liitostaulu ja yksi kuvaa käyttäjää:

Liike-luokka sisältää pääavaimen(id).
Attribuutteina sillä on liikkeen nimi, sen vaikeusarvo, kuvaus liikkeestä ja teline, jolla liike suoritetaan.
               
Voimistelija-luokka sisältää pääavaimen(id) ja viiteavaimet vastuuvalmentaja_id sekä ryhma_id. Luokalla on lisäksi attribuutit nimi ja valmentaja, jotka kertovat voimistelijasta.

VoimistelijaLiike- taulu on liitostaulu voimistelijan ja liikkeen välillä sisältäen niihin viiteavaimet.

Ryhmä-taulu sisältää pääavaimen(id) ja viiteavaimen vastuuvalmentaja_id, ryhmän nimen. 
   
Vastuuvalmentaja(käyttäjä)-luokka sisältää pääavaimen(id) ja attribuuttina nimen, salasanan ja käyttäjätunnuksen.


### CREATE TABLE -lauseet

###### Vastuuuvalmentaja 

CREATE TABLE vastuuvalmentaja (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
)

###### Liike 

CREATE TABLE liike (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        nimi VARCHAR(144) NOT NULL, 
        teline VARCHAR(144) NOT NULL, 
        vaikeusarvo VARCHAR(144) NOT NULL, 
        kuvaus VARCHAR(500), 
        PRIMARY KEY (id)
)

###### Ryhmä 

CREATE TABLE ryhma (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        ryhma VARCHAR(144) NOT NULL, 
        vastuuvalmentaja_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(vastuuvalmentaja_id) REFERENCES vastuuvalmentaja (id)
)

###### Voimistelija

CREATE TABLE voimistelija (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        nimi VARCHAR(144) NOT NULL, 
        vastuuvalmentaja_id INTEGER NOT NULL, 
        ryhma_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(vastuuvalmentaja_id) REFERENCES vastuuvalmentaja (id), 
        FOREIGN KEY(ryhma_id) REFERENCES ryhma (id)
)

###### VoimistelijaLiike 

CREATE TABLE voimistelijaliike (
        voimistelija_id INTEGER, 
        liike_id INTEGER, 
        FOREIGN KEY(voimistelija_id) REFERENCES voimistelija (id), 
        FOREIGN KEY(liike_id) REFERENCES liike (id)
)
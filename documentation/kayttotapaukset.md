## LIIKESEURANTA-PALVELU |TIETOKANTASOVELLUS - KÄYTTÖTAPAUKSET
#### Vuorenmaa, Kaisla M
#### Helsingin Yliopisto | 1. periodi 2019

### Käyttötapaukset
#### User storyt:

* Valmentaja voi kirjautua järjestelmään
* Valmentaja voi lisätä liikkeitä, joille voi antaa ominaisuuksia, kuten vaikeusarvon
* Valmentaja voi lisätä voimistelijoita itse lisäämiinsä ryhmiin
* Valmentaja voi poistaa itse lisäämiään voimistelijoita järjestelmästä
* Valmentaja voi lisätä ryhmiä järjestelmään
* Valmentaja voi poistaa itse lisäämiään ryhmiä järjestelmästä
* Valmentaja voi tarkastella kaikkia lisättyjä voimistelijoita, vaikka ei olisi itse lisännyt kaikkia niistä
* Valmentaja voi tarkastella kaikkia lisättyjä ryhmiä, vaikka ei olisi itse lisännyt kaikkia niistä
* Valmentaja voi muokata voimistelijoiden tietoja järjestelmässä, esimerkiksi vaihtaa ryhmän nimeä
* Valmentaja voi tarkastella ryhmien tietoja ja nähdä esimerkiksi kuhunkin ryhmään lisätyt voimistelijat ja heidän suorittamansa liikkeet
* Valmentaja voi lisätä voimistelijalle, jonka on itse lisännyt järjestelmään, uuden harjoiteltavan liikkeen

### Käyttötapausten SQL -kyselyt

Uusia asioita tauluihin lisättäessä, lisätään automaattisesti myös mm. id ja luontiaika.

* Valmentaja voi kirjautua järjestelmään:

INSERT INTO Vastuuvalmentaja (name, username, password) VALUES ('nimi', 'käyttäjä', 'salasana');


* Valmentaja voi lisätä liikkeitä, joille voi antaa ominaisuuksia, kuten vaikeusarvon:

INSERT INTO Liike (nimi, teline, vaikeusarvo, kuvaus) VALUES ('nimi', 'teline', 'arvo', 'kuvaus');


* Valmentaja voi lisätä voimistelijoita itse lisäämiinsä ryhmiin:

INSERT INTO Voimistelija (nimi, valmentaja_id, ryhma_id) VALUES ('nimi', 'nykyinen käytttäjä id', 'ryhma_id');


* Valmentaja voi poistaa itse lisäämiään voimistelijoita järjestelmästä:

DELETE FROM Voimistelija where id = 'id'


* Valmentaja voi lisätä ryhmiä järjestelmään:

INSERT INTO Ryhma (nimi, valmentaja_id) VALUES ('nimi', 'nykyinen käyttäjä id');


* Valmentaja voi poistaa itse lisäämiään ryhmiä järjestelmästä:

Ensin muutetaan ryhmän voimistelijoiden ryhma_id = -1
UPDATE(Voimistelija).where(Voimistelija.ryhma_id==ryhma_id).\values(ryhma_id='-1')

Tämän jälkeen vasta varsinainen ryhmän poisto:
DELETE FROM Ryhma where id = 'id'


* Valmentaja voi tarkastella kaikkia lisättyjä voimistelijoita, vaikka ei olisi itse lisännyt kaikkia niistä:

SELECT * FROM Voimistelija


* Valmentaja voi tarkastella kaikkia lisättyjä ryhmiä, vaikka ei olisi itse lisännyt kaikkia niistä:

SELECT * FROM Ryhma


* Valmentaja voi muokata voimistelijoiden tietoja järjestelmässä, esimerkiksi vaihtaa ryhmän nimeä:

UPDATE(Voimistelija).where(Voimistelija.id=='id').\values(ryhma_id='uuden ryhmän id')


* Valmentaja voi tarkastella ryhmien tietoja ja nähdä esimerkiksi kuhunkin ryhmään lisätyt voimistelijat ja heidän suorittamansa liikkeet:

"SELECT Liike.nimi AS 'Liike', Liike.teline AS 'Teline', Liike.vaikeusarvo AS 'Vaikeus' FROM Liike"
                    "INNER JOIN VoimistelijaLiike ON VoimistelijaLiike.liike_id = Liike.id"
                    "INNER JOIN Voimistelija ON Voimistelija.id= VoimistelijaLiike.voimistelija_id"
                    "INNER JOIN Ryhma ON Ryhma.id= Voimistelija.ryhma_id"
                    "WHERE Ryhma.id= 'id'"
                    "GROUP BY Liike.nimi"
                    
"SELECT Liike.id, Liike.nimi, Liike.teline  FROM Liike"


* Valmentaja voi lisätä voimistelijalle, jonka on itse lisännyt järjestelmään, uuden harjoiteltavan liikkeen:

INSERT INTO VoimistelijaLiike (voimistelija_id, liike_id) VALUES ('voimisteiljan id', 'liikkeen id');

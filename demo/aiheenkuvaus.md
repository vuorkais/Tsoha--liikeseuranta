## LIIKESEURANTA- PALVELU
## TIETOKANTASOVELLUS - AIHEKUVAUS
#### Vuorenmaa, Kaisla M
#### Helsingin Yliopisto | 1. periodi 2019

### Aihe harjoitustyölle

Tietokantasovelluksen harjoitustyöni on telinevoimisteluun erikoistunut liikeseurantasovellus. 
Telinevoimistelijoilla on useita eri liikkeitä, joita he harjoittelevat (kullakin eri liikkeet keskenään) 
ja valmentajana on hyödyllistä tehdä jonkinlaista seurantaa siitä, kuinka liikkeen harjoittelu edistyy. 
Tietokannassani voidaan lisätä voimistelijoita ja liikkeitä. 
Näiden välille tulee vaadittu monesta moneen suhde (koska voimistelijalla voi olla harjoiteltavissa useita liikkeitä 
ja taas toisaalta liike voi yhdistyä useaan eri voimistelijaan). 
Liikkeestä voidaan kirjata ylös sen vaikeusarvo, kuvaus liikkeen suorituksesta ja teline, jolla liike suoritetaan. 
Lisäksi on kolmas tietokantataulu suoritus, johon voidaan merkitä kunkin harjoituskerran osalta jokaisen 
liikkeen suoritukseen liittyvää dataa. Siis esimerkiksi maanantaina Nojapuilla Viivi Voimistelija on harjoitellut kieppiä. 
Hän on suorittanut 5 kertaa onnistuneesti kiepin, mutta yrittänyt kieppiä 8 kertaa. 
Suoritusten jälkeen voidaan merkitä ylös onnistuneet ja tehdyt suoritukset ja mahdolliset muut kommentit. 
Esimerkiksi, jos suoritus on tehty avustuksella tai siihen on käytetty lisämattoja. 
Näin saadaan valmentajalle seurantatyökalu, jolla pysyä ajan tasalla voimistelijoidensa liikkeiden harjoittelusta.

Liike-luokka sisältää pääavaimen(id).
Attribuutteina sillä on liikkeen nimi, sen vaikeusarvo, kuvaus liikkeestä ja teline, jolla liike suoritetaan.

Suoritus-luokka sisältää pääavaimen(id), ja viiteavaimet liike_id ja voimistelija_id. 
Luokalla on lisäksi useita attribuutteja, jotka kertovat suoritukseen liittyvistä yksityiskohdista.
               
Voimistelija-luokka sisältää pääavaimen(id) ja viiteavaimen vastuuvalmentaja_id. Luokalla on lisäksi attribuutit nimi, ryhmä ja valmentaja, jotka kertovat voimistelijasta.
VoimistelijaLiike- taulu on liitostaulu voimistelijan ja liikkeen välillä sisältäen niihin viiteavaimet.
   
Vastuuvalmentaja(käyttäjä)-luokka sisältää pääavaimen(id) ja attribuuttina nimen.

##### Toimintoja:
* Kirjautuminen
* Liikkeen syöttö ja muokkaus
* Uuden voimistelijan syöttö ja muokkaus
* Suorituksen lisääminen ja poistaminen
* Mahdollisuus saada lista voimistelijoista, liikkeistä ja suorituskerroista
* Mahdollisuus järjestää em. listoja esimerkiksi ryhmien tai onnistumiskertojen perusteella 

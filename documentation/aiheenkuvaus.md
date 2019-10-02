## LIIKESEURANTA-PALVELU |TIETOKANTASOVELLUS - AIHEKUVAUS
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
liikkeen suoritukseen liittyvää dataa. Lisäksi on luokat ryhmä ja vastuuvalmentaja(käyttäjä).

Siis esimerkiksi maanantaina Nojapuilla Viivi Voimistelija on harjoitellut kieppiä. 
Hän on suorittanut 5 kertaa onnistuneesti kiepin, mutta yrittänyt kieppiä 8 kertaa. 
Suoritusten jälkeen voidaan merkitä ylös onnistuneet ja tehdyt suoritukset ja mahdolliset muut kommentit. 
Esimerkiksi, jos suoritus on tehty avustuksella tai siihen on käytetty lisämattoja. 
Näin saadaan valmentajalle seurantatyökalu, jolla pysyä ajan tasalla voimistelijoidensa liikkeiden harjoittelusta.

Liike-luokka sisältää pääavaimen(id).
Attribuutteina sillä on liikkeen nimi, sen vaikeusarvo, kuvaus liikkeestä ja teline, jolla liike suoritetaan.

Suoritus-luokka sisältää pääavaimen(id), ja viiteavaimet liike_id ja voimistelija_id. 
Luokalla on lisäksi useita attribuutteja, jotka kertovat suoritukseen liittyvistä yksityiskohdista.
               
Voimistelija-luokka sisältää pääavaimen(id) ja viiteavaimet vastuuvalmentaja_id sekä ryhma_id. Luokalla on lisäksi attribuutit nimi ja valmentaja, jotka kertovat voimistelijasta.

VoimistelijaLiike- taulu on liitostaulu voimistelijan ja liikkeen välillä sisältäen niihin viiteavaimet.

Ryhmä-taulu sisältää pääavaimen(id) ja viiteavaimen vastuuvalmentaja_id, ryhmän nimen. 
   
Vastuuvalmentaja(käyttäjä)-luokka sisältää pääavaimen(id) ja attribuuttina nimen, .

#### User storyt:
* Valmentaja voi kirjautua järjestelmään
* Valmentaja voi lisätä liikkeitä, joille voi antaa ominaisuuksia, kuten vaikeusarvon
* Valmentaja voi poistaa liikkeitä, joille voi antaa ominaisuuksia, kuten vaikeusarvon
* Valmentaja voi lisätä voimistelijoita järjestelmään
* Valmentaja voi poistaa voimistelijoita järjestelmästä
* Valmentaja voi muokata voimistelijoiden tietoja järjestelmässä, esimerkiksi vaihtaa ryhmän nimeä
* Valmentaja voi lisätä voimistelijalle suorituksia järjestelmään
* Valmentaja voi poistaa suorituksia järjestelmästä
* Valmentaja voi muokata tehtyjä suorituksia jälkikäteen
* Valmentaja voi tehdä listoja voimistelijoiden suorituksista
* Valmentaja voi järjestellä tekemiään listoja esimerkiksi ryhmien perusteella
* Valmentaja voi tarkastella voimistelijoiden suorituksia ja liikkeitä
* Valmentaja voi seurata voimistelijan edistymistä listaamalla onnistumisprosentin

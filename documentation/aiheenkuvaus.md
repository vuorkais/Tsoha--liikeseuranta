## LIIKESEURANTA-PALVELU |TIETOKANTASOVELLUS - AIHEKUVAUS
#### Vuorenmaa, Kaisla M
#### Helsingin Yliopisto | 1. periodi 2019

### Aihe harjoitustyölle

Tietokantasovelluksen harjoitustyöni on telinevoimisteluun erikoistunut liikeseurantasovellus. 
Telinevoimistelijoilla on useita eri liikkeitä, joita he harjoittelevat (kullakin eri liikkeet keskenään) 
ja valmentajana on hyödyllistä tehdä jonkinlaista seurantaa siitä, mitä liikkeitä kukin voimistelija harjoittelee tai mitä liikkeitä tietyssä ryhmässä harjoitellaan.

Tietokannassani voidaan lisätä voimistelijoita ja liikkeitä. 
Näiden välille tulee vaadittu monesta moneen suhde (koska voimistelijalla voi olla harjoiteltavissa useita liikkeitä 
ja taas toisaalta liike voi yhdistyä useaan eri voimistelijaan). 
Liikkeestä voidaan kirjata ylös sen vaikeusarvo, kuvaus liikkeen suorituksesta ja teline, jolla liike suoritetaan. 
Lisäksi on luokat ryhmä ja vastuuvalmentaja(käyttäjä).

Liike-luokka sisältää pääavaimen(id).
Attribuutteina sillä on liikkeen nimi, sen vaikeusarvo, kuvaus liikkeestä ja teline, jolla liike suoritetaan.
               
Voimistelija-luokka sisältää pääavaimen(id) ja viiteavaimet vastuuvalmentaja_id sekä ryhma_id. Luokalla on lisäksi attribuutit nimi ja valmentaja, jotka kertovat voimistelijasta.

VoimistelijaLiike- taulu on liitostaulu voimistelijan ja liikkeen välillä sisältäen niihin viiteavaimet.

Ryhmä-taulu sisältää pääavaimen(id) ja viiteavaimen vastuuvalmentaja_id, ryhmän nimen. 
   
Vastuuvalmentaja(käyttäjä)-luokka sisältää pääavaimen(id) ja attribuuttina nimen, salasanan ja käyttäjätunnuksen.

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

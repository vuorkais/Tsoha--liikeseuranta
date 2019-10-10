## LIIKESEURANTA-PALVELU |TIETOKANTASOVELLUS - ASENNUSOHJE
#### Vuorenmaa, Kaisla M
#### Helsingin Yliopisto | 1. periodi 2019

### Ohje Sovelluksen Asennukseen

##### Paikallisen käytön asennus

1. ALoita käytön asennus lataamalla tai päivittämällä python3 ja sqlite3, mikäli ne eivät jo ole ajan tasalla. Myös Flaskin tai riippuvuuksien asennus tai päivitys saattaa olla ajankohtaista tässä vaiheessa ja sen voi tehdä komennoilla `pip install Flask`, jonka jälkeen `pip install requirements.txt`. Tarkista, ettei requirements.txt tiedostoon jää pkg-resources==0.0.0 -nimistä riviä.

2. Seuraavaksi lataa githubista Liikeseurantasovellus koneellesi pakattuna tiedostona ja pura se haluamaasi kohteeseen. Suunnista kansioon terminaalissa ja aja komento `python -m venv venv`.

3. Käynnistä venv komennolla `source venv/bin/activate`.

4. Nyt sovelluksen voi käynnistää paikallisesti komennolla `python3 run.py`. Sovellus löytyy tulosteen mukaisesta osoitteesta: http://127.0.0.1:5000



##### Herokun käytön asennus

1. Tarkista, että Flask on käytössä ja paikallisen käytön asennus on tehty 3. kohtaan asti. Tämän jälkeen voit asentaa Gunicorn-palvelimen komennolla `pip install qunicorn`. 

2. Jotta heroku toimisi, tulee luoda Procfile-tiedosto esimerkiksi komennolla: `echo "web: gunicorn --preload --workers 1 application:app" > Procfile`.

3. Sovelluksen käyttöä varten tulee luoda käyttäjätili herokuun esimerkiksi www.heroku.com ja seurata sieltä ohjeita sovelluksen ja tarvittavien työkalujen asentamiseen tietokoneelle.

4. Luo herokuun uusi sovelluspaikka (esimerkiksi herokun nettisivujen ohjeita seuraten), jonne tuot sovelluksen. Voit myös tehdä vaiheen komentoriviltä seuraavin komennoin: 
*`$ git remote add heroku osoite` 
*`$ git add .`
*`$ git commit -m "Sovelluksen siirto herokuun"`
*`$ git push heroku master`

5. Jos psycopg2 ei ole vielä asennettuna, asenna se esimerkiksi komennolla: `pip install psycopg2`.

6. Määritellään Herokuun ympäristömuuttuja ja luodaan tietokanta:
*`heroku config:set HEROKU=1`
*`heroku addons:add heroku-postgresql:hobby-dev`

Nyt sovelluksen pitäisi olla toiminnassa myös Herokussa

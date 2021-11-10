# Kiosk mode med automatisk pålogging for Chromium

| Utstyr | Links |
| ------ | ------ |
| Python3 | [Følger med Raspberry OS] |
| Selenium | [https://selenium-python.readthedocs.io/installation.html] |
| web.py | [[https://github.com/TheLonelyPug/UiAKioskMode/blob/main/web.py/] |
| config.py | [https://github.com/TheLonelyPug/UiAKioskMode/blob/main/config.py/] |
| SelectorsHub | [https://github.com/TheLonelyPug/UiAKioskMode/blob/main/web.py] |

## Oppsett

web.py

```sh
Opprett web.py eller kiosk.py på Raspberry Pi med å skrive touch web.py i terminal

Kan kalle filen det du vil så lenge du vet hva den heter

Kopier koden fra lenken til web.py som står oppført i utstyr listen

nano web.py i terminalen og lim inn koden

ctrl+x, y og enter slik at det lagres og lukkes 

Derretter må du benytte deg av SelectorsHub til å finne Rel XPath ved å gå til nettsiden du ønsker å ha i kiosk mode

Høreklikk over username feltet slik som i bildet nedenfor og gå til SelectorsHub, og klikk "Copy Rel XPath"
```
![image](https://user-images.githubusercontent.com/33001277/141118330-b59f450a-c6e7-418e-b58e-7b18d28127ab.png)

```sh
Lim dette inn der det står "XPATH bane"

En til bruker, en til passord og en til påloggingsknappen

Hver av disse har forskjellige Rel XPaths så du må kopiere fra bruker, pass og knapp slik at den vet hvor den skal gå
for å fylle ut

Det vil bli noe lignende som denne
```
![image](https://user-images.githubusercontent.com/33001277/141119233-df6ef21b-deea-4f80-bdb7-3ab83d61e97f.png)

config.py

```sh
Gjør det samme med å opprette config.py fil med touch kommandoen

Kopier config.py filen fra lenken i utstyr kolonnen

Endre lenke til nettsiden du ønsker at den skal peke til

Fyll ut brukernavn og passord i de to neste kolonnene og lagre filen
```

crontab

```sh
crontab -e

Velg nano som editor

Kopier og lim inn dette inn i bunnen av crontab filen:

@reboot env -i DISPLAY=:0.0 XAUTHORITY="$XAUTHORITY" /usr/bin/python3 /home/pi/web.py

Slik som bildet
```
![image](https://user-images.githubusercontent.com/33001277/141115863-ed1cc9bd-f382-4248-a33b-38ef469f99db.png)

```sh
Derretter trykker du ctrl+x, y og enter slik at man lagrer endringer og kommer seg ut av crontab

Så er det bare å starte RPi-en på nytt
```

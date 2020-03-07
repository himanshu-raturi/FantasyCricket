# Fantasy Cricket Application
![images (14)](https://user-images.githubusercontent.com/27719791/76102964-d34f3b00-5ff6-11ea-9b7c-6bd5f437ef4b.jpeg)
----

> Fantasy Cricket Application is an online game where you create a virtual team of real cricket players and score points depending on how your chosen players perform in real life matches. To win a tournament, you must try and get the maximum points and the No. 1 rank amongst other participants!!!....Isn't it exciting.....

---


## Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [Use of Badges](#use-of-badges)
- [Features](#features)
- [Installation](#installation)
- [Code Snippet](#code-snippet)
- [Getting Started](#getting-started)
- [Tools](#tools)



---

## Description
> Fanatsy cricket is build in python using `Pyqt5` library specifically `QtCore`  `QtGui`  `QtWidgets` for **GUI** development and `SqliteStudio` for **Back end database connectivity**.


---

### Use of Badges

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![Github Issues](http://githubbadges.herokuapp.com/badges/badgerbadgerbadger/issues.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger/issues)  [![Badges](http://img.shields.io/:badges-9/9-ff6799.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger)

- For more on these wonderful `badges`, refer to <a href="http://badges.github.io/badgerbadgerbadger/" target="_blank">`badgerbadgerbadger`</a>.



![st1](https://user-images.githubusercontent.com/27719791/76096054-684c3700-5feb-11ea-9b35-8c8093893e56.png)

![Screenshot_20200307_095958](https://user-images.githubusercontent.com/27719791/76096032-5cf90b80-5feb-11ea-8dff-479357cd41ea.png)


## Features
  * Create your own dream team in Auction
  * Save your team and evaluate it later as per **Match**
  * Initially a Owner will be provided with `1000 Points` to purchase there players
  * Team selection follows basic cricketing rules 
  * Not more than 5 batsman/bowler
  * Only a Single Wicket Keeper
  * if the game logic is not followed error message occurred.





## Installation
* install `PyQt5` python library using pip
```python
pip install PyQt5

```
or
```python
pip3 install PyQt5

```
* Install SqliteStudio for creating database for the `teams` , `players` , `stats`

- Download Sqlite Studio - [Sqlitestudio](https://sqlitestudio.pl/index.rvt)





## Code Snippet

```python
 for i in range(self.listWidget.count()):
            ttl, batscore, bowlscore, fieldscore=0,0,0,0
            nm=self.listWidget.item(i).text()
            cursor=conn.execute("select * from "+match+" where player='"+nm+"'")
            row=cursor.fetchone()
            batscore=int(row[1]//2)
            if batscore>=50: batscore+=5
            if batscore>=100: batscore+=10
            if row[2]>0:
                sr=(row[1]/row[2])*100
                if sr>=80: batscore+=2
                if sr>=100:batscore+=4
            batscore+=row[3]
            batscore+=2*row[4]
            bowlscore=row[8]*10
            if row[8]>=3: bowlscore=bowlscore+5
            if row[8]>=5: bowlscore=bowlscore+10
            if row[5]>0:
                er=row[7]/row[5]
                if er<=2: bowlscore=bowlscore+10
                elif er>2 and er<=3.5: bowlscore=bowlscore+7
                elif er>3.5 and er<=4.5: bowlscore=bowlscore+4
            fieldscore=(row[9]+row[10]+row[11])*10            
            ttl=batscore+bowlscore+fieldscore
            self.listWidget_2.addItem(str(ttl))
            teamttl=teamttl+ttl
        self.label_5.setText(str(teamttl))




---
```
## Getting Started
```
git clone https://github.com/himanshurishikesh731/TrainingFantasyCricket.git
```
* install the required tools 

* fork or download the repo 

* run the following command in terminal

```
python3 FantasyCricket.py
```


![summer-training-project (1)](https://user-images.githubusercontent.com/27719791/76101808-05f83400-5ff5-11ea-9db2-05d11a11f738.gif)



## Tools
### References
* [PyQt](https://riverbankcomputing.com/software/pyqt/intro)
* [Sublime Text](https://www.sublimetext.com/3)
* [SqliteStudio](https://sqlitestudio.pl/index.rvt)
* [Internshala-Summer-Trainings](https://trainings.internshala.com/python-training)
* [Python](https://www.python.org/)



---



## License
---
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)


[Back To The Top](#Fantasy-Cricket-Application)

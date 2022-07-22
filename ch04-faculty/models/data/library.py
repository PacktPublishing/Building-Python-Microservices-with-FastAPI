from enum import Enum

class Classification(str, Enum): 
    Non_Fiction='Non-Fiction'
    Fiction='Fiction'
    Science='Science'
    Technology='Technology'
    History='History'
    Arts='Arts'
    Music='Music'
    Travels='Travels'
    Food='Food'
    Engineering='Engineering'
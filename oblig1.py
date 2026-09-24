'''
Sammenligning av elbil og bensinbil
Obligatorisk oppgave 1 PY1010 høsten 2026
Av Anja Bjølgerud
abj@usn.no
'''

#%%  Data
kjørelengde = 12000 # [km/år]

forsikring_el = 5000 # [kr/år]
forsikring_bensin = 7500 # [kr/år]

trafikkforsikringsavgift = 8.38*365 # [kr/år]

drivstoffbruk_el = 0.2 # [kWh/km]
strømpris = 2.00 # [kr/kWh]
drivstoffkostnad_el = drivstoffbruk_el * strømpris * kjørelengde # [kr/år]

pris_bensin = 1.0 # [kr/km]
drivstoffkostnad_bensin = pris_bensin * kjørelengde # [kr/år]

bomavgift_el = 0.1 * kjørelengde # [kr/år]
bomavgift_bensin = 0.3 * kjørelengde # [kr/år]


#%%  Totalkostnad
totalkostnad_el = forsikring_el + trafikkforsikringsavgift + drivstoffkostnad_el + bomavgift_el
totalkostnad_bensin = forsikring_bensin + trafikkforsikringsavgift + drivstoffkostnad_bensin + bomavgift_bensin

#%%  Differanse
differanse = totalkostnad_bensin - totalkostnad_el

#%%  Print
print ("Sammenligning av årlige kostnader for elbil og bensinbil ved kjørelengde", kjørelengde, "km/år")
print ("Totalkostnad for elbil er", totalkostnad_el,"kroner per år")
print ("Totalkostnad for bensinbil er", totalkostnad_bensin,"kroner per år")
print ("Differansen er =", abs(differanse), "kroner")

if totalkostnad_el < totalkostnad_bensin:
    print ("Elbil har lavest totalkostnad")
elif totalkostnad_el > totalkostnad_bensin:
    print ("Bensinbil har lavest totalkostnad")
elif totalkostnad_el == totalkostnad_bensin:
    print("Kostnadene for elbil og bensinbil er like")

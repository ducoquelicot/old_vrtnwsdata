#%%
import pandas as pd 
%matplotlib inline
nationaliteiten = pd.read_csv('nieuwe_buren/nationaliteiten.csv')

#%%
nationaliteiten.columns

#%%
nationaliteiten = nationaliteiten.melt(id_vars=['niscode', 'woonplaats', 'jaar', 'geslacht'], value_vars=['totaal', 'belgie', 'europa', 'duitsland', 'oostenrijk', 'bulgarije', 'cyprus', 'denemarken', 'spanje', 'finland', 'frankrijk', 'verenigd_koninkrijk', 'luxemburg', 'griekenland', 'hongarije', 'ierland', 'malta', 'portugal', 'roemenie', 'zweden', 'italie', 'nederland', 'letland', 'estland', 'litouwen', 'polen', 'tsjechie', 'slowakije', 'kroatie', 'slovenie', 'albanie', 'noorwegen', 'zwitserland', 'serbiemontenegro', 'belarus', 'oekraine', 'rusland', 'noordmacedonie', 'bosnieherzegovina', 'montenegro', 'servie', 'kosovo', 'exjoegoslavie', 'extsjechoslowakije', 'exsovjet', 'ander_europa', 'azie', 'zuidkorea', 'india', 'indonesie', 'japan', 'nepal', 'filipijnen', 'china', 'vietnam', 'kazachstan', 'kirgizie', 'oezbekistan', 'thailand', ])
# Importação de bilbiotecas 
import pdfplumber
import pandas as pd
import numpy as np
import os
import re

folder = "/Users/leonardoyada/Desktop/dados/RREO/"

my_series = []
dfFinalanalise = pd.DataFrame()

for name in os.listdir(folder): 
    if not name.startswith('.') and os.path.isfile(os.path.join(folder, name)):

        PDFfile = os.path.join(folder, name)
        print(PDFfile)

        ANO = PDFfile[-8]+PDFfile[-7]+PDFfile[-6]+PDFfile[-5]
        UF = PDFfile[-13]+PDFfile[-12]

        # Extração da tabela da primeira página do Anexo 08 do RREO
        ANO = int(ANO)
        UF = UF
        
        if (ANO > 2016) & (ANO <= 2020):

            with pdfplumber.open(PDFfile) as pdf:
                for n in range(0, 5, 1):
                    page = pdf.pages[n].extract_tables()
                    for i in range(len(page)):
                        for z in range(len(page[i])):
                            if ('37- TOTAL DAS DESPESAS PARA FINS DE LIMITE (29 - 36)6' in page[i][z]) | ('38- TOTAL DAS DESPESAS PARA FINS DE LIMITE (29 - 37)6' in page[i][z]) | ('38- MÍNIMO DE 25% DAS RECEITAS RESULTANTES DE IMPOSTOS EM MDE ((37) / (4) x 100) %6' in page[i][z]) | ('39- MÍNIMO DE 25% DAS RECEITAS RESULTANTES DE IMPOSTOS EM MDE ((38) / (4) x 100) %6' in page[i][z]):
                                page[i][z].append(ANO)
                                page[i][z].append(UF)
                                res = []
                                for val in page[i][z]:
                                    if val != None:
                                        res.append(val)                                         
                
                                my_series.append(res)

        elif ANO <= 2016:

            with pdfplumber.open(PDFfile) as pdf:
                for n in range(0, 6, 1):
                    page = pdf.pages[n].extract_tables()
                    for i in range(len(page)):
                        for z in range(len(page[i])):
                            if ('43- TOTAL DAS DESPESAS PARA FINS DE LIMITE (34 - 42)' in page[i][z]) | ('43- TOTAL DAS DESPESAS PARA FINS DE LIMITE (34 - 462)' in page[i][z]) | ('43- TOTAL DAS DESPESAS PARA FINS DE LIMITE (34 - 42)6' in page[i][z]) | ('44- MÍNIMO DE 25% DAS RECEITAS RESULTANTES DE IMPOSTOS EM MDE ((43) / (8) x 100) %6' in page[i][z]) | ('44- MÍNIMO DE 25% DAS RECEITAS RESULTANTES DE IMPOSTOS EM MDE ((43) / (8) x 1060) %' in page[i][z]) | ('44- MÍNIMO DE 25% DAS RECEITAS RESULTANTES DE IMPOSTOS EM MDE ((43) / (8) x 100) %' in page[i][z]) | ('44- MÍNIMO DE 25% DAS RECEITAS RESULTANTES DE IMPOSTOS EM M5D((4E3 ) / (8) x 100) %' in page[i][z]) | ('44- MÍNIMO DE 25% DAS RECEITAS RESULTANTES DE IMPOSTOS EM M5 D((4E3) / (8) x 100) %' in page[i][z]) | ('46- MÍNIMO DE 25% DAS RECEITAS RESULTANTES DE IMPOSTOS EM M5D((4E5 ) / (3) x 100) %' in page[i][z]) | ('45- TOTAL DAS DESPESAS PARA FINS DE LIMITE (37 - 44)' in page[i][z]) | ('46- MÍNIMO DE 25% DAS RECEITAS RESULTANTES DE IMPOSTOS EM M5 D((4E5) / (3) x 100) %' in page[i][z]) | ('46- MÍNIMO DE 25% DAS RECEITAS RESULTANTES DE IMPOSTOS EM M5D((4E5 ) / (3) x 100) %6' in page[i][z]) | ('45- TOTAL DAS DESPESAS PARA FINS DE LIMITE (37 - 464)' in page[i][z]) | ('45- TOTAL DAS DESPESAS PARA FINS DE LIMITE (37 - 44)6' in page[i][z]) | ('46- MÍNIMO DE 25% DAS RECEITAS RESULTANTES DE IMPOSTOS EM MDE 5((45) / (3) x 100) %6' in page[i][z]):
                                page[i][z].append(ANO)
                                page[i][z].append(UF)
                                res = []
                                for val in page[i][z]:
                                    if val != None:
                                        res.append(val)
                                
                                my_series.append(res)
        
        elif ANO > 2020:
            with pdfplumber.open(PDFfile) as pdf:
                for n in range(0, 6, 1):
                    page = pdf.pages[n].extract_tables()
                    for i in range(len(page)):
                        for z in range(len(page[i])):
                            if ('35- APLICAÇÃO EM MDE SOBRE\nA RECEITA LÍQUIDA DE\nIMPOSTOS' in page[i][z]) | ('35- APLICAÇÃO EM MDE\nSOBRE A RECEITA LÍQUIDA\nDE IMPOSTOS' in page[i][z]) | ('35- APLICAÇÃO EM MDE SOBRE A\nRECEITA LÍQUIDA DE IMPOSTOS' in page[i][z]) | ('35- APLICAÇÃO EM MDE\nSOBRE A RECEITA LÍQUIDA DE\nIMPOSTOS' in page[i][z]):
                                page[i][z].append(ANO)
                                page[i][z].append(UF)
                                res = []
                                for val in page[i][z]:
                                    if val != None:
                                        res.append(val)
                                
                                my_series.append(res)
        
        else:
            pass

my_series = pd.Series(my_series)
df = my_series.apply(pd.Series)

df.to_excel("/Users/leonardoyada/Downloads/20231103_planilhafinal_fundeb.xlsx")

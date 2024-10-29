# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:34:43 2024

@author: marianna cecyn
"""

## Created by Marianna Cecyn 
## github: https://github.com/mariannacecyn 
## orcid: https://orcid.org/0000-0002-4995-7482
## linkedin: https://www.linkedin.com/in/mariannacecyn 
## This application was developed as part of Marianna Cecyn's doctoral thesis.


import pandas as pd
import numpy as np
import os

##I suggest you use the Spyder IDE within the anaconda environment
## You should use Anaconda environment to update the packages, this path is easier for beginners.


    
def MatrizTransicaoCont(array):
    #this function creates an counting matrix of transitions for each animal
    matrixcont = pd.crosstab(
        pd.Series(array[:-1], name='from'), #row
        pd.Series(array[1:], name='to'), #column
        margins=True)
    return matrixcont


def MatrizTransicaoProb(array):
    #this function creates an Matrix of Markov for each animal  
    matrixprob = pd.crosstab(
        pd.Series(array[:-1], name='from'), ##row
        pd.Series(array[1:], name='to'), ##column
        normalize="columns",
        margins=True)
    return matrixprob
    

def Frequencias(array):
    #this fuction counts the frequencies of Boris ethogram behaviors
    ##### KEY POINT OF ATTENCION:
    #It is very important to check that the dictionary 
    #has exactly the same behavior as your ethogram 
    #and that the spelling is exactly the same with upper and lower case letters, 
    #spacing, special characters, etc. 
    i=0
    #epm (comment if you don't use it)
    Frequencies = {'Rearing close': 0, 'Stretching close': 0, 'Head out close': 0, 'Grooming close': 0, 'Sniffing close': 0, 'Walking close': 0, 'Stretching and risk': 0, 'Head out and risk': 0, 'Rearing open': 0, 'Head dipping open': 0, 'Grooming open': 0, 'Sniffing open': 0, 'Walking open': 0}
    #ldb (comment if you don't use it)
    #Frequencies = {'Rearing': 0, 'Stretching': 0, 'Head out': 0, 'Grooming': 0, 'Sniffing': 0, 'Walking': 0, 'Light side entry':0, 'Dark side entry': 0} 
    #if you change this dictionary, 
    #you should update the Prob dictionary for Probabilidades()
    #and run combinations code to update the transitions for Transicoes()
    while i < array.size:  
      Key = array[i] 
     
      if Key in Frequencies:
          Frequencies[Key] = Frequencies[Key] + 1 
      else:
          Frequencies[Key] = 1 
      i = i+1

    dfFreq = pd.DataFrame.from_dict(Frequencies, orient ='index') 
    dfFreqt = dfFreq.T
    return dfFreqt

def Probabilidades(array):
    #this function created the State Vector for Markov Chain 
    Probabilities = {'Rearing close': 0, 'Stretching close': 0, 'Head out close': 0, 'Grooming close': 0, 'Sniffing close': 0, 'Walking close': 0, 'Stretching and risk': 0, 'Head out and risk': 0, 'Rearing open': 0, 'Head dipping open': 0, 'Grooming open': 0, 'Sniffing open': 0, 'Walking open': 0}
    #ldb (comment if you don't use it)
    #Frequencies = {'Rearing': 0, 'Stretching': 0, 'Head out': 0, 'Grooming': 0, 'Sniffing': 0, 'Walking': 0, 'Light side entry':0, 'Dark side entry': 0} 
    i = 0
    while i < array.size:  
      Key = array[i] 
     
      if Key in Probabilities:
          Probabilities[Key] = Probabilities[Key] + 1 
      else:
          Probabilities[Key] = 1 
      i = i+1

    for key in Probabilities:
        Probabilities[key] /= contBehavior
    dfProb = pd.DataFrame.from_dict(Probabilities, orient ='index')
    dfProbt = dfProb.T
    return dfProbt

    
           
def Transicoes(array):

    AllTransitions = {
                      'Grooming close - Grooming close': 0, 
                      'Grooming close - Grooming open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Grooming close - Head dipping open': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Grooming close - Head out and risk': 0, 
                      'Grooming close - Head out close': 0, 
                      'Grooming close - Rearing close': 0, 
                      'Grooming close - Rearing open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Grooming close - Sniffing close': 0, 
                      'Grooming close - Sniffing open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Grooming close - Stretching and risk': 0,  
                      'Grooming close - Stretching close': 0, 
                      'Grooming close - Walking close': 0, 
                      'Grooming close - Walking open': 0, 
                      
                      'Grooming open - Grooming close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Grooming open - Grooming open': 0, 
                      'Grooming open - Head dipping open': 0, 
                      'Grooming open - Head out and risk': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Grooming open - Head out close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Grooming open - Rearing close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Grooming open - Rearing open': 0, 
                      'Grooming open - Sniffing close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Grooming open - Sniffing open': 0, 
                      'Grooming open - Stretching and risk': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Grooming open - Stretching close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Grooming open - Walking close': 0, 
                      'Grooming open - Walking open': 0, 
                      
                      'Head dipping open - Grooming close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head dipping open - Grooming open': 0, 
                      'Head dipping open - Head dipping open': 0, 
                      'Head dipping open - Head out and risk': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Head dipping open - Head out close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head dipping open - Rearing close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head dipping open - Rearing open': 0, 
                      'Head dipping open - Sniffing close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head dipping open - Sniffing open': 0, 
                      'Head dipping open - Stretching and risk': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Head dipping open - Stretching close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head dipping open - Walking close': 0, 
                      'Head dipping open - Walking open': 0, 
                      
                      'Head out and risk - Grooming close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head out and risk - Grooming open': 0, 
                      'Head out and risk - Head dipping open': 0, 
                      'Head out and risk - Head out and risk': 0, 
                      'Head out and risk - Head out close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head out and risk - Rearing close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head out and risk - Rearing open': 0, 
                      'Head out and risk - Sniffing close': 0, 
                      'Head out and risk - Sniffing open': 0, 
                      'Head out and risk - Stretching and risk': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head out and risk - Stretching close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head out and risk - Walking close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head out and risk - Walking open': 0, 
                      
                      'Head out close - Grooming close': 0, 
                      'Head out close - Grooming open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head out close - Head dipping open': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Head out close - Head out and risk': 0, 
                      'Head out close - Head out close': 0, 
                      'Head out close - Rearing close': 0, 
                      'Head out close - Rearing open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head out close - Sniffing close': 0, 
                      'Head out close - Sniffing open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Head out close - Stretching and risk': 0,  
                      'Head out close - Stretching close': 0, 
                      'Head out close - Walking close': 0, 
                      'Head out close - Walking open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      
                      'Rearing close - Grooming close': 0, 
                      'Rearing close - Grooming open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Rearing close - Head dipping open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Rearing close - Head out and risk': 0, 
                      'Rearing close - Head out close': 0, 
                      'Rearing close - Rearing close': 0, 
                      'Rearing close - Rearing open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Rearing close - Sniffing close': 0, 
                      'Rearing close - Sniffing open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Rearing close - Stretching and risk': 0,  
                      'Rearing close - Stretching close': 0, 
                      'Rearing close - Walking close': 0, 
                      'Rearing close - Walking open': 0, 
                      
                      'Rearing open - Grooming close': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Rearing open - Grooming open': 0, 
                      'Rearing open - Head dipping open': 0, 
                      'Rearing open - Head out and risk': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Rearing open - Head out close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Rearing open - Rearing close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Rearing open - Rearing open': 0, 
                      'Rearing open - Sniffing close': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Rearing open - Sniffing open': 0, 
                      'Rearing open - Stretching and risk': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Rearing open - Stretching close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Rearing open - Walking close': 0, 
                      'Rearing open - Walking open': 0, 
                      
                      'Sniffing close - Grooming close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Sniffing close - Grooming open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Sniffing close - Head dipping open': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Sniffing close - Head out and risk': 0, 
                      'Sniffing close - Head out close': 0, 
                      'Sniffing close - Rearing close': 0, 
                      'Sniffing close - Rearing open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Sniffing close - Sniffing close': 0, 
                      'Sniffing close - Sniffing open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Sniffing close - Stretching and risk': 0, 
                      'Sniffing close - Stretching close': 0, 
                      'Sniffing close - Walking close': 0, 
                      'Sniffing close - Walking open': 0, 
                      
                      'Sniffing open - Grooming close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Sniffing open - Grooming open': 0, 
                      'Sniffing open - Head dipping open': 0, 
                      'Sniffing open - Head out and risk': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Sniffing open - Head out close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Sniffing open - Rearing close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Sniffing open - Rearing open': 0, 
                      'Sniffing open - Sniffing close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Sniffing open - Sniffing open': 0, 
                      'Sniffing open - Stretching and risk': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Sniffing open - Stretching close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Sniffing open - Walking close': 0, 
                      'Sniffing open - Walking open': 0, 
                      
                      'Stretching and risk - Grooming close': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Stretching and risk - Grooming open': 0, 
                      'Stretching and risk - Head dipping open': 0, 
                      'Stretching and risk - Head out and risk': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Stretching and risk - Head out close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Stretching and risk - Rearing close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Stretching and risk - Rearing open': 0, 
                      'Stretching and risk - Sniffing close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Stretching and risk - Sniffing open': 0, 
                      'Stretching and risk - Stretching and risk': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Stretching and risk - Stretching close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Stretching and risk - Walking close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Stretching and risk - Walking open': 0, 
                      
                      'Stretching close - Grooming close': 0, 
                      'Stretching close - Grooming open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Stretching close - Head dipping open': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Stretching close - Head out and risk': 0, 
                      'Stretching close - Head out close': 0, 
                      'Stretching close - Rearing close': 0, 
                      'Stretching close - Rearing open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Stretching close - Sniffing close': 0, 
                      'Stretching close - Sniffing open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Stretching close - Stretching and risk': 0, 
                      'Stretching close - Stretching close': 0, 
                      'Stretching close - Walking close': 0, 
                      'Stretching close - Walking open': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      
                      'Walking close - Grooming close': 0, 
                      'Walking close - Grooming open': 0, 
                      'Walking close - Head dipping open': 0, 
                      'Walking close - Head out and risk': 0, 
                      'Walking close - Head out close': 0, 
                      'Walking close - Rearing close': 0, 
                      'Walking close - Rearing open': 0, 
                      'Walking close - Sniffing close': 0, 
                      'Walking close - Sniffing open': 0, 
                      'Walking close - Stretching and risk': 0, 
                      'Walking close - Stretching close': 0, 
                      'Walking close - Walking close': 0, 
                      'Walking close - Walking open': 0,
                      
                      'Walking open - Grooming close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Walking open - Grooming open': 0, 
                      'Walking open - Head dipping open': 0, 
                      'Walking open - Head out and risk': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Walking open - Head out close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Walking open - Rearing close': 0, 
                      'Walking open - Rearing open': 0, 
                      'Walking open - Sniffing close': 0, 
                      'Walking open - Sniffing open': 0, 
                      'Walking open - Stretching and risk': 0, #these transitions are not possible, if it occurs may be error in video analysis 
                      'Walking open - Stretching close': 0, #these transitions are not possible, if it occurs may be error in video analysis
                      'Walking open - Walking close': 0, 
                      'Walking open - Walking open': 0
                      } #thanks copilot for these combinations, to make you combinations, use the code in comment below.
    
    
    
    
    
    AnimalTransitions = {} #Thank Fernando Cecyn for that strategy for each animal behavior combinations 
    i=0
    while i < contBehavior:
            
        Key = str(array[i-1]) + " - " + str(array[i]) 
        if Key in AnimalTransitions:
              AnimalTransitions[Key] = AnimalTransitions[Key] + 1 
        else:
              AnimalTransitions[Key] = 1 
        i = i+1
        
    
    Transitions = {**AllTransitions, **AnimalTransitions} #to combine both dictionaries 

    dfTrans = pd.DataFrame.from_dict(Transitions, orient ='index')
    dfTranst = dfTrans.T
    return dfTranst
##############################
##if you need to create your combinations and combination dictionary, use the following code:
    
##List of behaviors
#comportamentos = [
    #'Rearing close', 'Stretching close', 'Head out close', 'Grooming close', 
    #'Sniffing close', 'Walking close', 'Head dipping close', 
    #'Stretching and risk', 'Head out and risk', 'Rearing open', 
    #'Head dipping open', 'Grooming open', 'Sniffing open', 'Walking open']

#combinacoes = []

##Generate all possible combinations of twos where order matters and the same element can occur with itself
#for comportamento1 in comportamentos:
#    for comportamento2 in comportamentos:
#        combinacoes.append(f"{comportamento1} - {comportamento2}")

##Sort the combinations alphabetically
#combinacoes_ordenadas = sorted(combinacoes)

## Turn the list of combinations into a Python dictionary
#AllTransitions = {i: combinacao for i, combinacao in enumerate(combinacoes_ordenadas)}
#print(AllTransiotions)
##I suggest running this code separately and then pasting your AllTransitions dictionary into the main code.
################################

##The following "Where" functions were created to answer questions asked in brainstorm with Dr. Mariana Cardoso Melo.
    
def MatrizTransicaoContWhere(array):
    # create a matrix with where transitions
    matrixcont = pd.crosstab(
        pd.Series(array[:-1], name='from'),  # linha
        pd.Series(array[1:], name='to'),  # coluna
        margins=True)
    return matrixcont

def MatrizTransicaoProbWhere(array):
    # create a markov matrix of where transitions
    matrixprob = pd.crosstab(
        pd.Series(array[:-1], name='from'),  # linha
        pd.Series(array[1:], name='to'),  # coluna
        normalize="columns",
        margins=True)
    return matrixprob


def FrequenciasWhere(array):
    # frequencies of open and close entries
    Frequencies = {}
    i = 0
    while i < array.size:  
        Key = array[i]
        if Key in Frequencies:
            Frequencies[Key] += 1
        else:
            Frequencies[Key] = 1
        i += 1
    dfFreq = pd.DataFrame.from_dict(Frequencies, orient='index')
    dfFreqt = dfFreq.T
    return dfFreqt

def ProbabilidadesWhere(array):
    # state vector for markov chain of open and close entries
    Probabilities = {}
    i = 0
    while i < array.size:  
        Key = array[i]
        if Key in Probabilities:
            Probabilities[Key] += 1
        else:
            Probabilities[Key] = 1
        i += 1
    for key in Probabilities:
        Probabilities[key] /= array.size
    dfProb = pd.DataFrame.from_dict(Probabilities, orient='index')
    dfProbt = dfProb.T
    return dfProbt

def TransicoesWhere(array):
    AllWhereTransitions = {"Open arm - Open arm": 0, "Open arm - Close arm": 0, "Close arm - Close arm": 0, "Close arm - Open arm": 0}
    WhereTransitions = {}
    i = 1  
    while i < array.size:
        Key = str(array[i-1]) + " - " + str(array[i])
        if Key in WhereTransitions:
            WhereTransitions[Key] += 1
        else:
            WhereTransitions[Key] = 1
        i += 1
    Transitionsw = {**AllWhereTransitions, **WhereTransitions}  
    dfTransw = pd.DataFrame.from_dict(Transitionsw, orient='index')
    dfTranstw = dfTransw.T
    return dfTranstw




#INICIANDO...

print("\n================================")
print("App for Behavior Data Processing 3.0 \n Created by Marianna Cecyn \n Please cite  \n github: https://github.com/mariannacecyn  \n orcid: https://orcid.org/0000-0002-4995-7482 \n linkedin: https://www.linkedin.com/in/mariannacecyn")
print("\n================================")   
#if you want to use console, use this code
##folder = input("Paste here the full path of the data folder you would like to process: ") ##if you prefer use the Spyder console 
##path = folder

#if you want to directly use the code, use this:
folder = "paste were the pathway of folder"
#remember that you should change "\" by "/" to use this.

path = folder
files = os.listdir(path)
files_xlsx = [path + '/' + f for f in files if f[-5:] == '.xlsx' ]
animals = [a[-20:-5] for a in files if a[-5:] == '.xlsx'] 
#here you must change a string depending your file name lenght
print("\n================================")
#datasubj = pd.DataFrame(animals)
#databaseBehaviors = pd.DataFrame()
#databaseTrans = pd.DataFrame()

for f in files_xlsx:
          

    
    df_original = pd.read_excel(f) #DataFrame of Boris .xlsx
    
    arr = df_original["Behavior"].values #behavior array 
            
    
    for i in arr:
        if i == "Open arm":   
            arr = np.delete(arr, np.where(arr == i))
        if i == "Close arm":
            arr = np.delete(arr, np.where(arr == i))
        if i == "Start of experiment":
            arr = np.delete(arr, np.where(arr == i))
        if i == "End of experiment":
            arr = np.delete(arr, np.where(arr == i))
        if i == "Start of test":
            arr = np.delete(arr, np.where(arr == i))
        if i == "End of test":
            arr = np.delete(arr, np.where(arr == i))
        if i == "Center cross":
            arr = np.delete(arr, np.where(arr == i))
        if i == "Head dipping close":
            arr = np.delete(arr, np.where(arr == i))    
        else: arr = arr
    contBehavior = np.size(arr)
    
    ##FOR WHERE TRANSITIONS
    # Read desired columns from Excel file
    df_originalWHERE = pd.read_excel(f, usecols=["Behavior", "Behavior type"])
        
    # Set condition to filter
    cond = df_originalWHERE["Behavior type"] == "START"

    # Apply the filter and select the "Behavior" column
    df_where = df_originalWHERE.loc[cond, "Behavior"]

    arrwhere = df_where.values  # Convert to numpy array
    contwhere = np.size(arrwhere)    
 
        
    

    
    ##using ExcelWriter to create a .xlsx, usando engine='xlsxwriter'
    ## you need to create a folder and copy the path here
    
    writer = pd.ExcelWriter("paste were the destination folder/" + '/python-32-' + f[-20:], engine='xlsxwriter')
    #remember that you should change "\" by "/" to use this. You should review the lenght of names.
    
    df_original.to_excel(writer, sheet_name='Boris')
    pd.DataFrame(arr).to_excel(writer, sheet_name='SeqBehaviors')
    Frequencias(arr).to_excel(writer, sheet_name='FreqBehaviors')
    Probabilidades(arr).to_excel(writer, sheet_name='ProbBehaviors')
    Transicoes(arr).to_excel(writer, sheet_name='TransCont')
    MatrizTransicaoCont(arr).to_excel(writer, sheet_name='ContMatrix')
    MatrizTransicaoProb(arr).to_excel(writer, sheet_name='ProbMatrix')
    FrequenciasWhere(arrwhere).to_excel(writer, sheet_name='FreqBehaviorsWHERE')
    ProbabilidadesWhere(arrwhere).to_excel(writer, sheet_name='ProbBehaviorsWHERE')
    TransicoesWhere(arrwhere).to_excel(writer, sheet_name='TransContWHERE')
    MatrizTransicaoContWhere(arrwhere).to_excel(writer, sheet_name='ContMatrixWHERE')
    MatrizTransicaoProbWhere(arrwhere).to_excel(writer, sheet_name='ProbMatrixWHERE')

    writer.close()
    

   



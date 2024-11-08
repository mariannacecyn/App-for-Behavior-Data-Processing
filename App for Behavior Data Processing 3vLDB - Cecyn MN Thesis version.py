# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:34:43 2024

@author: marianna cecyn
"""

## Created by Marianna Cecyn 
## github: https://github.com/mariannacecyn 
## orcid: https://orcid.org/0000-0002-4995-7482
## linkedin: https://www.linkedin.com/in/mariannacecyn 


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
    #######LDB 
    Frequencies = {'Light side entry':0, 'Close side entry':0, 'Rearing': 0, 'Stretching': 0, 'Head out': 0, 'Grooming': 0, 'Sniffing': 0, 'Walking': 0, 'stretch risk': 0, 'head risk': 0}
 
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
    Probabilities = {'Light side entry':0, 'Close side entry':0, 'Rearing': 0, 'Stretching': 0, 'Head out': 0, 'Grooming': 0, 'Sniffing': 0, 'Walking': 0, 'stretch risk': 0, 'head risk': 0} 
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

    AllTransitions = {'Close side entry - Close side entry':0, 
                      'Close side entry - Grooming':0, 
                      'Close side entry - Head out':0,
                      'Close side entry - Light side entry':0, 
                      'Close side entry - Rearing':0, 
                      'Close side entry - Sniffing':0, 
                      'Close side entry - Stretching':0, 
                      'Close side entry - Walking':0, 
                      'Close side entry - head risk':0, 
                      'Close side entry - stretch risk':0, 
                      'Grooming - Close side entry':0, 
                      'Grooming - Grooming':0, 
                      'Grooming - Head out':0, 
                      'Grooming - Light side entry':0, 
                      'Grooming - Rearing':0, 
                      'Grooming - Sniffing':0, 
                      'Grooming - Stretching':0, 
                      'Grooming - Walking':0, 
                      'Grooming - head risk':0, 
                      'Grooming - stretch risk':0, 
                      'Head out - Close side entry':0, 
                      'Head out - Grooming':0, 
                      'Head out - Head out':0, 
                      'Head out - Light side entry':0, 
                      'Head out - Rearing':0, 
                      'Head out - Sniffing':0, 
                      'Head out - Stretching':0, 
                      'Head out - Walking':0, 
                      'Head out - head risk':0, 
                      'Head out - stretch risk':0, 
                      'Light side entry - Close side entry':0, 
                      'Light side entry - Grooming':0,
                      'Light side entry - Head out':0, 
                      'Light side entry - Light side entry':0, 
                      'Light side entry - Rearing':0, 
                      'Light side entry - Sniffing':0, 
                      'Light side entry - Stretching':0, 
                      'Light side entry - Walking':0,
                      'Light side entry - head risk':0, 
                      'Light side entry - stretch risk':0, 
                      'Rearing - Close side entry':0, 
                      'Rearing - Grooming':0, 
                      'Rearing - Head out':0, 
                      'Rearing - Light side entry':0, 
                      'Rearing - Rearing':0, 
                      'Rearing - Sniffing':0, 
                      'Rearing - Stretching':0, 
                      'Rearing - Walking':0, 
                      'Rearing - head risk':0, 
                      'Rearing - stretch risk':0, 
                      'Sniffing - Close side entry':0, 
                      'Sniffing - Grooming':0, 
                      'Sniffing - Head out':0, 
                      'Sniffing - Light side entry':0, 
                      'Sniffing - Rearing':0, 
                      'Sniffing - Sniffing':0, 
                      'Sniffing - Stretching':0, 
                      'Sniffing - Walking':0, 
                      'Sniffing - head risk':0, 
                      'Sniffing - stretch risk':0, 
                      'Stretching - Close side entry':0, 
                      'Stretching - Grooming':0, 
                      'Stretching - Head out':0, 
                      'Stretching - Light side entry':0, 
                      'Stretching - Rearing':0, 
                      'Stretching - Sniffing':0, 
                      'Stretching - Stretching':0, 
                      'Stretching - Walking':0, 
                      'Stretching - head risk':0, 
                      'Stretching - stretch risk':0, 
                      'Walking - Close side entry':0, 
                      'Walking - Grooming':0, 
                      'Walking - Head out':0, 
                      'Walking - Light side entry':0, 
                      'Walking - Rearing':0, 
                      'Walking - Sniffing':0, 
                      'Walking - Stretching':0, 
                      'Walking - Walking':0, 
                      'Walking - head risk':0, 
                      'Walking - stretch risk':0, 
                      'head risk - Close side entry':0, 
                      'head risk - Grooming':0, 
                      'head risk - Head out':0, 
                      'head risk - Light side entry':0, 
                      'head risk - Rearing':0, 
                      'head risk - Sniffing':0, 
                      'head risk - Stretching':0, 
                      'head risk - Walking':0, 
                      'head risk - head risk':0, 
                      'head risk - stretch risk':0,
                      'stretch risk - Close side entry':0, 
                      'stretch risk - Grooming':0, 
                      'stretch risk - Head out':0,
                      'stretch risk - Light side entry':0, 
                      'stretch risk - Rearing':0, 
                      'stretch risk - Sniffing':0, 
                      'stretch risk - Stretching':0, 
                      'stretch risk - Walking':0, 
                      'stretch risk - head risk':0,
                      'stretch risk - stretch risk':0}
                       #thanks copilot for these combinations, to make you combinations, use the code in comment below.
    
    
    
    
    
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
#comportamentos = ['Light side entry', 'Close side entry', 'Rearing', 'Stretching', 'Head out', 'Grooming', 'Sniffing', 'Walking', 'stretch risk', 'head risk']


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
          

    
    df_original = pd.read_excel(f) #transformei o excel num objeto do python que ele consegue mostrar como Dataframe
    
    arr = df_original["Behavior"].values #criado um array com a sequencia de comportamentos
    #print(arr)        
    
    for i in arr:


        if i == "Start of test":
            arr = np.delete(arr, np.where(arr == i))
        if i == "End of test":
            arr = np.delete(arr, np.where(arr == i))
    
        else: arr = arr
    contBehavior = np.size(arr)
    

 
        
    

    
    ##Usando o ExcelWriter, cria um doc .xlsx, usando engine='xlsxwriter'
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
    

    writer.close()
    

   



# importing all the required modules
import PyPDF2

# creating a pdf reader object
reader = PyPDF2.PdfReader('Prethiv_VoE_Letter.pdf')

# print the number of pages in pdf file
print(len(reader.pages))
i=0
# print the text of the first page
stringOfPages = ''
for page in reader.pages:
    print("Page ",i+1)
    i+=1
    stringOfPages+=page.extract_text()
    print(page.extract_text())
    print("****************************************************************************************************************************************************************")
    print("++++++++++++++++++++++++++++++++++++++++")

import subprocess
import json
def promptMe(prompt,story):
    return subprocess.check_output(shell=False,args=['llm','-m','ggml-model-gpt4all-falcon-q4_0',
        'Understand the story given below:\n'+story+'\n and answer the following '+prompt])

i=''
while i!='quit':
    i=input("Enter your query")
    # Opening JSON file
    # f = open('DummyData.json')
    # returns JSON object as
    # a dictionary
    # data = json.load(f)
    # print(data)
    if i=='quit':
        break
    print(promptMe(i,stringOfPages))
   

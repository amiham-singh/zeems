    
from jinja2 import Environment, FileSystemLoader
import pandas as pd
import random 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
#%%
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C://Users//Family New//Desktop//keys.json', scope)

#%%

client = gspread.authorize(creds)

#%%

zeal= client.open('zeems').sheet1

#%%
data = zeal.get_all_values()
headers = data.pop(0)
zeel = pd.DataFrame(data, columns=headers)
mahima= client.open('zeems').get_worksheet(1)
datas = mahima.get_all_values()
header = datas.pop(0)
heemz = pd.DataFrame(datas, columns=header)
word=[]
word.append(random.choice(zeel["words"]))
word.append(random.choice(heemz["words"]))
final= random.sample(set(word), 2)
answer = final[0] + ' ' + final[1]

#%%
root = os.getcwd()
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('index.html')
 
 
filename = os.path.join(root, 'html', 'index.html')
with open(filename, 'w') as fh:
    fh.write(template.render(
        theme = answer,
       
    ))    
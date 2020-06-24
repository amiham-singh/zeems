    
from jinja2 import Environment, FileSystemLoader
import pandas as pd
import random 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
#%%
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/hp/Desktop/keys.json', scope)

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
#%%
word=[]
word.append(random.choice(zeel["words"]))
word.append(random.choice(heemz["words"]))
word
#%%
final= random.sample(set(word), 2)
answer = final[0] + ' ' + final[1]
answer
#%%
#updating the theme list
text= client.open('zeems').get_worksheet(2)



#%%

update_word= "a" + str(len(text.col_values(1))+1)
update_zimg = "d" + str(len(text.col_values(1))+1)
update_textm = "b" + str(len(text.col_values(1))+1)
update_textz = "c" + str(len(text.col_values(1))+1)
update_mimg = "e" + str(len(text.col_values(1))+1)
zimg_p = "pics/zeel_" + str(len(text.col_values(1))) +".jpg"
mimg_p = "pics/heemz_" + str(len(text.col_values(1)))+".jpg"                            
text.update_acell(update_word,answer)
text.update_acell(update_zimg,zimg_p)
text.update_acell(update_mimg,mimg_p)
text.update_acell(update_textm,"Work in progress")
text.update_acell(update_textz,"Work in progress")


#%%
#getting this week's text
text= client.open('zeems').get_worksheet(2)
word=text.col_values(1)[1:]
z = text.col_values(2)[1:]
m = text.col_values(3)[1:]
zpic = text.col_values(4)[1:]
mpic= text.col_values(5)[1:]

#%%
m.reverse()
z.reverse()
word.reverse()
mpic.reverse()
zpic.reverse()




#%%
os.chdir("C:\\Users\\hp\\Desktop\\zeems")
root = os.getcwd()
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('index.html')
 
 

filename = os.path.join(root, 'index.html')
with open(filename, 'w') as fh:
    fh.write(template.render(
        theme = answer,
        content = zip(m, z, word, mpic,zpic ),
    ))    

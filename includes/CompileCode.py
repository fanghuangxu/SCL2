from includes.LexerWithSingleQuoteString import lexer_with_single_quote_string as LWSQS 
from includes.constants import *
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
Dict=CodeDict

def InputTheLWSQSRe(code):
        return LWSQS(code)


def ToTkinterGuiProgram(code):
    code=str(code)
    command="import tkinter as tk"
    root = ET.fromstring(code)
    Code={
         "Title":"",
         "h":200,
         "w":300
    }
    Code['Title']=root.find('title').text
    command+="\n"+f"root=tk.Tk()"
    command+="\n"+f"root.title('{Code['Title']}')"
    command+="\n"+f"root.geometry('{Code['w']}x{Code['h']}')"
    try:
        Code['h']=int(root.find('height'))
        Code['w']=int(root.find('width'))
    
        for Imports in root.findall('imports'):
            for module in Imports.findall('module'):
                command+="\n"+f"import {module.text}"
        
        for windowcode in root.findall('window'):
            command+=windowcode.find('functions').text
            for Buttons in windowcode.findall('button'):
                Text=Buttons.find('text').text
                Command=Buttons.find('command').text
                Id=Buttons.find('id').text
                command+="\n"+f"{Id}=tk.Button(root,text='{Text}',command={Command})\n{Id}.pack()"
            for Labels in windowcode.findall('label'):
                Text=Labels.find('text').text
                Id=Labels.find('id').text
                command+="\n"+f"{Id}=tk.Label(root,text='{Text}')\n{Id}.pack()"
            for Entries in windowcode.findall('entry'):
                Id=Entries.find('id').text
                command+="\n"+f"{Id}=tk.Entry(root)\n{Id}.pack()"
            for Texts in windowcode.findall('text'):
                Text=Texts.find('text').text
                Id=Texts.find('id').text
                command+="\n"+f"{Id}=tk.Text(root)\n{Id}.insert(tk.END,'{Text}')\n{Id}.pack()"
            for Checkboxes in windowcode.findall('checkbox'):
                Text=Checkboxes.find('text').text
                Variable=Checkboxes.find('variable').text
                Id=Checkboxes.find('id').text
                command+="\n"+f"{Variable}=tk.IntVar()\n{Id}=tk.Checkbutton(root,text='{Text}',variable={Variable})\n{Id}.pack()"
            for Radiobuttons in windowcode.findall('radiobutton'):
                Text=Radiobuttons.find('text').text
                Variable=Radiobuttons.find('variable').text
                Value=Radiobuttons.find('value').text
                Id=Radiobuttons.find('id').text
                command+="\n"+f"{Variable}=tk.StringVar()\n{Id}=tk.Radiobutton(root,text='{Text}',variable={Variable},value='{Value}')\n{Id}.pack()"
            for Menus in windowcode.findall('menu'):
                Id=Menus.find('id').text
                command+="\n"+f"{Id}=tk.Menu(root)\nroot.config(menu={Id})"
                for Menuitems in Menus.findall('menuitem'):
                    Text=Menuitems.find('text').text
                    Command=Menuitems.find('command').text
                    Id=Menuitems.find('id').text
                    command+="\n"+f"{Id}=tk.Menu(root,tearoff=0)\n{Id}.add_command(label='{Text}',command={Command})\n{Id}.add_separator()\n{Id}.add_command(label='Exit',command=root.quit)"
    except:
           pass
    command+="\n"+f"root.mainloop()"
    return command

def Compile1(Code):
    code = InputTheLWSQSRe(Code)
    code1=ToTkinterGuiProgram(Code)
    return code1,code



def Return(code,code1):
    comd=\
f"""
'''
Tokens:
{code}
'''
{code1}
"""
    return comd





def Compile(code2):
    code1,code=Compile1(code2)
    return Return(code=code,code1=code1)
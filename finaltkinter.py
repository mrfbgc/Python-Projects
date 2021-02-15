import tkinter as tk
from tkinter import messagebox
from tkinter import *
import json
patient = []
selectedPatient = -1
#---------------------------------------------------------------------------
def LoadAllPatients():
    try:
        file = open("patients.arf", "r")
        patientData = json.load(file)
        for pat in patientData:
            patient.append({"NS": pat["NS"], "Mail": pat["Mail"], "Height": pat["Height"], "Weight": pat["Weight"],
                            "KanSeker": pat["KanSeker"], "Tel": pat["Tel"]})
            patientlist.insert(END, pat.get("NS", "No Name"))
            patientemaillist.insert(END, pat.get("Mail", "No Mail"))
            patientheightlist.insert(END, pat.get("Height", "No Height"))
            patientweightlist.insert(END, pat.get("Weight", "No Weight"))
            patientkansekerlist.insert(END, pat.get("KanSeker", "No Kan Sekeri"))
            patienttellist.insert(END, pat.get("Tel", "No Tel"))
        file.close()
    except:
        pass
#---------------------------------------------------------------------------
def SaveAllPatients():
    file = open("patients.arf","w")
    json.dump(patient,file)
    file.close()
#---------------------------------------------------------------------------
def AddPation():
    newPatient = {"NS":E1.get() if E1.get()  != "" else "No Name","Mail":E2.get() if E2.get()  != "" else "No Mail","Height":E3.get() if E3.get()  != "" else "No Height","Weight":E4.get() if E4.get()  != "" else "No Weight","KanSeker":E5.get() if E5.get()  != "" else "No Kan Sekeri","Tel":E6.get() if E6.get()  != "" else "No Tel"}
    patientlist.insert(END,newPatient["NS"])
    patientemaillist.insert(END,newPatient["Mail"])
    patientheightlist.insert(END, newPatient["Height"])
    patientweightlist.insert(END,newPatient["Weight"])
    patientkansekerlist.insert(END, newPatient["KanSeker"])
    patienttellist.insert(END, newPatient["Tel"])
    patient.append(newPatient)
    SaveAllPatients()
#---------------------------------------------------------------------------
def DeletePation():
    index = patientlist.curselection()[0]
    patientlist.delete(index)
    patientemaillist.delete(index)
    patientheightlist.delete(index)
    patientweightlist.delete(index)
    patientkansekerlist.delete(index)
    patienttellist.delete(index)
    patient.remove(patient[index])
    for i in range(8):
        patientInfoList[i].place_forget()

    SaveAllPatients()
#---------------------------------------------------------------------------
def IsDiabet():
    if(int(patient[selectedPatient]["KanSeker"]) >= 126): return "Hasta Seker Hastası."
    else: return "Hasta Seker Hastası Değil."
#---------------------------------------------------------------------------
def IsObese():
    vki = (int(patient[selectedPatient]["Weight"])/(int(patient[selectedPatient]["Height"])/100)**2)
    print(vki)
    if vki < 18.4:
        return "Hasta Zayıf"
    elif vki >= 18.4 and vki < 25:
        return "Hasta Normal Kiloda"
    elif vki >= 25 and vki < 30:
        return "Hasta Fazla Kilolu"
    elif vki >= 30 and vki < 35:
        return "Hasta Tip 1 Obez"
    elif vki >= 35 and vki < 45:
        return "Hasta Tip 2 Obez"
    elif vki >= 45:
        return "Hasta Morbid Obez"
#---------------------------------------------------------------------------
def PatientSelect(event):
    global selectedPatient
    try:
        selectedPatient = event.widget.curselection()[0]
    except:
        pass
    textList = ["Hasta:","Hasta Mail:","Hasta Boy:","Hasta Kilo:","Kan Şekeri:","Hasta Telefon:"]
    keys = ["NS","Mail","Height","Weight","KanSeker","Tel"]
    if(selectedPatient != -1):
        for i in range(6):
            patientInfoList[i].place(height=30,width=426,x=426,y=315+(i*30))
            patientInfoList[i].config(text=f"{textList[i]} {patient[selectedPatient][keys[i]]}")
        patientInfoList[6].place(height=30,width=426,x=426,y=495)
        patientInfoList[6].config(text=f"{IsDiabet()}")
        patientInfoList[7].place(height=30, width=426, x=426, y=525)
        patientInfoList[7].config(text=f"{IsObese()}")
def kullanım():
    messagebox.showinfo(title="Kullanım Kılavuzu!",message="Hasta bilgilerini giriş bölümlerine ekledikten sonra ekle tuşuna basınız. Sonuçlarını görmek istediğiniz hastanın ismine tıkladıktan sonra bilgiler ekrana gelecektir. Silmek için hasta adını seçtikten sonra sil butonuna basınız. Boyu cm cinsinden kiloyu kg cinsinden giriniz!")
# ---------------------------------------------------------------------------
win=tk.Tk()
win.resizable(False,False) #pencerinin boyu değişemez
win.configure(bg='cadetblue')
win.title("Hasta bilgileri")
win.geometry("1280x600")

#---------------------------------------------------------------------------

patientinfo=tk.Frame(win,bg='cadetblue')
patientinfo.place(x=0,y=0,width=1280,height=720)

patientname=tk.Label(patientinfo,text='Hasta adı ve soyadı:',bg='LightSeaGreen')
patientname.place(x=0,y=0,width=213, height=15)

patientlist=tk.Listbox(patientinfo,bg='LightSteelBlue1')
patientlist.place(x=0,y=15,width=213, height=250)
patientlist.bind("<<ListboxSelect>>",PatientSelect)
#----------------------------------------------------------------------------
E1 =tk.Entry(patientinfo, bd = 2,bg='LightSeaGreen')
E1.place(x=0,y=265,width=213, height=25)
#----------------------------------------------------------------------------
button1= tk.Button(patientinfo,text='Ekle',command=AddPation,bg='seagreen')
button1.place(x=0,y=290,width=426, height=25)
button3= tk.Button(patientinfo,text='Kullanım Kılavuzu',command=kullanım,bg='seagreen')
button3.place(x=426,y=290,width=427, height=25)
button2= tk.Button(patientinfo,text='Sil',command=DeletePation,bg='seagreen')
button2.place(x=852,y=290,width=427, height=25)
#----------------------------------------------------------------------------
#---------------------------------------------------------------------------

patientemail=tk.Label(patientinfo,text='Hasta e-mail:',bg='LightSeaGreen')
patientemail.place(x=213,y=0,width=213, height=15)

patientemaillist=tk.Listbox(patientinfo,bg='LightSteelBlue1')
patientemaillist.place(x=213,y=15,width=213, height=250)
#----------------------------------------------------------------------------
E2 =tk.Entry(patientinfo, bd = 2,bg='LightSeaGreen')
E2.place(x=213,y=265,width=213, height=25)

#---------------------------------------------------------------------------

patientheight=tk.Label(patientinfo,text='Hasta boyu:',bg='LightSeaGreen')
patientheight.place(x=426,y=0,width=213, height=15)

patientheightlist=tk.Listbox(patientinfo,bg='LightSteelBlue2')
patientheightlist.place(x=426,y=15,width=213, height=250)

E3 =tk.Entry(patientinfo, bd = 2,bg='LightSeaGreen')
E3.place(x=426,y=265,width=213, height=25)

#---------------------------------------------------------------------------

patientweight=tk.Label(patientinfo,text='Hasta kilosu:',bg='LightSeaGreen')
patientweight.place(x=639,y=0,width=213, height=15)

patientweightlist=tk.Listbox(patientinfo,bg='LightSteelBlue2')
patientweightlist.place(x=639,y=15,width=213, height=250)

E4 =tk.Entry(patientinfo, bd = 2,bg='LightSeaGreen')
E4.place(x=639,y=265,width=213, height=25)

#---------------------------------------------------------------------------

patientkanseker=tk.Label(patientinfo,text='Hasta açlık kan şekeri:',bg='LightSeaGreen')
patientkanseker.place(x=852,y=0,width=213, height=15)

patientkansekerlist=tk.Listbox(patientinfo,bg='LightSteelBlue3')
patientkansekerlist.place(x=852,y=15,width=213, height=250)

E5 =tk.Entry(patientinfo, bd = 2,bg='LightSeaGreen')
E5.place(x=852,y=265,width=213, height=25)

#---------------------------------------------------------------------------
patienttel=tk.Label(patientinfo,text='Hasta telefon no:',bg='LightSeaGreen')
patienttel.place(x=1065,y=0,width=213, height=15)

patienttellist=tk.Listbox(patientinfo,bg='LightSteelBlue3')
patienttellist.place(x=1065,y=15,width=213, height=250)

E6 =tk.Entry(patientinfo, bd = 2,bg='LightSeaGreen')
E6.place(x=1065,y=265,width=213, height=25)

#---------------------------------------------------------------------------

patientInfoList = [Label(patientinfo,text="Hasta ", font="Calibri 15",bg='cadetblue'),Label(patientinfo,text="Mail ", font="Calibri 15",bg='cadetblue'),Label(patientinfo,text="Hasta Boy ", font="Calibri 15",bg='cadetblue')
                ,Label(patientinfo ,text="Hasta Kilo", font="Calibri 15",bg='cadetblue'),Label(patientinfo ,text="Kan Şekeri ", font="Calibri 15",bg='cadetblue'),
                 Label(patientinfo ,text="Hasta Telefon ", font="Calibri 15",bg='cadetblue'),Label(patientinfo ,text="Hasta Diyabet Yada Değil", font="Calibri 15",bg='cadetblue'),
                 Label(patientinfo, text="Hasta Obez Yada Değil", font="Calibri 15",bg='cadetblue') ]

LoadAllPatients()
win.mainloop()
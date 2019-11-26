from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msg
from datetime import datetime
from pytz import timezone
from pytz import all_timezones
import pytz
from tkcalendar import DateEntry
import re

window=Tk()

window.wm_title("Timezone Converter")

photo = PhotoImage(file = 'C:/Users/Raj/Desktop/Python_Files/Timezone/Time_converter.png')
window.iconphoto(False, photo)
window.configure(background = '#87CEEB')

def clear_all():
    list1.delete(0,END)
    list2.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    number_min.delete(0,END)
    number_hrs.delete(0,END)

def aboutbox():
    msg.showinfo('Timezone Converter','Timezone Conversion Version 0.1 \n \nCopyright (c) 2019. All Rights Reserved.')

def exitbox():
    answer = msg.askyesnocancel('Timezone Converter Exit','Are you sure you really wish to exit?')
    if answer == True:
        window.destroy()
    elif answer == False:
        window.destroy
    else:
        window.destroy

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label="New",command=clear_all)
file_menu.add_command(label="Exit",command=exitbox)
menu_bar.add_cascade(label="File",menu=file_menu)

help_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Help',menu=help_menu)
help_menu.add_command(label='About',command=aboutbox)

style = Style()
style.configure('W.TButton', font = ('calibri', 10, 'bold',), foreground = 'black',background = '#87CEEB')
style.configure('TLabel', font = ('calibri', 10, 'bold',), foreground = 'black',background = '#87CEEB')

def get_selected_row(event):
    global selected_tuple
    index=list2.curselection()
    selected_tuple=list2.get(index)
    if not e1.get():
        e1.insert(END,selected_tuple)
        e4.delete(0,END)
        list2.delete(0,END)
    elif not e2.get():
        e2.insert(END,selected_tuple)
        e4.delete(0,END)
        list2.delete(0,END)

ctry_list2 = {'andorra':'Andorra','united arab emirates':'United Arab Emirates','afghanistan':'Afghanistan','antigua & barbuda':'Antigua & Barbuda','anguilla':'Anguilla',
'albania':'Albania','armenia':'Armenia','angola':'Angola','antarctica':'Antarctica','argentina':'Argentina','samoa (american)':'Samoa (American)',
'austria':'Austria','australia':'Australia','aruba':'Aruba','åland islands':'Åland Islands','azerbaijan':'Azerbaijan','bosnia & herzegovina':'Bosnia & Herzegovina',
'barbados':'Barbados','bangladesh':'Bangladesh','belgium':'Belgium','burkina faso':'Burkina Faso','bulgaria':'Bulgaria','bahrain':'Bahrain','burundi':'Burundi',
'benin':'Benin','st barthelemy':'St Barthelemy','bermuda':'Bermuda','brunei':'Brunei','bolivia':'Bolivia','caribbean nl':'Caribbean NL','brazil':'Brazil',
'bahamas':'Bahamas','bhutan':'Bhutan','bouvet island':'Bouvet Island','botswana':'Botswana','belarus':'Belarus','belize':'Belize','canada':'Canada',
'cocos (keeling) islands':'Cocos (Keeling) Islands','congo (dem. rep.)':'Congo (Dem. Rep.)','central african rep.':'Central African Rep.','congo (rep.)':'Congo (Rep.)',
'switzerland':'Switzerland','côte d\'ivoire':'Côte d\'Ivoire','cook islands':'Cook Islands','chile':'Chile','cameroon':'Cameroon','china':'China','colombia':'Colombia',
'costa rica':'Costa Rica','cuba':'Cuba','cape verde':'Cape Verde','curaçao':'Curaçao','christmas island':'Christmas Island','cyprus':'Cyprus','czech republic':'Czech Republic',
'germany':'Germany','djibouti':'Djibouti','denmark':'Denmark','dominica':'Dominica','dominican republic':'Dominican Republic','algeria':'Algeria','ecuador':'Ecuador',
'estonia':'Estonia','egypt':'Egypt','western sahara':'Western Sahara','eritrea':'Eritrea','spain':'Spain','ethiopia':'Ethiopia','finland':'Finland','fiji':'Fiji',
'falkland islands':'Falkland Islands','micronesia':'Micronesia','faroe islands':'Faroe Islands','france':'France','gabon':'Gabon','britain (uk)':'Britain (UK)',
'grenada':'Grenada','georgia':'Georgia','french guiana':'French Guiana','guernsey':'Guernsey','ghana':'Ghana','gibraltar':'Gibraltar','greenland':'Greenland',
'gambia':'Gambia','guinea':'Guinea','guadeloupe':'Guadeloupe','equatorial guinea':'Equatorial Guinea','greece':'Greece','south georgia & the south sandwich islands':'South Georgia & the South Sandwich Islands',
'guatemala':'Guatemala','guam':'Guam','guinea-bissau':'Guinea-Bissau','guyana':'Guyana','hong kong':'Hong Kong','heard island & mcdonald islands':'Heard Island & McDonald Islands',
'honduras':'Honduras','croatia':'Croatia','haiti':'Haiti','hungary':'Hungary','indonesia':'Indonesia','ireland':'Ireland','israel':'Israel','isle of man':'Isle of Man',
'india':'India','british indian ocean territory':'British Indian Ocean Territory','iraq':'Iraq','iran':'Iran','iceland':'Iceland','italy':'Italy','jersey':'Jersey',
'jamaica':'Jamaica','jordan':'Jordan','japan':'Japan','kenya':'Kenya','kyrgyzstan':'Kyrgyzstan','cambodia':'Cambodia','kiribati':'Kiribati','comoros':'Comoros',
'st kitts & nevis':'St Kitts & Nevis','korea (north)':'Korea (North)','korea (south)':'Korea (South)','kuwait':'Kuwait','cayman islands':'Cayman Islands',
'kazakhstan':'Kazakhstan','laos':'Laos','lebanon':'Lebanon','st lucia':'St Lucia','liechtenstein':'Liechtenstein','sri lanka':'Sri Lanka','liberia':'Liberia',
'lesotho':'Lesotho','lithuania':'Lithuania','luxembourg':'Luxembourg','latvia':'Latvia','libya':'Libya','morocco':'Morocco','monaco':'Monaco','moldova':'Moldova',
'montenegro':'Montenegro','st martin (french)':'St Martin (French)','madagascar':'Madagascar','marshall islands':'Marshall Islands','north macedonia':'North Macedonia',
'mali':'Mali','myanmar (burma)':'Myanmar (Burma)','mongolia':'Mongolia','macau':'Macau','northern mariana islands':'Northern Mariana Islands','martinique':'Martinique',
'mauritania':'Mauritania','montserrat':'Montserrat','malta':'Malta','mauritius':'Mauritius','maldives':'Maldives','malawi':'Malawi','mexico':'Mexico','malaysia':'Malaysia',
'mozambique':'Mozambique','namibia':'Namibia','new caledonia':'New Caledonia','niger':'Niger','norfolk island':'Norfolk Island','nigeria':'Nigeria','nicaragua':'Nicaragua',
'netherlands':'Netherlands','norway':'Norway','nepal':'Nepal','nauru':'Nauru','niue':'Niue','new zealand':'New Zealand','oman':'Oman','panama':'Panama',
'peru':'Peru','french polynesia':'French Polynesia','papua new guinea':'Papua New Guinea','philippines':'Philippines','pakistan':'Pakistan','poland':'Poland',
'st pierre & miquelon':'St Pierre & Miquelon','pitcairn':'Pitcairn','puerto rico':'Puerto Rico','palestine':'Palestine','portugal':'Portugal','palau':'Palau',
'paraguay':'Paraguay','qatar':'Qatar','réunion':'Réunion','romania':'Romania','serbia':'Serbia','russia':'Russia','rwanda':'Rwanda','saudi arabia':'Saudi Arabia',
'solomon islands':'Solomon Islands','seychelles':'Seychelles','sudan':'Sudan','sweden':'Sweden','singapore':'Singapore','st helena':'St Helena','slovenia':'Slovenia',
'svalbard & jan mayen':'Svalbard & Jan Mayen','slovakia':'Slovakia','sierra leone':'Sierra Leone','san marino':'San Marino','senegal':'Senegal','somalia':'Somalia',
'suriname':'Suriname','south sudan':'South Sudan','sao tome & principe':'Sao Tome & Principe','el salvador':'El Salvador','st maarten (dutch)':'St Maarten (Dutch)',
'syria':'Syria','eswatini (swaziland)':'Eswatini (Swaziland)','turks & caicos is':'Turks & Caicos Is','chad':'Chad','french southern & antarctic lands':'French Southern & Antarctic Lands',
'togo':'Togo','thailand':'Thailand','tajikistan':'Tajikistan','tokelau':'Tokelau','east timor':'East Timor','turkmenistan':'Turkmenistan','tunisia':'Tunisia',
'tonga':'Tonga','turkey':'Turkey','trinidad & tobago':'Trinidad & Tobago','tuvalu':'Tuvalu','taiwan':'Taiwan','tanzania':'Tanzania','ukraine':'Ukraine',
'uganda':'Uganda','us minor outlying islands':'US minor outlying islands','united states':'United States','uruguay':'Uruguay','uzbekistan':'Uzbekistan',
'vatican city':'Vatican City','st vincent':'St Vincent','venezuela':'Venezuela','virgin islands (uk)':'Virgin Islands (UK)','virgin islands (us)':'Virgin Islands (US)',
'vietnam':'Vietnam','vanuatu':'Vanuatu','wallis & futuna':'Wallis & Futuna','samoa (western)':'Samoa (western)','yemen':'Yemen','mayotte':'Mayotte',
'south africa':'South Africa','zambia':'Zambia','zimbabwe':'Zimbabwe'}

def search_tz_ctry():
    for i in sorted(pytz.country_names):
        if pytz.country_names[i] in ctry_list2[e4.get()]:
            return pytz.country_timezones(i)

def search_tz():
    list2.delete(0,END)
    for i in search_tz_ctry():
        list2.insert(END,str(i))

def From_To_TS():
    mytime = datetime.strptime(number_hrs.get()+number_min.get(),'%H%M').time()
    date_str = datetime.combine(datetime.strptime(e3.get(),'%d-%m-%Y').date(), mytime)
    datetime_obj_from = timezone(e1.get()).localize(date_str)
    datetime_obj_to = datetime_obj_from.astimezone(timezone(e2.get()))
    return datetime_obj_to.strftime("%d-%m-%Y %H:%M")

def convert_tz():
    list1.delete(0,END)
    to_value = str(From_To_TS())
    list1.insert(END,to_value)

class AutocompleteEntry(Entry):
    def __init__(self, lista, *args, **kwargs):

        Entry.__init__(self, *args, **kwargs)
        self.lista = lista
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)

        self.lb_up = False

    def changed(self, name, index, mode):

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
                    self.lb_up = True

                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False

    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]


l1=Label(window,text="From Timestamp  : ")
l1.grid(row=1,column=0,padx=6,pady=8)

l2=Label(window,text="=")
l2.grid(row=1,column=2)

l3=Label(window,text="To Timestamp      : ")
l3.grid(row=2,column=0,padx=6,pady=8)

l4=Label(window,text="=")
l4.grid(row=2,column=2)

l5=Label(window,text="Search by Country : ")
l5.grid(row=3,column=0,padx=6,pady=8)

l6=Label(window,text="Select Date :")
l6.grid(row=0,column=3)

l7=Label(window,text="Hours :")
l7.grid(row=0,column=4)

l8=Label(window,text="Minutes :")
l8.grid(row=0,column=5)

From_text=StringVar()
e1=Entry(window,textvariable=From_text)
e1.grid(row=1,column=1)

to_text=StringVar()
e2=Entry(window,textvariable=to_text)
e2.grid(row=2,column=1)

From_dt_text=StringVar()
e3=DateEntry(window, width=15, date_pattern='dd-mm-yyyy', background='darkblue', foreground='white')
e3.grid(row=1,column=3)
e3.delete(0,END)

From_hrs_text=StringVar()
number_hrs = Combobox(window, width=4, textvariable=From_hrs_text)
number_hrs['values'] = (f"{0:02d}",f"{1:02d}",f"{2:02d}",f"{3:02d}",f"{4:02d}",f"{5:02d}",f"{6:02d}",f"{7:02d}",f"{8:02d}",f"{9:02d}",\
                        10,11,12,13,14,15,16,17,18,19,20,21,22,23)
number_hrs.grid(row=1,column=4)

From_min_text=StringVar()
number_min = Combobox(window, width=4, textvariable=From_min_text)
number_min['values'] = (f"{0:02d}",f"{1:02d}",f"{2:02d}",f"{3:02d}",f"{4:02d}",f"{5:02d}",f"{6:02d}",f"{7:02d}",f"{8:02d}",f"{9:02d}",\
                        10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59)
number_min.grid(row=1,column=5)

e4 = AutocompleteEntry(ctry_list2.keys(), window)
e4.grid(row=3, column=1)

list1=Listbox(window, height=1,width=19,state="normal")
list1.grid(row=2,column=3)

list2=Listbox(window, height=5,width=21)
list2.grid(row=4,column=1,padx=6,pady=8)

sb1=Scrollbar(window,orient='vertical')
sb1.grid(row=4,column=2,padx=6,pady=8,sticky='NS')

sb2=Scrollbar(window,orient='horizontal')
sb2.grid(row=5,column=1,padx=6,pady=8,sticky='NS')

list2.configure(xscrollcommand=sb2.set,yscrollcommand=sb1.set)
sb1.configure(command=list2.yview)
sb2.configure(command=list2.xview)

list2.bind('<<ListboxSelect>>',get_selected_row)

image_search_path = 'C:/Users/Raj/Desktop/Python_Files/Timezone/Search_logo.png'
Search_logo = PhotoImage(file=image_search_path)
b1=Button(window,image=Search_logo, width=12,style = 'W.TButton',command=search_tz)
b1.grid(row=3,column=2)

b2=Button(window,text="Convert", width=12,style = 'W.TButton',command=convert_tz)
b2.grid(row=3,column=3)

window.mainloop()

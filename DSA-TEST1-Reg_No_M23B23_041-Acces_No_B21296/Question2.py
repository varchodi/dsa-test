catholic_martyrs:list[str]=[
    'Achileo Kiwanuka',
'Adolphus Ludigo-Mukasa',
"Ambrosius ",
"Kibuuka",
"Anatoli ",
"Kiriggwajjo",
"Andrew Kaggwa",
"Antanansio" ,
"Bazzekuketta",
"Bruno" ,
"Sserunkuuma",
"Charles Lwanga",
"Denis" ,
"Ssebuggwawo" ,
"Wasswa",
"Gonzaga Gonza",
"Gyavira Musoke",
"Yowana Mukiibi",
"Yusufu Lugalama",
"Zakayo Lubega",
"James ",
"Buuzaabalyaawo",
"John Maria" ,
"Muzeeyi",
"Joseph Mukasa",
"Kizito",
"Lukka" ,
"Baanabakintu",
"Matiya Mulumba",
"Mbaga Tuzinde",
"Mugagga Lubowa",
"Mukasa" ,
"Kiriwawanvu",
"Nowa Mawaggali",
"Ponsiano" ,
"Ngondwe",

]
anglican_martyrs:list[str]=[
"Aaron Lubega",
"Apollo Kivebulaya",
"Eria Sebukyala",
"Fredrick Kizza",
"George Kizza",
"James Hannington",
"Janani Luwum",
"Joseph", 
"Balikuddembe",
"Kizito",
"Mark Kakumba",
"Matia Mulumba",
"Nuhu Mbegu",
"Robert" ,
"Munyagayirwa",
"Samwiri Mukasa",
"Yefusa Namayanja",
"Yohana Mukasa",
"Yosefu Lugalama",
"Yowana Kitaka",
"Yowana Maria ",
"Mukasa",

]

temp_catholic=catholic_martyrs #this temporary will be used to clear duplicate in anglican martyrs(as we have to clear on both list)
# let remove duplicate on both list
def clear_duplicate():
    #remove duplicate on catholics
    i = 0
    while i < len(catholic_martyrs):
        #print(catholic_martyrs[i])
        if catholic_martyrs[i] in anglican_martyrs:
            catholic_martyrs.remove(catholic_martyrs[i])
        else:
            i += 1
    
clear_duplicate()

#print(anglican_martyrs)
    

#get martyr_len
def martyr_count(name:str)->list[str]:
    if name in anglican_martyrs:
        print(f'group: Anglican')
        return anglican_martyrs
    elif name in catholic_martyrs:
        print(f'group: Catholic')
        return catholic_martyrs
    else:
        return []
        
kizito_group=martyr_count("Kizito")

#check if martyr exist
def is_martyr(name:str)->bool:
    if (name in anglican_martyrs ) or (name in catholic_martyrs):
        return True
    else:
        return False
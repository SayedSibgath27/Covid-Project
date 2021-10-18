from tkinter import*
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
def analyse():
    heading1.configure(text="Please wait processing....",font=200,bg='red')
    #Fetch the data from the combo box
    #dot get() function is used to retrive the data
    selectedstate=state_value.get()
    print(selectedstate)
    #analyse the covid cases for selected state
    confimed=(data.loc[selectedstate]["Confirmed"])
    confimed=list(str(confimed))
    print(confimed)

    con_data=''
    for i in confimed:
        con_data=con_data+i
    print(con_data)


    recovered=(data.loc[selectedstate]["Recovered"])
    recovered=list(str(recovered))
    print(recovered)

    rec_data=''
    for i in recovered:
        rec_data=rec_data+i
    print(rec_data)

    deaths=(data.loc[selectedstate]["Deaths"])
    deaths=list(str(deaths))
    print(deaths)
    det_data=''
    for i in deaths:
        det_data=rec_data+i
    print(det_data)

    #date=data.loc["Uttar Pradesh"]["Date"]
    #date=list(date)
    #print(date)
    
    active=(data.loc[selectedstate]["Active"])
    active=list(str(active))
    print(active)

    act_data=''
    for i in active:
        act_data=act_data+i
    print(act_data)
    
    Clable.configure(text="Confirmed cases:-"+str(con_data),fg='orange')
    Rlable.configure(text="Recovered cases:- "+str(rec_data),fg='Green')
    Dlable.configure(text="Detah cases:-"+str(det_data),fg='blue')
    Alable.configure(text="Active cases:-"+str(act_data),fg='red')
    
    
    #.....END of data analytics 
    #Start of data visualization 
    import pandas as pd
    data1=pd.read_csv("C:\\Users\\HP Elitebook G6\\Desktop\\Python\\window python\\states.csv",index_col="State")
    #Retrive data
    #print(data1)
    
    recovered=data1.loc[selectedstate]["Recovered"]
    recovered_data=list(recovered)
    
    confirmed=data1.loc[selectedstate]["Confirmed"]
    confirmed_data=list(confirmed)
    
    
    Deceased=data1.loc[selectedstate]["Deceased"]
    Deceased_data=list(Deceased)
    #print(recovered_data)
    #print(confirmed_data)
    #print(Deceased_data)
    
    
    date=data1.loc[selectedstate]["Date"]
    date_data=list(date)
    #print(date_data)
    
    



    figure=plt.Figure(figsize=(6,5),dpi=100)
    ax=figure.add_subplot()
    bargraph=FigureCanvasTkAgg(figure,window)
    Graph=bargraph.get_tk_widget()
    Graph.place(x=700, y=160)
    
    #Plot the graph
    df=pd.DataFrame({'Date':date_data,'Confirmed':confirmed_data,'recovered':recovered_data,'Deceased':Deceased_data})
    df.plot.bar(x='Date',y='Confirmed', color='red', legend=True,ax=ax)
    df.plot.bar(x='Date',y='recovered', color='green', legend=True,ax=ax)
    df.plot.bar(x='Date',y='Deceased', color='blue', legend=True,ax=ax)
    heading1.configure(text="Your data is ready to view....",font=200,bg='green')



window=Tk()
window.geometry('1500x1550')
heading=Label(window, text='Covid-19 Application', font=300,fg='red')
heading.place(x=700,y=10)

heading1=Label(window, text='Welcome', font=300,fg='White', bg='green')
heading1.place(x=700,y=40)

state=Label(window, text="Choose the State", font=100)
state.place(x=200,y=150)

Clable=Label(window, text="Confirm cases:-", font=100)
Clable.place(x=200,y=250)

Rlable=Label(window, text="Recovered:-", font=100)
Rlable.place(x=200,y=300)

Dlable=Label(window, text="Death cases:-", font=100)
Dlable.place(x=200,y=350)


Alable=Label(window, text="Active:-", font=100)
Alable.place(x=200,y=400)

#declare a variable in python
state_value=StringVar()
#a=IntVar()
import pandas as pd
data=pd.read_csv("C:\\Users\\HP Elitebook G6\\Desktop\\Python\\covidproject\\state_wise.csv",index_col="State")
#print(data)
state=data['Statename']
#print(state)
state=tuple(state)
print(state)
state_data=ttk.Combobox(window,textvariable=state_value)
state_data['values']=state
state_data.current(2)
state_data.place(x=200,y=120)

btn=Button(window,text="AnalyseCOVID", font=300, fg='blue', command=analyse)
btn.place(x=200,y=200)


figure=plt.Figure(figsize=(6,5),dpi=100)
ax=figure.add_subplot()
bargraph=FigureCanvasTkAgg(figure,window)
Graph=bargraph.get_tk_widget()
Graph.place(x=700, y=160)

window.mainloop()
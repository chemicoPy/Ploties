'''Use this data as sample:
For x axis: 1951,1952,1953,,19551954,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980


For y axis: 1,2,4,7,9,12,14,16,18,19,22,24,34,44,56,76,101,107,113,142,149,154,202,205,209,210,211,213,219,220
'''

generatedPasswords=['1LgiyhcT',
'Vpk!#Os8',
'K2XTUvHt',
'kPYO2AI$',
'V(ebA06I',
'5?jbFKru',
'2ORrhPmk',
'9KxuU?Sn',
'GUB8wPzp',
'!5CUtV0j',
'K8kq%l3j',
'G!MiKFv$',
'M1eFp$S!',
'kQ(o4izt',
'S9nmQ0AG',
'(tWMc6nP',
'aOVIYU(D',
'sOrxQHk&',
'kfW7XK?G',
'#rsL0RCd',
'uNfCLI2F',
'rth8fL3q',
'FSOvf48a',
'L^d503zu',
'QL51wUbk',
'*Vm5nXHw',
'gd9c?6^T',
'Z&50834@',
'$(qW!ewY',
'!azfdi0w',
'zn@jRMi?',
'OXiqSPht',
'&QdVf0m9',
'$9SrQy@l',
'xIUMjzir',
'T*AhE(2d',
'gsSA4^h2',
'?zR9A#1$',
'jUNI5VAQ','SEOYw3au',
'R)d@EAM*',
'i5dQrN@l',
'oetDhM03',
'zc7dFagQ',
'rj2CL0qe',
'RmtyPVLB',
'8JxzSrph',
'g20uTFH@',
'u6wl$X)V',
'iDX3C#6s',
'aswEN3rg',
't5B@&YeN',
'(G%?Wop0',
'f*2OkPKe',
'mja0^u54',
'eKF^(Y!@',
'zC&?%NMe',
'%gr124o(',
'fUpDms6B',
'YA4Xdf$H',
'3#lNV(5z',
'K^Il0*JA',
'&BoSqw%R',
'Tl&qxK0w',
'rceZuHWl',
'12Oqx0X7',
'QBPykima',
'JgF)5tUp',
'euyEl?W0',
'(%ap$hR8',
'kG?oR0j9',
'ltkP2?6q',
'oIt$xzQ@',
'RGcfC5Fu',
'v)0HogMq',
'^AqkWMYZ',
'$othXEkr',
'qsZyWOjv',
'cTV@SgBP',
'id%4sM!z',
'B)vatjx^',
'6rkR(Ddw',
'fOmVvZp%',
'Lm^VDBQn',
'gtSb#1I0',
'A(eg&HN$',
'2lW!^Pzr',
'$e^36(Y)',
'ftVs6*4?',
'wj7AH@Ot',
'3xdgQX0b',
'^6kpwMWa',
'd8ca(iln',
'I1rs!O7f',
'A90OJHn!',
'luh^S*R5',
'@bh*(MZI',
'e00tW)Ui',
'Tj!LM@y9',
'PJZpjqI3']

admin=['Victor','David']


password=input('Enter password from our ticket to use this service:\nAnd wait for a sec for response.')

if password in (generatedPasswords) or password in (admin):
    #import seaborn as sns; sns.set()
    import numpy as np
    import matplotlib.pyplot as plt
    from tkinter import *
    from tkinter.ttk import *
    import tkinter
    from tkinter.messagebox import askquestion
    from tkinter.filedialog import *
    from tkinter.scrolledtext import ScrolledText
    # from PIL import  Image, ImageTk, ImageDraw
    from random import randint
    from numpy.random import randn

    root = Tk()




    var = StringVar()
    label = Label(root, textvariable=var, relief=RAISED)
    var.set(
        "Project Title: A program that asks user for axes of 2 Topics or import file that has the values and does different graphical representations ; one  with its regression line. ")
    label.pack()


    def open():
        textbox = ScrolledText()
        # textbox.grid()
        filename = askopenfilename(initialdir='c:\\python31\\', filetypes=[('Text files', '.txt'), ('All files', '*')])
        s = open('5-year-mean-1882-2014').read()
        textbox.insert(1.0, s)


    def donothing():
        filewin = Toplevel(root)
        button = Button(filewin, text="Do nothing button")
        button.pack()


    def nothing():
        from tkinter import messagebox
        msg = messagebox.showinfo("Warning", "No function assigned yet!.")


    def helpline():
        from tkinter import messagebox
        msg = messagebox.showinfo("Problems with operations?", "Call: +2348148918155.")


    def About():
        from tkinter import messagebox
        msg = messagebox.showinfo("About this Project:",
                                  'This is a self project by OGUNJOBI Victor designed to ask user to input name and time of the day and shows a clock or weather with appropriate greeting.  ')


    def quit():
        answer = askquestion(title='Quit?', message='Really quit?')
        if answer == 'yes':
            root.destroy()


    root.protocol('WM_DELETE_WINDOW', quit)

    root.geometry('300x300')
    root.title("Welcome back, Victor!.")
    var = ("Hey!? How are you doing?")
    label = Label(root, textvariable=var, relief=RAISED, bg='yellow')

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0, bd=2, bg='orange')
    filemenu.add_command(label="New", command=nothing)
    filemenu.add_command(label="Open", command=open)
    filemenu.add_command(label="Save", command=nothing)
    filemenu.add_command(label="Save as...", command=nothing)
    filemenu.add_command(label="Close", command=nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0, bd=2, bg='brown')
    editmenu.add_command(label="Undo", command=nothing)

    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=nothing)
    editmenu.add_command(label="Copy", command=nothing)
    editmenu.add_command(label="Paste", command=nothing)
    editmenu.add_command(label="Delete", command=nothing)
    editmenu.add_command(label="Select All", command=nothing)
    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0, bd=2, bg='purple')
    helpmenu.add_command(label="Help Index", command=nothing)
    helpmenu.add_command(label="About...", command=About)
    helpmenu.add_command(label='Call Author?.', command=helpline)
    menubar.add_cascade(label="Help", menu=helpmenu)
    aboutmenu = Menu(menubar, tearoff=0)
    aboutmenu.add_command(label='About Project', command=About)

    root.config(menu=menubar)



    def plotme():
        import matplotlib.pyplot as plt
        fig = plt.figure()
        first_axis = fig.add_subplot(2, 2, 1)
        second_axis = fig.add_subplot(2, 2, 2)
        third_axis = fig.add_subplot(2, 2, 3)
        fourth_axis = fig.add_subplot(2, 2, 4)

        '''
        The whole logic here is just to enable multiple
        points on the graph as users enter values separated
        by a comma
        '''

        E1_short = E1.get()
        num_x = []
        for i in (E1_short.split(",")):
            if i.isdigit():
                num_x.append(int(i))
        E2_short = E2.get()
        num_y = []
        for i in (E2_short.split(",")):
            if i.isdigit():
                num_y.append(int(i))

        first_axis= plt.plot(num_x, num_y,label='x-axis against y-axis')
        #first_axis.legend(loc='center')

        second_axis.scatter(num_x, num_y, label='Scatter - graph form of the axes')
        second_axis.legend(loc='center')

        third_axis.hist(num_x, num_y, label='Histogram of the axes')
        third_axis.legend(loc='center')

        #fourth_axis=sns.violinplot(num_x, num_y)



        '''first_axis.plot(randn(1000).cumsum(), 'k--', label='-- is for')
        first_axis.plot(randn(1000).cumsum(), 'k--', label='. is for')'''

        plotit = plt.xlabel('x axis', fontsize='small')
        plt.ylabel('y axis', fontsize='small')
        plt.title('Graph of x - axis against y - axis.', fontsize='small')
        #plt.scatter(num_x, num_y, edgecolors='black')
        #plt.plot(num_x, num_y)

        plt.yticks(color='blue')
        plt.xticks(color='darkred')
        #sns.regplot(num_x, num_y)
        plt.show()

        #        plotgraph= Label(root,text='$%.2f'% plotit).grid(x=605, y=500)
        plt.draw_all((num_x, num_y))
        return


    E1 = StringVar()
    E2 = StringVar()

    lblE1 = Label(root, text="Give points on x axis:", font=('batang', 9, 'bold'))
    lblE1.place(x=509, y=238)
    entE1 = Entry(root, textvariable=E1)
    entE1.place(x=653, y=239)

    lblE2 = Label(root, text="Give points on y axis:", font=('batang', 9, 'bold'))
    lblE2.place(x=510, y=300)
    entE2 = Entry(root, textvariable=E2)
    entE2.place(x=653, y=300)

    plotnow = Button(root, text="Plot Graph", font=('batang', 10, 'bold'), borderwidth='4', foreground='darkblue',
                     command=plotme)
    plotnow.place(x=605, y=500)

    root.configure(bg='darkred')  # Fine colours : Chocolate, fuchsia, darkred, darkblue
    root.mainloop()




else:
    print("Access Denied, Wrong Password!.")
    print('Helpline: +2348148918155')
























'''
    fig = plt.figure()
    first_axis = fig.add_subplot(2, 2, 1)
    second_axis = fig.add_subplot(2, 2, 2)
    third_axis = fig.add_subplot(2, 2, 3)
    fourth_axis = fig.add_subplot(2, 2, 4)

    plt.yticks(color='green')
    plt.xticks(color='red')

    ticks = first_axis.set_xticks([E1,E2])

loc can be:
       upper left
   	center left
   	lower center
   	lower left
   	right
   	upper right
   	upper center
   	lower right
   	center right
   	best
   	center

_ = first_axis.hist(randn(100), bins=20, color='k', alpha=0.3), first_axis.plot(randn(1000).cumsum(),label='Title here')
    # first_axis.hist(randn(100), color='k', alpha=0.3),first_axis.plot(randn(1000).cumsum(), label='Title here')
first_axis.legend(loc='center')

second_axis.scatter(np.arange(30), np.arange(30) + 3 * randn(30), label='Title here')
second_axis.legend(loc='center')

third_axis.hist(x, y, label='Title here')
third_axis.legend(loc='center')

first_axis.plot(randn(1000).cumsum(), 'k--', label='-- is for')
first_axis.plot(randn(1000).cumsum(), 'k--', label='. is for')

   # fourth_axis.legend(loc='center')

 plt.xlabel('x axis', fontsize='small')
   plt.ylabel('y axis',fontsize='small')
   plt.title('Title here',fontsize='small')
   

plt.plot(randn(50).cumsum(), 'k--')
plt.plot(randn(30).cumsum(), 'ko--')


b=0
for r in range(6):
    for c in range(6):
        b=b+1
        Button(root, text=str(b),borderwidth=1 ) 

 C = Canvas(root,height=100000000,width=100000000, bg="indigo")
C.place(x=10, y=10)
C.pack()




canvas = Canvas(width=300, height=300)
canvas.grid()
image=Image.new(mode='RGB',size=(300,300))
draw = ImageDraw.Draw(image)
draw.rectangle([(0,0),(300, 300)],fill='#000030')
L = [(randint(0,299), randint(0, 299)) for i in range(100)]
draw.point(L, fill='yellow')
#photo=ImageTk.PhotoImage(image)
#canvas.create_image(0,0,image=photo,anchor=NW)   

root.configure(bg='chocolate')

root.mainloop()


frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )
blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)


C = Canvas(top, bg="blue", height=250, width=300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
line = C.create_line(10,10,200,200,fill='white')
C.pack()
root.mainloop()

L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)   '''







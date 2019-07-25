from tkinter import *
from tkinter import ttk
from tkinter import Toplevel
from tkinter.filedialog import askopenfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from mpl_toolkits import mplot3d
# plt.rcParams.update({'figure.max_open_warning': 0})

import numpy as np
import time
import math
import os.path
from sklearn.cluster import MeanShift

from readFile import readFilePart
from changeLang import changeLang


def isFloat(stringToTest):
    try:
        float(stringToTest)
        return True
    except:
        return False
		

class InterfaceGraphe():
	def __init__(self):

		self.root = Tk()
		self.root.title('Particles Application')
		self.root.protocol('WM_DELETE_WINDOW', self.root.quit)
		self.root.resizable(width=False, height=False)

		# Langue

		# self.language = [
		# 'HOME',
		# 'DATA',
		# 'PLOT ENERGY',
		# 'HISTOGRAM ENERGY',
		# 'PLOT VELOCITY',
		# 'HISTOGRAM VELOCITY',
		# 'HELP',

		# # 7
		# 'File :',
		# 'None',
		# '',
		# 'Number of particles : ',
		# 'Min is : ',
		# 'Max is : ',

		# # 13
		# 'Home',
		# 'Data',
		# 'Plot Energy',
		# 'Histogram Energy',
		# 'Plot Velocity',
		# 'Histogram Velocity',
		# 'Help',

		# # 20
		# 'Welcome',

		# # 21
		# 'Choose File :',
		# 'Browse',
		# 'Select number of sort of particles :',
		# 'OK',

		# # 25
		# 'Particle find : ',
		# 'Face',
		# 'Energy From :',
		# 'To :',
		# 'OK',
		# 'Save as :',
		# 'Save',

		# # 32
		# 'Save as :',
		# 'Save',

		# # 34
		# 'No file selected !',
		# 'Select a number !',
		# 'Part : ',
		# ' J',

		# # 38
		# 'It\'s not a float !',
		# 'Enter a positif number !',
		# '1 is the maximum !',
		# ' is the minimum !',
		# 'Select a slice !',
		# 'Choose language :',
		# 'OK'
		# ]

		self.language = changeLang(0)


		# Argument function

		self.fileName = self.language[8]
		self.num = 1
		self.nb_part_file = 0
		self.max = 0
		self.min = 0
		self.maxvel = 0
		self.minvel = 0

		self.slice = 0.0
		self.Dslice = 0.0
		self.actualSlice = ''
		self.nb = 0

		self.slicevel = 0.0
		self.Dslicevel = 0.0
		self.actualSlicevel = ''
		self.nbvel = 0

		self.Axis1=0.0
		self.Axis2=1.0
		self.Axis1vel=0.0
		self.Axis2vel=1.0

		self.scalevalue = 10
		self.scalevaluevel = 10


		self.boxe_prise = StringVar()
		self.boxe_prise_2 = StringVar()


		# Argument graph

		self.parttab = 0
		self.tabPart = []
		self.energy = []
		self.velocity = []

		# Graph

		fig = plt.figure(figsize=(12, 7), dpi=96)
		fig2 = plt.figure(figsize=(12, 6), dpi=96)
		fig3 = plt.figure(figsize=(12, 7), dpi=96)
		fig4 = plt.figure(figsize=(12, 6), dpi=96)
		fig5 = plt.figure(figsize=(12, 7), dpi=96)

		
		#Clusters

		self.clusters=[]


		self.creationCanvas()




	def creationCanvas(self):


		try:
			self.language = changeLang(self.listBox.curselection()[0])
			self.fileName = self.language[8]
		except:
			pass




		tmp = 0
		tmp_vide = 9
		tmp_unit = 37
		tmp_save = 32
		tmp_lang = 43



		# Creation des canevas

		self.menu = Canvas(self.root,width =1000, height=30, bg = '#AAAAAA', highlightthickness=0)
		self.menu.grid(row=0, column=1, padx=1, pady=1)
		self.menu.grid_propagate(0)

		self.title = Canvas(self.root,width =1000, height =50, highlightthickness=0)
		self.title.grid(row=1,column=1,padx=1, pady=1,sticky=W)
		self.title.grid_propagate(0)

		self.file = Canvas(self.root,width =1000, height =100, highlightthickness=0)
		self.file.grid(row=2,column=1,padx=1, pady=1,sticky=W)
		self.file.grid_propagate(0)

		self.can_home = Canvas(self.root,width =1000, height =400, highlightthickness=0)
		self.can_home.grid(row=3,column=1,padx=1, pady=1)
		self.can_home.grid_propagate(0)

		self.can_data = Canvas(self.root,width =1000, height =400, highlightthickness=0)
		self.can_data.grid_propagate(0)

		self.can_plot = Canvas(self.root, highlightthickness=0)

		self.can_histo = Canvas(self.root, highlightthickness=0)

		self.can_plotvel = Canvas(self.root, highlightthickness=0)

		self.can_histovel = Canvas(self.root, highlightthickness=0)

		self.can_help = Canvas(self.root, highlightthickness=0)



		# L'entete

		self.entete_home = Label(self.title,text = self.language[tmp], font=(None, 15))
		tmp += 1
		self.entete_home.grid(row = 0, column = 0 ,padx=10)


		self.entete_data = Label(self.title,text = self.language[tmp], font=(None, 15))
		tmp += 1

		self.entete_plot = Label(self.title,text = self.language[tmp], font=(None, 15))
		tmp += 1
		
		self.entete_histo = Label(self.title,text = self.language[tmp], font=(None, 15))
		tmp += 1

		self.entete_plotvel = Label(self.title,text = self.language[tmp], font=(None, 15))
		tmp += 1

		self.entete_histovel = Label(self.title,text = self.language[tmp], font=(None, 15))
		tmp += 1

		self.entete_help = Label(self.title,text = self.language[tmp], font=(None, 15))
		tmp += 1


		# File

		fileNameCont = Canvas(self.file, highlightthickness=0)
		fileNameCont.grid(row=0,column=1,padx=1, pady=1,sticky=W)

		label = Label(fileNameCont, text = self.language[tmp])
		tmp += 1
		label.grid(row=1, column=1,padx=10,pady=2)

		self.fileNameLabel = Label(fileNameCont, text = self.fileName)
		tmp += 1
		self.fileNameLabel.grid(row=1, column=2,pady=2)

		self.part = Label(fileNameCont, text = self.language[tmp])
		tmp += 1
		self.part.grid(row=1, column=3,pady=2)

		self.labelNumber = Label(self.file, text = self.language[tmp] + '0')
		tmp += 1
		self.labelNumber.grid(row = 1, column = 1,padx=10, pady=1,sticky=W)

		self.labelenergy = Label(self.file, text = "Energy")
		self.labelenergy.grid(row = 2, column = 1,padx=10, pady=1,sticky=W)

		self.labelvelocity = Label(self.file, text = "Velocity")
		self.labelvelocity.grid(row = 2, column = 2,padx=10, pady=1,sticky=W)

		self.labelMin = Label(self.file, text = self.language[tmp] + str(self.min) + self.language[tmp_unit])
		self.labelMinvel = Label(self.file, text = self.language[tmp] + str(self.minvel) + " cm/s")
		tmp += 1
		self.labelMin.grid(row = 3, column = 1,padx=10, pady=1,sticky=W)
		self.labelMinvel.grid(row = 3, column = 2,padx=10, pady=1,sticky=W)

		self.labelMax = Label(self.file, text = self.language[tmp] + str(self.max) + self.language[tmp_unit])
		self.labelMaxvel = Label(self.file, text = self.language[tmp] + str(self.maxvel) + " cm/s")
		tmp += 1
		self.labelMax.grid(row = 4, column = 1,padx=10, pady=1,sticky=W)
		self.labelMaxvel.grid(row = 4, column = 2,padx=10, pady=1,sticky=W)


		# Les boutons pour Menu

		bou1 = ttk.Button(self.menu, text = self.language[tmp], width = 15, command = self.returnHome)
		tmp += 1
		bou1.grid(row=1, column=1,padx=2, pady=2,sticky=W)

		bou2 = ttk.Button(self.menu, text=self.language[tmp], width = 15, command = self.changeDataFile)
		tmp += 1
		bou2.grid(row=1, column=2,padx=2, pady=2,sticky=W)

		bou3 = ttk.Button(self.menu, text=self.language[tmp], width = 15)
		tmp+=1
		bou3.bind("<Button-1>", self.plotPart)
		bou3.grid(row=1, column=3,padx=2, pady=2,sticky=W)

		bou4 = ttk.Button(self.menu, text=self.language[tmp], width = 15, command = self.histo)
		tmp += 1
		bou4.grid(row=1, column=5,padx=2, pady=2,sticky=W)

		bou5 = ttk.Button(self.menu, text=self.language[tmp], width = 15)
		tmp += 1
		bou5.bind("<Button-1>", self.plotPartVel)
		bou5.grid(row=1, column=6,padx=2, pady=2,sticky=W)

		bou6 = ttk.Button(self.menu, text=self.language[tmp], width = 15, command = self.histovel)
		tmp += 1
		bou6.grid(row=1, column=7,padx=2, pady=2,sticky=W)

		bou7 = ttk.Button(self.menu, text=self.language[tmp], width = 15)
		tmp += 1
		bou7.grid(row=1, column=8,padx=2, pady=2,sticky=W)


		# Canvas de Home

		Label(self.can_home, text = self.language[tmp], font=(None, 30)).grid(sticky = W, row = 0, column = 0, padx = 10, pady = 10)
		tmp += 1

		langCanvas = Canvas(self.can_home, highlightthickness=0)

		label = Label(langCanvas, text = self.language[tmp_lang])
		label.grid(row = 0, column = 1,pady=1,sticky=W)


		listFrame = Frame(langCanvas)
		listFrame.grid(row = 1, column =1,pady=1,sticky=W)

		scrollBar = Scrollbar(listFrame)
		scrollBar.pack(side=RIGHT, fill=Y)
		self.listBox = Listbox(listFrame, selectmode=SINGLE)
		self.listBox.pack(side=LEFT, fill=Y)
		scrollBar.config(command=self.listBox.yview)
		self.listBox.config(yscrollcommand=scrollBar.set)

		self.listBox.insert(1, "English")
		self.listBox.insert(2, "Francais")
		self.listBox.insert(3, "русский")

		but = ttk.Button(langCanvas, text=self.language[tmp_lang+1], width = 15, command = self.creationCanvas)
		but.grid(row = 2, column =1,pady=1,sticky=W)

		langCanvas.grid(row = 1, column = 0,padx = 10,pady=50,sticky=W)


		# Canvas de Data

		fileCan = Canvas(self.can_data, highlightthickness=0)

		labelName = Label(fileCan, text = self.language[tmp])
		tmp += 1
		labelName.grid(row = 0, column = 0, pady=2,sticky=W)

		filebrowser = Button(fileCan, text = self.language[tmp], command = self.loadtemplate, width = 10)
		tmp += 1
		filebrowser.grid(row = 1, column = 0,pady=2,sticky=W)

		self.entName = Label(fileCan,text = self.fileName)
		self.entName.grid(row = 1, column = 1, pady=2,sticky=W)

		fileCan.grid(row = 1, column = 0, padx=10, pady=2,sticky=W)

		self.errorName = Label(self.can_data,fg='red')
		self.errorName.grid(row = 2, column = 0, padx=10, pady=2,sticky=W)

		n = Label(self.can_data, text = self.language[tmp])
		tmp += 1
		n.grid(row = 3, column = 0, padx=10, pady=2,sticky=W)

		radio = Canvas(self.can_data)

		sort1 = Radiobutton (radio, text="1", variable = self.boxe_prise, value = "1")
		sort2 = Radiobutton (radio, text="2", variable = self.boxe_prise, value = "2")
		sort3 = Radiobutton (radio, text="3", variable = self.boxe_prise, value = "3")
		sort4 = Radiobutton (radio, text="All", variable = self.boxe_prise, value = "4")

		sort1.grid(row=1,column=2)
		sort2.grid(row=1,column=3)
		sort3.grid(row=1,column=4)
		sort4.grid(row=1,column=5)

		radio.grid(row = 4, column = 0,padx=10, pady=2,sticky=W)

		self.errorNum = Label(self.can_data,fg='red')
		self.errorNum.grid(row = 5, column = 0, padx=10, pady=2,sticky=W)

		valid = ttk.Button(self.can_data, text=self.language[tmp], width = 15)
		tmp += 1
		valid.bind('<Button-1>',self.changeDataFileButton)
		self.root.bind('<Return>', self.changeDataFileButton)
		
		valid.grid(row = 6, column = 0, padx=10, pady=2,sticky=W)
		
		self.loading1 = Label(self.can_data)
		self.loading1.grid(row = 7, column = 0,padx=10, pady=1,sticky=W)


		# Canvas de Plot 2D

		fig = plt.figure(1)
		self.graph = FigureCanvasTkAgg(fig, master = self.can_plot)
		self.graph.get_tk_widget().pack(side='left', fill='both', expand=1, pady = 10)

		self.menuFig = Canvas(self.can_plot, width = 300, highlightthickness=0)
		self.menuFig.pack(side='right', fill='both', expand=1)

		self.nb_label = Label(self.menuFig, text = self.language[tmp] + str(self.nb))
		tmp += 1
		self.nb_label.grid(row=0,column=1, padx=10, pady=10,sticky=W)

		radio = Canvas(self.menuFig)

		label = Label(radio, text=self.language[tmp])
		tmp += 1
		label.grid(row=1,column=1)

		x = Radiobutton (radio, text="X", variable = self.boxe_prise_2, value = "x", command=self.SliceFace)
		y = Radiobutton (radio, text="Y", variable = self.boxe_prise_2, value = "y", command=self.SliceFace)
		z = Radiobutton (radio, text="Z", variable = self.boxe_prise_2, value = "z", command=self.SliceFace)

		x.grid(row=1,column=2)
		y.grid(row=1,column=3)
		z.grid(row=1,column=4)

		radio.grid(row = 1, column = 1,padx=10, pady=10,sticky=W)

		self.errorRadio = Label(self.menuFig,fg='red')
		self.errorRadio.grid(row = 2, column = 1,padx=10, pady=1,sticky=W)


		label1 = Label(self.menuFig, text = "Slice selection :")
		label1.grid(row = 3, column = 1,padx=10, pady=1,sticky=W)

		self.sliceAxis1 = Scale(self.menuFig, orient='horizontal', sliderlength = 10, resolution=0.00001, length=250, from_=0.0, to=1.2)
		self.sliceAxis1.grid(row = 5,column = 1,padx=10, pady=1,sticky=W)

		self.sliceAxis2 = Scale(self.menuFig, orient='horizontal', sliderlength = 10, resolution=0.00001, length=250, from_=0.0, to=1.2)
		self.sliceAxis2.grid(row = 7,column = 1,padx=10, pady=1,sticky=W)

		self.errorAxis = Label(self.menuFig,fg='red')
		self.errorAxis.grid(row = 8, column = 1,padx=10, pady=1,sticky=W)



		label2 = Label(self.menuFig, text = self.language[tmp])
		tmp += 1
		label2.grid(row = 9, column = 1,padx=10, pady=1,sticky=W)

		self.sliceValue = Scale(self.menuFig, orient='horizontal', sliderlength = 10, resolution=0.000000000000001, length=250, from_=self.min, to=self.max)
		self.sliceValue.grid(row = 11,column = 1,padx=10, pady=1,sticky=W)

		self.errorenergy = Label(self.menuFig,fg='red')
		self.errorenergy.grid(row = 12, column = 1,padx=10, pady=1,sticky=W)


		label3 = Label(self.menuFig, text =self.language[tmp])
		tmp += 1
		label3.grid(row = 13, column = 1,padx=10, pady=1,sticky=W)


		self.deltaValue = Scale(self.menuFig, orient='horizontal', sliderlength = 10, resolution=0.000000000000001, length=250, from_=self.min, to=self.max)
		self.deltaValue.grid(row = 15,column = 1,padx=10, pady=1,sticky=W)


		self.errorDelta = Label(self.menuFig,fg='red')
		self.errorDelta.grid(row = 16, column = 1,padx=10, pady=1,sticky=W)
	
		valid = Button(self.menuFig, text = self.language[tmp], width = 10)
		tmp += 1
		self.root.bind('<Return>', self.plotPartButton)
		valid.bind('<Button-1>', self.plotPartButton)
		valid.grid(row = 17, column = 1,padx = 10,pady=2,sticky=W)

		self.loading2 = Label(self.menuFig)
		self.loading2.grid(row = 18, column = 1,padx=10, pady=1,sticky=W)

		clustering = ttk.Button(self.menuFig, text="Clusters", width = 15, command = self.Kmeans)
		clustering.grid(row = 20, column =1,padx=10,pady=1,sticky=W)

		self.nbrclusters = Label(self.menuFig)
		self.nbrclusters.grid(row = 21, column = 1,padx=10, pady=1,sticky=W)

		saveCanvas = Canvas(self.menuFig, highlightthickness=0)

		label = Label(saveCanvas, text = self.language[tmp])
		tmp += 1
		label.grid(row = 0, column = 1,pady=1,sticky=W)

		self.saveName1 = Entry(saveCanvas)
		self.saveName1.grid(row = 1, column = 1,pady=1,sticky=W)

		saveBut = ttk.Button(saveCanvas, text=self.language[tmp], width = 15, command = self.savePlt)
		tmp += 1
		saveBut.grid(row = 2, column =1,pady=1,sticky=W)

		saveCanvas.grid(row = 22, column = 1,padx = 10,pady=50,sticky=W)

		self.createPlot()

		# Canvas de l'histogramme

		fig = plt.figure(2)
		self.canvas = FigureCanvasTkAgg(fig, master = self.can_histo)
		self.canvas.get_tk_widget().pack(side='left', fill='both', expand=1)

		self.menuFig_2 = Canvas(self.can_histo)

		saveCanvas = Canvas(self.menuFig_2, highlightthickness=0)

		label = Label(saveCanvas, text = self.language[tmp_save])
		label.grid(row = 0, column = 1,pady=1,sticky=W)

		self.saveName2 = Entry(saveCanvas)
		self.saveName2.grid(row = 1, column = 1,pady=1,sticky=W)

		saveBut = ttk.Button(saveCanvas, text=self.language[tmp_save+1], width = 15, command = self.savePlt2)
		saveBut.grid(row = 2, column =1,pady=1,sticky=W)

		saveCanvas.grid(row = 0, column = 0,padx = 10,pady=50,sticky=W)

		slide = Canvas(self.menuFig_2, highlightthickness=0)

		scale = Scale(slide, orient='vertical', sliderlength = 30, tickinterval = 49, length=600, from_=1, to=300, command = self.slideValue)
		scale.set(self.scalevalue)
		scale.grid(row = 1, column = 0,padx = 50)

		self.showNumber = Label(slide,text = "" )
		self.showNumber.grid(row = 2, column = 0)
		self.showenergy = Label(slide,text = "" )
		self.showenergy.grid(row = 3, column = 0)

		slide.grid(row = 1, column = 0)

		self.menuFig_2.pack(side = "right")


		# Canvas de Plot Velocity

		fig3 = plt.figure(3)
		self.graphvel = FigureCanvasTkAgg(fig3, master = self.can_plotvel)
		self.graphvel.get_tk_widget().pack(side='left', fill='both', expand=1, pady = 10)

		self.menuFigVel = Canvas(self.can_plotvel, width = 300, highlightthickness=0)
		self.menuFigVel.pack(side='right', fill='both', expand=1)

		self.nb_labelvel = Label(self.menuFigVel, text = "Particles find" + str(self.nb))
		#tmp += 1
		self.nb_labelvel.grid(row=0,column=1, padx=10, pady=10,sticky=W)

		radio = Canvas(self.menuFigVel)

		label = Label(radio, text="Face : ")
		#tmp += 1
		label.grid(row=1,column=1)

		x = Radiobutton (radio, text="X", variable = self.boxe_prise_2, value = "x", command=self.SliceFace)
		y = Radiobutton (radio, text="Y", variable = self.boxe_prise_2, value = "y", command=self.SliceFace)
		z = Radiobutton (radio, text="Z", variable = self.boxe_prise_2, value = "z", command=self.SliceFace)

		x.grid(row=1,column=2)
		y.grid(row=1,column=3)
		z.grid(row=1,column=4)

		radio.grid(row = 1, column = 1,padx=10, pady=10,sticky=W)

		self.errorRadiovel = Label(self.menuFig,fg='red')
		self.errorRadiovel.grid(row = 2, column = 1,padx=10, pady=1,sticky=W)


		label1 = Label(self.menuFigVel, text = "Slice selection :")
		label1.grid(row = 3, column = 1,padx=10, pady=1,sticky=W)

		self.sliceAxis1vel = Scale(self.menuFigVel, orient='horizontal', sliderlength = 10, resolution=0.00001, length=250, from_=0.0, to=1.2)
		self.sliceAxis1vel.grid(row = 5,column = 1,padx=10, pady=1,sticky=W)

		self.sliceAxis2vel = Scale(self.menuFigVel, orient='horizontal', sliderlength = 10, resolution=0.00001, length=250, from_=0.0, to=1.2)
		self.sliceAxis2vel.grid(row = 7,column = 1,padx=10, pady=1,sticky=W)

		self.errorAxisvel = Label(self.menuFigVel,fg='red')
		self.errorAxisvel.grid(row = 8, column = 1,padx=10, pady=1,sticky=W)



		label2 = Label(self.menuFigVel, text = "Velocity from :")
		#tmp += 1
		label2.grid(row = 9, column = 1,padx=10, pady=1,sticky=W)

		self.sliceValuevel = Scale(self.menuFigVel, orient='horizontal', sliderlength = 10, resolution=0.0000000001, length=250, from_=self.minvel, to=self.maxvel)
		self.sliceValuevel.grid(row = 11,column = 1,padx=10, pady=1,sticky=W)

		self.errorvelocity = Label(self.menuFigVel,fg='red')
		self.errorvelocity.grid(row = 12, column = 1,padx=10, pady=1,sticky=W)


		label3 = Label(self.menuFigVel, text ="to :")
		#tmp += 1
		label3.grid(row = 13, column = 1,padx=10, pady=1,sticky=W)


		self.deltaValuevel = Scale(self.menuFigVel, orient='horizontal', sliderlength = 10, resolution=0.0000000001, length=250, from_=self.minvel, to=self.maxvel)
		self.deltaValuevel.grid(row = 15,column = 1,padx=10, pady=1,sticky=W)


		self.errorDeltavel = Label(self.menuFigVel,fg='red')
		self.errorDeltavel.grid(row = 16, column = 1,padx=10, pady=1,sticky=W)
	
		valid = Button(self.menuFigVel, text = "OK", width = 10)
		#tmp += 1
		self.root.bind('<Return>', self.plotPartButtonVel)
		valid.bind('<Button-1>', self.plotPartButtonVel)
		valid.grid(row = 17, column = 1,padx = 10,pady=2,sticky=W)

		self.loading2vel = Label(self.menuFigVel)
		self.loading2vel.grid(row = 18, column = 1,padx=10, pady=1,sticky=W)

		saveCanvas = Canvas(self.menuFigVel, highlightthickness=0)

		label = Label(saveCanvas, text = "Save as")
		#tmp += 1
		label.grid(row = 0, column = 1,pady=1,sticky=W)

		self.saveName3 = Entry(saveCanvas)
		self.saveName3.grid(row = 1, column = 1,pady=1,sticky=W)

		saveBut = ttk.Button(saveCanvas, text="Save", width = 15, command = self.savePlt3)
		#tmp += 1
		saveBut.grid(row = 2, column =1,pady=1,sticky=W)

		saveCanvas.grid(row = 19, column = 1,padx = 10,pady=50,sticky=W)

		self.createPlotVel()


		# Canvas de l'histogramme velocity

		fig4 = plt.figure(4)
		self.canvasvel = FigureCanvasTkAgg(fig4, master = self.can_histovel)
		self.canvasvel.get_tk_widget().pack(side='left', fill='both', expand=1)

		self.menuFig_4 = Canvas(self.can_histovel)

		saveCanvas = Canvas(self.menuFig_2, highlightthickness=0)

		label = Label(saveCanvas, text = self.language[tmp_save])
		label.grid(row = 0, column = 1,pady=1,sticky=W)

		self.saveName4 = Entry(saveCanvas)
		self.saveName4.grid(row = 1, column = 1,pady=1,sticky=W)

		saveBut = ttk.Button(saveCanvas, text=self.language[tmp_save+1], width = 15, command = self.savePlt4)
		saveBut.grid(row = 2, column =1,pady=1,sticky=W)

		saveCanvas.grid(row = 0, column = 0,padx = 10,pady=50,sticky=W)

		slide = Canvas(self.menuFig_2, highlightthickness=0)

		scale = Scale(slide, orient='vertical', sliderlength = 30, tickinterval = 49, length=600, from_=1, to=300, command = self.slideValueVel)
		scale.set(self.scalevaluevel)
		scale.grid(row = 1, column = 0,padx = 50)

		self.showNumberself = Label(slide,text = "" )
		self.showNumberself.grid(row = 2, column = 0)
		self.showvelocity = Label(slide,text = "" )
		self.showvelocity.grid(row = 3, column = 0)

		slide.grid(row = 1, column = 0)

		self.menuFig_4.pack(side = "right")

		

	def updateCanvas(self):

		# Canvas de Plot 2D


		self.sliceValue = Scale(self.menuFig, orient='horizontal', sliderlength = 10, resolution=0.000000000000001, length=250, from_=self.min, to=self.max)
		self.sliceValue.grid(row = 11,column = 1,padx=10, pady=1,sticky=W)

		self.deltaValue = Scale(self.menuFig, orient='horizontal', sliderlength = 10, resolution=0.000000000000001, length=250, from_=self.min, to=self.max)
		self.deltaValue.grid(row = 15,column = 1,padx=10, pady=1,sticky=W)

		self.createPlot()

		# Canvas de l'histogramme


		slide = Canvas(self.menuFig_2, highlightthickness=0)

		scale = Scale(slide, orient='vertical', sliderlength = 30, tickinterval = 49, length=600, from_=1, to=300, command = self.slideValue)
		scale.set(self.scalevalue)
		scale.grid(row = 1, column = 0,padx = 50)

		self.showNumber = Label(slide,text = "" )
		self.showNumber.grid(row = 2, column = 0)
		self.showenergy = Label(slide,text = "" )
		self.showenergy.grid(row = 3, column = 0)

		slide.grid(row = 1, column = 0)

		self.menuFig_2.pack(side = "right")

		# Canvas de Plot Velocity


		self.sliceValuevel = Scale(self.menuFigVel, orient='horizontal', sliderlength = 10, resolution=0.000000000001, length=250, from_=self.minvel, to=self.maxvel)
		self.sliceValuevel.grid(row = 11,column = 1,padx=10, pady=1,sticky=W)

		self.deltaValuevel = Scale(self.menuFigVel, orient='horizontal', sliderlength = 10, resolution=0.000000000001, length=250, from_=self.minvel, to=self.maxvel)
		self.deltaValuevel.grid(row = 15,column = 1,padx=10, pady=1,sticky=W)

		self.createPlotVel()

		# Canvas de l'histogramme


		slide = Canvas(self.menuFig_4, highlightthickness=0)

		scale = Scale(slide, orient='vertical', sliderlength = 30, tickinterval = 49, length=600, from_=1, to=300, command = self.slideValueVel)
		scale.set(self.scalevaluevel)
		scale.grid(row = 1, column = 0,padx = 50)

		self.showNumbervel = Label(slide,text = "" )
		self.showNumbervel.grid(row = 2, column = 0)
		self.showvelocity = Label(slide,text = "" )
		self.showvelocity.grid(row = 3, column = 0)

		slide.grid(row = 1, column = 0)

		self.menuFig_4.pack(side = "right")


	def onpick1(self,event):
		thisline = event.artist
		ind = event.ind
		
		if (self.boxe_prise_2.get() == 'x'):
			self.y=self.centers[ind[0]][0]
			self.z=self.centers[ind[0]][1]
			self.x=self.centers[ind[0]][2]
		elif (self.boxe_prise_2.get() == 'y'):
			self.y=self.centers[ind[0]][2]
			self.z=self.centers[ind[0]][1]
			self.x=self.centers[ind[0]][0]
		elif (self.boxe_prise_2.get() == 'z'):
			self.y=self.centers[ind[0]][1]
			self.z=self.centers[ind[0]][2]
			self.x=self.centers[ind[0]][0]
		self.plotElec()


	def Kmeans(self):
		fig = plt.figure(1)
		plt.clf()
		if (self.boxe_prise_2.get() == 'x'):
			plt.title('Plasma particles energy (J) Y and Z')
			plt.xlabel('Y (cm)')
			plt.ylabel('Z (cm)')
		elif (self.boxe_prise_2.get() == 'y'):
			plt.title('Plasma particles energy (J) X and Z')
			plt.xlabel('X (cm)')
			plt.ylabel('Z (cm)')
		elif (self.boxe_prise_2.get() == 'z'):
			plt.title('Plasma particles energy (J) X and Y')
			plt.xlabel('X (cm)')
			plt.ylabel('Y (cm)')
		kmeans=MeanShift(bandwidth = 0.01).fit(self.clusters)
		self.centers=kmeans.cluster_centers_
		labels=kmeans.labels_
		labels_unique=np.unique(labels)
		plt.scatter(self.abss,self.ordn, c = labels, s = 10, marker = 'o', cmap = 'gist_ncar',edgecolor = 'none')
		ax = plt.gca()
		abscenter=[]
		ordcenter=[]
		for i in range(len(self.centers)):
			l=0.0
			h=0.0
			for j in range(len(labels)):
				if i==labels[j]:
					l_tmp=abs(self.abss[j]-self.centers[i][0])
					h_tmp=abs(self.ordn[j]-self.centers[i][1])
					if l_tmp>l:
						l=l_tmp
					if h_tmp>h:
						h=h_tmp
			abscenter+=[self.centers[i][0]]
			ordcenter+=[self.centers[i][1]]
			ellipse=Ellipse((self.centers[i][0],self.centers[i][1]),width=2*l,height=2*h,color="fuchsia",fill=False,linewidth=0.5)
			ax.add_artist(ellipse)
		plt.plot(abscenter,ordcenter,"ro",color="fuchsia",picker="True")
		fig.canvas.mpl_connect('pick_event', self.onpick1)
		self.graph.draw()
		self.nbrclusters['text'] = str(len(self.centers)) + " clusters"


	def SliceFace(self):
		if (self.boxe_prise_2.get() == 'x'):
			self.sliceAxis1.configure(from_=0.0, to=1.2)
			self.sliceAxis2.configure(from_=0.0, to=1.2)
			self.sliceAxis1vel.configure(from_=0.0, to=1.2)
			self.sliceAxis2vel.configure(from_=0.0, to=1.2)
		elif (self.boxe_prise_2.get() == 'y'):
			self.sliceAxis1.configure(from_=0.0, to=0.05)
			self.sliceAxis2.configure(from_=0.0, to=0.05)
			self.sliceAxis1vel.configure(from_=0.0, to=0.05)
			self.sliceAxis2vel.configure(from_=0.0, to=0.05)
		elif (self.boxe_prise_2.get() == 'z'):
			self.sliceAxis1.configure(from_=0.0, to=0.05)
			self.sliceAxis2.configure(from_=0.0, to=0.05)
			self.sliceAxis1vel.configure(from_=0.0, to=0.05)
			self.sliceAxis2vel.configure(from_=0.0, to=0.05)


	def createPlot(self):
		self.loading2['text'] = " Loading..."
		self.loading2.update()
		try:
			self.slice = float(self.sliceValue.get())
			self.Dslice = float(self.deltaValue.get())
			self.Axis1 = float(self.sliceAxis1.get())
			self.Axis2 = float(self.sliceAxis2.get())

		except:
			pass
		plt.figure(1)
		plt.clf()

		self.nb = 0
		self.abss = []
		self.ordn = []
		color = []
		self.clusters=[]
		if (self.boxe_prise_2.get() == 'x'):
			a = 1
			o = 2
			r = 0
			plt.title('Plasma particles energy (J) Y and Z')
			plt.xlabel('Y (cm)')
			plt.ylabel('Z (cm)')

		elif (self.boxe_prise_2.get() == 'y'):
			a = 0
			o = 2
			r = 1
			plt.title('Plasma particles energy (J) X and Z')
			plt.xlabel('X (cm)')
			plt.ylabel('Z (cm)')
		elif (self.boxe_prise_2.get() == 'z'):
			a = 0
			o = 1
			r = 2
			plt.title('Plasma particles energy (J) X and Y')
			plt.xlabel('X (cm)')
			plt.ylabel('Y (cm)')
		else:
			plt.title('Plasma particles energy')

		if (self.boxe_prise_2.get() != ""):
			xmin = self.tabPart[a][0]
			xmax = self.tabPart[a][0]
			ymin = self.tabPart[o][0]
			ymax = self.tabPart[o][0]

			for i in range(0,int(self.parttab)):

				if xmin > self.tabPart[a][i]:
					xmin = self.tabPart[a][i]
				if xmax < self.tabPart[a][i]:
					xmax = self.tabPart[a][i]
				if ymin > self.tabPart[o][i]:
					ymin = self.tabPart[o][i]
				if ymax < self.tabPart[o][i]:
					ymax = self.tabPart[o][i]

				if ((self.energy[i] >= self.slice) and (self.energy[i] <= self.Dslice) and (self.tabPart[r][i]>=self.Axis1) and (self.tabPart[r][i]<=self.Axis2)):
					self.abss.append(self.tabPart[a][i])
					self.ordn.append(self.tabPart[o][i])
					color.append(self.energy[i])
					self.clusters+=[[self.tabPart[a][i],self.tabPart[o][i],self.tabPart[r][i]]]
					self.nb += 1

			plt.scatter(self.abss,self.ordn, c = color, s = 10, marker = 'o', cmap = 'jet',edgecolor = 'none')
			plt.xlim(xmin,xmax)
			plt.ylim(ymin,ymax)
			plt.colorbar()


		self.nb_label['text'] = self.language[25] + str(self.nb)
		self.graph.draw()
		self.nbrclusters['text'] = ""
		self.loading2['text'] = ""


	def plotPartButton(self,event):

		verif1 = False
		verif2 = False
		verif3 = False
		verif4 = False

		if (float(self.sliceAxis1.get())>float(self.sliceAxis2.get())):
			self.errorAxis['text'] = str(float(self.sliceAxis1.get())) + self.language[37]
			verif4 = False
		else:
			self.errorAxis['text'] = self.language[9]
			verif4 = True


		if not isFloat(self.sliceValue.get()):
			self.errorenergy['text'] = self.language[38]
			verif1 = False
		elif  float(self.sliceValue.get()) < 0 :
			self.errorenergy['text'] = self.language[39]
			verif1 = False
		else:
			verif1 = True
			self.errorenergy['text'] = self.language[9]


		if not isFloat(self.deltaValue.get()):
			self.errorDelta['text'] = self.language[38]
			verif2 = False
		elif float(self.deltaValue.get()) > 2:
			self.errorDelta['text'] = self.language[40]
			verif2 = False

		elif  float(self.deltaValue.get()) <  float(self.sliceValue.get()):
			self.errorDelta['text'] = str(self.sliceValue.get()) + self.language[41]
			verif2 = False

		else:
			verif2 = True
			self.errorDelta['text'] = self.language[9]

		if self.boxe_prise_2.get() == "" :
			self.errorRadio['text'] = self.language[42]
			verif3 = False
		else :
			verif3 = True
			self.errorRadio['text'] = self.language[9]

		if verif2 and verif3 and verif1 and verif4 and (float(self.deltaValue.get()) != self.Dslice or float(self.sliceValue.get()) != self.slice or self.boxe_prise_2.get() != self.actualSlice or float(self.sliceAxis1.get()) != self.Axis1 or float(self.sliceAxis2.get()) != self.Axis2):
			self.actualSlice = self.boxe_prise_2.get()
			self.createPlot()



	def loadtemplate(self):
		filename = askopenfilename(filetypes = (("NetCDF files", "*.nc"),("Data files", "*.dat"),("All files", "*.*")))
		if filename:
			try:
				self.entName['text'] = filename
			except:
				showerror("Open Source File", "Failed to read file \n'%s'"%filename)
				return



	def loadData(self):
		if os.path.exists(self.fileName):
			self.parttab, self.tabPart, self.energy , self.velocity , self.elec = readFilePart(self.fileName, int(self.num))
			self.slice = 0.0
			self.Dslice = 0.0
			self.actualSlice = ''
			self.slicevel = 0.0
			self.Dslicevel = 0.0
			self.actualSlicevel = ''
			self.max = max(self.energy)
			self.min = min(self.energy)
			self.maxvel = max(self.velocity)
			self.minvel = min(self.velocity)



	def changeDataFileButton(self,event):
		self.loading1['text'] = "Loading..."
		self.loading1.update()

		verif1 = False
		verif2 = False

		if not (os.path.exists(self.entName['text'])):
			self.errorName['text'] = self.language[34]
			verif1 = False
		else :
			self.errorName['text'] = self.language[9]
			verif2 = True

		if self.boxe_prise.get() != '1' and self.boxe_prise.get() != '2' and self.boxe_prise.get() != '3' and self.boxe_prise.get() != '4':
			self.errorNum['text'] = self.language[35]
			verif2 = False
		else :
			self.errorNum['text'] = self.language[9]
			verif1 = True


		if verif1 and verif2 and (self.num != int(self.boxe_prise.get()) or self.fileName != self.entName['text']):

			self.fileName = self.entName['text']
			self.fileNameLabel['text'] = self.fileName
			self.num = int(self.boxe_prise.get())
			self.part['text'] = self.language[36] + str(self.num)

			# Data

			start = time.time()
			self.loadData()

			print()
			print("Success")
			print("Time : ",time.time()-start,"s\n")

			self.nb_part_file = int(self.parttab)

			self.labelNumber['text'] = self.language[10] + str(self.nb_part_file)
			self.labelMin['text'] = self.language[11] + str(self.min) + self.language[37]
			self.labelMax['text'] = self.language[12] + str(self.max) + self.language[37]
			self.labelMinvel['text'] = self.language[11] + str(self.minvel) + " cm/s"
			self.labelMaxvel['text'] = self.language[12] + str(self.maxvel) + " cm/s"
			self.updateCanvas()
		self.loading1['text'] = ""
		self.loading1.update()



	def createPlotVel(self):
		self.loading2vel['text'] = " Loading..."
		self.loading2vel.update()
		try:
			self.slicevel = float(self.sliceValuevel.get())
			self.Dslicevel = float(self.deltaValuevel.get())
			self.Axis1vel = float(self.sliceAxis1vel.get())
			self.Axis2vel = float(self.sliceAxis2vel.get())

		except:
			pass
		plt.figure(3)
		plt.clf()

		self.nbvel = 0
		abss = []
		ordn = []
		color = []
		if (self.boxe_prise_2.get() == 'x'):
			a = 1
			o = 2
			r = 0
			plt.title('Plasma particles velocity (cm/s) Y and Z')
			plt.xlabel('Y (cm)')
			plt.ylabel('Z (cm)')

		elif (self.boxe_prise_2.get() == 'y'):
			a = 0
			o = 2
			r = 1
			plt.title('Plasma particles velocity (cm/s) X and Z')
			plt.xlabel('X (cm)')
			plt.ylabel('Z (cm)')
		elif (self.boxe_prise_2.get() == 'z'):
			a = 0
			o = 1
			r = 2
			plt.title('Plasma particles velocity (cm/s) X and Y')
			plt.xlabel('X (cm)')
			plt.ylabel('Y (cm)')
		else:
			plt.title('Plasma particles velocity')

		if (self.boxe_prise_2.get() != ""):
			xmin = self.tabPart[a][0]
			xmax = self.tabPart[a][0]
			ymin = self.tabPart[o][0]
			ymax = self.tabPart[o][0]

			for i in range(0,int(self.parttab)):

				if xmin > self.tabPart[a][i]:
					xmin = self.tabPart[a][i]
				if xmax < self.tabPart[a][i]:
					xmax = self.tabPart[a][i]
				if ymin > self.tabPart[o][i]:
					ymin = self.tabPart[o][i]
				if ymax < self.tabPart[o][i]:
					ymax = self.tabPart[o][i]

				if ((self.velocity[i] >= self.slicevel) and (self.velocity[i] <= self.Dslicevel) and (self.tabPart[r][i]>=self.Axis1vel) and (self.tabPart[r][i]<=self.Axis2vel)):
					abss.append(self.tabPart[a][i])
					ordn.append(self.tabPart[o][i])
					color.append(self.velocity[i])
					self.nbvel += 1

			plt.scatter(abss,ordn, c = color, s = 10, marker = 'o', cmap = 'jet',edgecolor = 'none')
			plt.xlim(xmin,xmax)
			plt.ylim(ymin,ymax)
			plt.colorbar()


		self.nb_labelvel['text'] = self.language[25] + str(self.nbvel)
		self.graphvel.draw()
		self.loading2vel['text'] = ""


	def plotElec(self):
		Elecwindow=Toplevel(self.can_plot)
		Elecwindow.title('Electric Field')
		fig5 = plt.figure(5)
		self.graphElec = FigureCanvasTkAgg(fig5, master = Elecwindow)
		self.graphElec.get_tk_widget().pack(side='left', expand=1, pady = 10)

		plt.clf()
		plt.title('Electric Field')
		plt.xlabel('Position X')
		plt.ylabel('Electric Field Ex')
		field=self.elec[0]
		abscissa = np.arange(int(100*self.x/1.255)-1, int(100*self.x/1.255)+2, 1)
		axis = [] + [field[i][int(100*self.y)][int(100*self.z)] for i in abscissa]
		plt.plot(abscissa, axis, markersize=0.2, color='red')
		self.graphElec.draw()


	def plotPartButtonVel(self,event):

		verif1 = False
		verif2 = False
		verif3 = False
		verif4 = False

		if (float(self.sliceAxis1vel.get())>float(self.sliceAxis2vel.get())):
			self.errorAxisvel['text'] = str(float(self.sliceAxis1vel.get())) + self.language[41]
			verif4 = False
		else:
			self.errorAxisvel['text'] = self.language[9]
			verif4 = True


		if not isFloat(self.sliceValuevel.get()):
			self.errorvelocity['text'] = self.language[38]
			verif1 = False
		elif  float(self.sliceValuevel.get()) < 0 :
			self.errorvelocity['text'] = self.language[39]
			verif1 = False
		else:
			verif1 = True
			self.errorvelocity['text'] = self.language[9]


		if not isFloat(self.deltaValuevel.get()):
			self.errorDeltavel['text'] = self.language[38]
			verif2 = False
		elif float(self.deltaValuevel.get()) > 2:
			self.errorDeltavel['text'] = self.language[40]
			verif2 = False

		elif  float(self.deltaValuevel.get()) <  float(self.sliceValuevel.get()):
			self.errorDeltavel['text'] = str(self.sliceValuevel.get()) + self.language[37]
			verif2 = False

		else:
			verif2 = True
			self.errorDeltavel['text'] = self.language[9]

		if self.boxe_prise_2.get() == "" :
			self.errorRadiovel['text'] = self.language[42]
			verif3 = False
		else :
			verif3 = True
			self.errorRadiovel['text'] = self.language[9]

		if verif2 and verif3 and verif1 and verif4 and (float(self.deltaValuevel.get()) != self.Dslicevel or float(self.sliceValuevel.get()) != self.slicevel or self.boxe_prise_2.get() != self.actualSlicevel or float(self.sliceAxis1vel.get()) != self.Axis1vel or float(self.sliceAxis2vel.get()) != self.Axis2vel):
			self.actualSlicevel = self.boxe_prise_2.get()
			self.createPlotVel()	




	def savePlt(self):
		plt.figure(1)
		plt.savefig(self.saveName1.get())


	def savePlt2(self):
		plt.figure(2)
		plt.savefig(self.saveName2.get())


	def savePlt3(self):
		plt.figure(3)
		plt.savefig(self.saveName3.get())


	def savePlt4(self):
		plt.figure(4)
		plt.savefig(self.saveName4.get())


	def slideValue(self, val):
		plt.figure(2)
		plt.clf()
		cm = plt.cm.get_cmap('jet')
		self.n, self.bins, patches = plt.hist(self.energy, int(val))
		bin_centers = 0.5 * (self.bins[:-1] + self.bins[1:])
		col = bin_centers - min(bin_centers)
		if max(col) != 0:
			col /= max(col)
		for c, p in zip(col, patches):
		    plt.setp(p, 'facecolor', cm(c))
		plt.title('Plasma electron energy')
		plt.xlabel('energy (J)')
		plt.ylabel('Number of particles')
		self.canvas.draw()
		self.scalevalue = val


	def slideValueVel(self, val):
		plt.figure(4)
		plt.clf()
		cm = plt.cm.get_cmap('jet')
		self.nvel, self.binsvel, patches = plt.hist(self.velocity, int(val))
		bin_centers = 0.5 * (self.binsvel[:-1] + self.binsvel[1:])
		col = bin_centers - min(bin_centers)
		if max(col) != 0:
			col /= max(col)
		for c, p in zip(col, patches):
		    plt.setp(p, 'facecolor', cm(c))
		plt.title('Plasma electron velocity')
		plt.xlabel('velocity (cm/s)')
		plt.ylabel('Number of particles')
		self.canvasvel.draw()
		self.scalevaluevel = val



	def changeDataFile(self):
		self.root.unbind('<Return>')
		self.menu['width'] = 1000

		self.can_home.grid_remove()
		self.can_plot.grid_remove()
		self.can_histo.grid_remove()
		self.can_histovel.grid_remove()
		self.can_plotvel.grid_remove()

		
		self.can_data.grid(row=3,column=1,padx=1, pady=1,sticky=W)



	def plotPart(self, event):
		if os.path.exists(self.fileName):
			self.root.unbind('<Return>')
			self.menu['width'] = 1500
			self.can_plot.grid(row=3,column=1,padx=1, pady=1)

			self.can_home.grid_remove()
			self.can_histo.grid_remove()
			self.can_histovel.grid_remove()
			self.can_data.grid_remove()
			self.can_plotvel.grid_remove()
			


	def histo(self):
		if os.path.exists(self.fileName):
			self.root.unbind('<Return>')
			self.menu['width'] = 1500

			self.can_histo.grid(row=3,column=1,padx=1, pady=1)

			self.can_histovel.grid_remove()
			self.can_home.grid_remove()
			self.can_plot.grid_remove()
			self.can_data.grid_remove()
			self.can_plotvel.grid_remove()

	def plotPartVel(self, event):
		if os.path.exists(self.fileName):
			self.root.unbind('<Return>')
			self.menu['width'] = 1500
			self.can_plotvel.grid(row=3,column=1,padx=1, pady=1)

			self.can_plot.grid_remove()
			self.can_home.grid_remove()
			self.can_histo.grid_remove()
			self.can_histovel.grid_remove()
			self.can_data.grid_remove()

	def histovel(self):
		if os.path.exists(self.fileName):
			self.root.unbind('<Return>')
			self.menu['width'] = 1500

			self.can_histovel.grid(row=3,column=1,padx=1, pady=1)

			self.can_histo.grid_remove()
			self.can_home.grid_remove()
			self.can_plot.grid_remove()
			self.can_data.grid_remove()
			self.can_plotvel.grid_remove()



	def returnHome(self):
		self.root.unbind('<Return>')
		self.menu['width'] = 1000

		self.can_home.grid(row=3,column=1,padx=1, pady=1)
		self.can_home.grid_propagate(0)

		self.can_plot.grid_remove()
		self.can_histo.grid_remove()
		self.can_histovel.grid_remove()
		self.can_data.grid_remove()
		self.can_plotvel.grid_remove()






def main():
	inter = InterfaceGraphe()
	inter.root.mainloop()
	print("Goodbye")

if __name__  == '__main__':
	main()

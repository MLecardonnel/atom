import struct
import numpy as np
import matplotlib.pyplot as plt
import time
import math
from netCDF4 import Dataset
import numpy.ma as ma



def readFilePartNC(nameFile, n):
	start = time.time()

	print("File : \"",nameFile,"\"")
	print("Reading ...\n")

	try:
		mumu=Dataset(nameFile,"r",format="NETCDF4")
		if (n == 1) :
			print("First Sort of Particules")
			part = mumu.variables["Coordinates_x0"].size
			print("Size : ",part)
			tabPart = np.zeros((3,part),dtype = 'd')
			tabPart[0] = ma.getdata(mumu.variables["Coordinates_x0"][:])
			tabPart[1] = ma.getdata(mumu.variables["Coordinates_y0"][:])
			tabPart[2] = ma.getdata(mumu.variables["Coordinates_z0"][:])
			energy = np.ones(part,dtype = 'd')
			Imp_x=abs(ma.getdata(mumu.variables["Impulses_x0"][:]))
			Imp_y=abs(ma.getdata(mumu.variables["Impulses_y0"][:]))
			Imp_z=abs(ma.getdata(mumu.variables["Impulses_z0"][:]))
			for i in range(0,part):
				energy[i]=1+Imp_x[i]**2+Imp_y[i]**2+Imp_z[i]**2

		elif (n == 2) :
			print("Second Sort of Particules") 
			part = mumu.variables["Coordinates_x1"].size
			print("Size : ",part)
			tabPart = np.zeros((3,part),dtype = 'd')
			tabPart[0] = ma.getdata(mumu.variables["Coordinates_x1"][:])
			tabPart[1] = ma.getdata(mumu.variables["Coordinates_y1"][:])
			tabPart[2] = ma.getdata(mumu.variables["Coordinates_z1"][:])
			energy = np.ones(part,dtype = 'd')
			Imp_x=abs(ma.getdata(mumu.variables["Impulses_x1"][:]))
			Imp_y=abs(ma.getdata(mumu.variables["Impulses_y1"][:]))
			Imp_z=abs(ma.getdata(mumu.variables["Impulses_z1"][:]))
			for i in range(0,part):
				energy[i]=1+Imp_x[i]**2+Imp_y[i]**2+Imp_z[i]**2

		elif (n == 3) :
			print("Third Sort of Particules")
			part = mumu.variables["Coordinates_x2"].size
			print("Size : ",part)
			tabPart = np.zeros((3,part),dtype = 'd')
			tabPart[0] = ma.getdata(mumu.variables["Coordinates_x2"][:])
			tabPart[1] = ma.getdata(mumu.variables["Coordinates_y2"][:])
			tabPart[2] = ma.getdata(mumu.variables["Coordinates_z2"][:])
			energy = np.ones(part,dtype = 'd')
			Imp_x=abs(ma.getdata(mumu.variables["Impulses_x2"][:]))
			Imp_y=abs(ma.getdata(mumu.variables["Impulses_y2"][:]))
			Imp_z=abs(ma.getdata(mumu.variables["Impulses_z2"][:]))
			for i in range(0,part):
				energy[i]=1+Imp_x[i]**2+Imp_y[i]**2+Imp_z[i]**2

		elif (n == 4) :
			print("All Sorts of Particules")
			part1 = mumu.variables["Coordinates_x0"].size
			tabPart1 = np.zeros((3,part1),dtype = 'd')
			tabPart1[0] = ma.getdata(mumu.variables["Coordinates_x0"][:])
			tabPart1[1] = ma.getdata(mumu.variables["Coordinates_y0"][:])
			tabPart1[2] = ma.getdata(mumu.variables["Coordinates_z0"][:])
			energy1 = np.ones(part1,dtype = 'd')
			Imp_x1=abs(ma.getdata(mumu.variables["Impulses_x0"][:]))
			Imp_y1=abs(ma.getdata(mumu.variables["Impulses_y0"][:]))
			Imp_z1=abs(ma.getdata(mumu.variables["Impulses_z0"][:]))
			for i in range(0,part1):
				energy1[i]=1+Imp_x1[i]**2+Imp_y1[i]**2+Imp_z1[i]**2
			part2 = mumu.variables["Coordinates_x1"].size
			tabPart2 = np.zeros((3,part2),dtype = 'd')
			tabPart2[0] = ma.getdata(mumu.variables["Coordinates_x1"][:])
			tabPart2[1] = ma.getdata(mumu.variables["Coordinates_y1"][:])
			tabPart2[2] = ma.getdata(mumu.variables["Coordinates_z1"][:])
			energy2 = np.ones(part2,dtype = 'd')
			Imp_x2=abs(ma.getdata(mumu.variables["Impulses_x1"][:]))
			Imp_y2=abs(ma.getdata(mumu.variables["Impulses_y1"][:]))
			Imp_z2=abs(ma.getdata(mumu.variables["Impulses_z1"][:]))
			for i in range(0,part2):
				energy2[i]=1+Imp_x2[i]**2+Imp_y2[i]**2+Imp_z2[i]**2
			part3 = mumu.variables["Coordinates_x2"].size
			tabPart3 = np.zeros((3,part3),dtype = 'd')
			tabPart3[0] = ma.getdata(mumu.variables["Coordinates_x2"][:])
			tabPart3[1] = ma.getdata(mumu.variables["Coordinates_y2"][:])
			tabPart3[2] = ma.getdata(mumu.variables["Coordinates_z2"][:])
			energy3 = np.ones(part3,dtype = 'd')
			Imp_x3=abs(ma.getdata(mumu.variables["Impulses_x2"][:]))
			Imp_y3=abs(ma.getdata(mumu.variables["Impulses_y2"][:]))
			Imp_z3=abs(ma.getdata(mumu.variables["Impulses_z2"][:]))
			for i in range(0,part3):
				energy3[i]=1+Imp_x3[i]**2+Imp_y3[i]**2+Imp_z3[i]**2
			part=part1+part2+part3
			print("Size : ",part)
			tabPart = np.concatenate((np.concatenate((tabPart1,tabPart2),axis=1),tabPart3),axis=1)
			energy = np.concatenate((np.concatenate((energy1,energy2),axis=0),energy3),axis=0)


	
	except IOError:
		print("Error")

	finally:
		mumu.close()
		print("OK")
	
		return (part,tabPart,energy)

def createFormatInt8(size):
	form = "<l"
	for h in range(0,size):
		form += "d"
	form += "l"
	return form

def readFilePartDat(nameFile, n):
	start = time.time()


	print("File : \"",nameFile,"\"")
	print("Reading ...\n")

	try:
		if (n == 4) :
			print("All Sorts of Particules")
			f = open(nameFile, "rb")
			tab = np.zeros((12,102,6,6),dtype='d')
			form = createFormatInt8(3672)
	
			for x in range(0,12):
				r = f.read(29384)
				v = struct.unpack(form, r)
				tmp = 1
				for i in range(0,102):
					for j in range(0,6):
						for k in range(0,6):
							tab[x][i][j][k] = v[tmp]
							tmp+=1

			r = f.read(32)
			part1 = struct.unpack("<ldddl",r)
			size1 = int(part1[1])
			form1 = createFormatInt8(size1)

			tabPart1 = np.zeros((3,size1),dtype = 'd')
			energy1 = np.ones(size1,dtype = 'd')
	
			for x in range(0,6):
				r = f.read(size1*8+8)
				struct1 = struct.unpack(form1, r)
				tmp = 1
				if x == 0 or x == 1 or x == 2:
					for i in range(0,size1):
						tabPart1[x][i] = struct1[tmp]
						tmp+=1
				elif x == 3 or x == 4:
					for i in range(0,size1):
						energy1[i]+=struct1[tmp]**2
						tmp+=1
				else:
					for i in range(0,size1):
						energy1[i]+=struct1[tmp]**2
						tmp+=1


			r = f.read(32)
			part2 = struct.unpack("<ldddl",r)
			size2 = int(part2[1])
			form2 = createFormatInt8(size2)
	
			tabPart2 = np.zeros((3,size2),dtype = 'd')
			energy2 = np.ones(size2,dtype = 'd')
	
			for x in range(0,6):
				r = f.read(size2*8+8)
				struct2 = struct.unpack(form2, r)
				tmp = 1
				if x == 0 or x == 1 or x == 2:
					for i in range(0,size2):
						tabPart2[x][i] = struct2[tmp]
						tmp+=1
				elif x == 3 or x == 4:
					for i in range(0,size2):
						energy2[i]+=struct2[tmp]**2
						tmp+=1
				else:
					for i in range(0,size2):
						energy2[i]+=struct2[tmp]**2
						tmp+=1

			r = f.read(32)
			part3 = struct.unpack("<ldddl",r)
			size3 = int(part3[1])
			form3 = createFormatInt8(size3)
	
			tabPart3 = np.zeros((3,size3),dtype = 'd')
			energy3 = np.ones(size3,dtype = 'd')
	
			for x in range(0,6):
				r = f.read(size3*8+8)
				struct3 = struct.unpack(form3, r)
				tmp = 1
				if x == 0 or x == 1 or x == 2:
					for i in range(0,size3):
						tabPart3[x][i] = struct3[tmp]
						tmp+=1
				elif x == 3 or x == 4:
					for i in range(0,size3):
						energy3[i]+=struct3[tmp]**2
						tmp+=1
				else:
					for i in range(0,size3):
						energy3[i]+=struct3[tmp]**2
						tmp+=1

			size = size1+size2+size3
			print("Size : ",size)
			tabPart = np.concatenate((np.concatenate((tabPart1,tabPart2),axis=1),tabPart3),axis=1)
			energy = np.concatenate((np.concatenate((energy1,energy2),axis=0),energy3),axis=0)
			
		else :
			f = open(nameFile, "rb")
			tab = np.zeros((12,102,6,6),dtype='d')
			form = createFormatInt8(3672)
	
			for x in range(0,12):
				r = f.read(29384)
				v = struct.unpack(form, r)
				tmp = 1
				for i in range(0,102):
					for j in range(0,6):
						for k in range(0,6):
							tab[x][i][j][k] = v[tmp]
							tmp+=1
			if (n > 1):
				r = f.read(32)
				part1 = struct.unpack("<ldddl",r)
				size = int(part1[1])
				form = createFormatInt8(size)
	
				for x in range(0,6):
					r = f.read(size*8+8)

				if (n > 2):
					r = f.read(32)
					part2 = struct.unpack("<ldddl",r)
					size = int(part2[1])
					form = createFormatInt8(size)
	
					for x in range(0,6):
							r = f.read(size*8+8)
	
			print()
			if (n == 1):
				print("First Sort of Particules")
			elif (n == 2):
				print("Second Sort of Particules") 
			elif (n == 3):
				print("Third Sort of Particules")
			else:
				print("Error number of Particules")
	
			r = f.read(32)
			part = struct.unpack("<ldddl",r)
	
			size = int(part[1])
			print("Size : ",size)
	
			tabPart = np.zeros((3,size),dtype = 'd')
			energy = np.ones(size,dtype = 'd')
			form = createFormatInt8(size)
	
			for x in range(0,6):
				r = f.read(size*8+8)
				struct3 = struct.unpack(form, r)
				tmp = 1
				if x == 0 or x == 1 or x == 2:
					for i in range(0,size):
						tabPart[x][i] = struct3[tmp]
						tmp+=1
				elif x == 3 or x == 4:
					for i in range(0,size):
						energy[i]+=struct3[tmp]**2
						tmp+=1
				else:
					for i in range(0,size):
						energy[i]+=struct3[tmp]**2
						tmp+=1
	
	except IOError:
		print("Error")

	finally:
		f.close()
		print("OK")
	
		return (size,tabPart, energy)

def readFilePart(nameFile, n):
	if (nameFile.split(".")[1]=="nc"):
		[part,tabPart,energy]=readFilePartNC(nameFile, n)
	elif (nameFile.split(".")[1]=="dat"):
		[part,tabPart,energy]=readFilePartDat(nameFile, n)
	return (part,tabPart,energy)



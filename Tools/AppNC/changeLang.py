
def changeLang(n):

	if n == 0:
		src = 'l-english'
	elif n == 1:
		src = 'l-french'
	elif n == 2:
		src = 'l-russian'
	else:
		pass


	try:
		f = open(src, "r")
		liste = []
		for line in f:
			c = line.rstrip('\n\r')
			liste.append(c)

	except IOError:
		print("Error")

	finally:
		f.close()
		print(src.rstrip('l-'))
		return (liste)

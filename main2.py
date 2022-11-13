import PyPDF2
from difflib import SequenceMatcher

#####################################
################ PDF1 ###############

pdf1 = open("contoh.pdf", "rb")
reader1 = PyPDF2.PdfFileReader(pdf1)
teks1=""
p=0
while 1:
	try:
		page = reader1.getPage(p)
		teks1+=page.extractText()	
		p+=1
	except:
		break

#####################################
################ PDF2 ###############

pdf2 = open("contoh.pdf", "rb")
reader2 = PyPDF2.PdfFileReader(pdf2)
teks2=""
p=0
while 1:
	try:
		page = reader2.getPage(p)
		teks2+=page.extractText()	
		p+=1
	except:
		break

#####################################
############## PROCESS ##############

sequenceScore = SequenceMatcher(None, teks1, teks2).ratio()
print("Keduanya Mirip Sekitar",sequenceScore * 100," % similar antara", pdf1, " dan ",pdf2)
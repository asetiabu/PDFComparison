print ("Hello World") #test

# PDF Comparison
import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


filename = 'C:\\users\\amadea.setiabudhi\\Desktop\\2019\\Overview of Audit US.pdf'

pdfFileObj = open(filename, 'rb')
#open allows you to read the file

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#the pdfreader variable is a readable object that will be parsed

num_pages = pdfReader.numPages
count = 0
text = ""
#distinguishing the number of pages will allow us to parse through
#all the pages


pageObj = pdfReader.getPage(count)
text = pageObj.extractText()
print(text)

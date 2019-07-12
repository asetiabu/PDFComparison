
# PDF Comparison
import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

filename = 'Enter File Path Here'

pdfFileObj = open(filename, 'rb')
#open allows you to read the file

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#Here I am creating the pdfreader object. The pdfreader variable is a readable object that will be parsed

num_pages = pdfReader.numPages
count = 0
text = ""
#Over here, I am getting all the pages

pageObj = pdfReader.getPage(count)
text = pageObj.extractText()
print(text)

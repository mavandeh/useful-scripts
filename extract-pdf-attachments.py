'''
Code modified from https://gist.github.com/kevinl95/29a9e18d474eb6e23372074deff2df38#file-extract_pdf_attachments-py

TODO:   tkinter filedialog.askdirectory()
        os.walk() to find pdf files
'''

import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def getAttachments(reader):
      """
      Retrieves the file attachments of the PDF as a dictionary of file names
      and the file data as a bytestring.
      :return: dictionary of filenames and bytestrings
      """
      catalog = reader.trailer["/Root"]
      fileNames = catalog['/Names']['/EmbeddedFiles']['/Kids'][0]['/Names']
      attachments = {}
      for f in fileNames:
          if isinstance(f, str):
              name = f
              dataIndex = fileNames.index(f) + 1
              fDict = fileNames[dataIndex].getObject()
              fData = fDict['/EF']['/F'].getData()
              attachments[name] = fData

      return attachments

# TODO:     tkinter filedialog.askdirectory(), 
#           os.walk() to find .pdf files, 
#           iterate to get attachments from each
handler = open(askopenfilename(), 'rb')
reader = PyPDF2.PdfFileReader(handler)
'''
# this was debugging code to find the location of the embedded file.
for i in reader.trailer['/Root']['/Names']['/EmbeddedFiles']['/Kids'][0]['/Limits']:
	print(i)
'''
dictionary = getAttachments(reader)
#print(dictionary)
for fName, fData in dictionary.items():
    with open(fName, 'wb') as outfile:
        outfile.write(fData)

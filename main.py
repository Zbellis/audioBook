# Credit to Programming Hero https://www.youtube.com/watch?v=kyZ_5cvrXJI&t=305s

# import Python: Text to Speech v3 and Python PDF.
import pyttsx3
import PyPDF2

# directory to the PDF you want to read, in binary format
book = open('theblissjourney.pdf', 'rb')


# Using PyPDF2 to read from a book
pdfReader = PyPDF2.PdfFileReader(book)


pages = pdfReader.numPages
speaker = pyttsx3.init()

# loop through start page to end
for num in range(15, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

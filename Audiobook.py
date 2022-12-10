import PyPDF2
import pyttsx3
from pyttsx3 import engine

speaker = pyttsx3.init()
pdfReader = PyPDF2.PdfFileReader(open('Angular2NotesForProfessionals.pdf', 'rb'))
for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

# Saving the audio file
engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()

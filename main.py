import pyttsx3
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('file.pdf', 'rb'))

#Intialize the speaker
speaker = pyttsx3.init()
text="Hey, Welcome to The Classes"
speaker.say(text)

# For changing rate
# rate=speaker.getProperty('rate')
# print(rate)
# speaker.setProperty('rate',400)

#For changing voice
# voices=speaker.getProperty('voices')
# print(voices[1])
# speaker.setProperty('voice',voices[1].id)

#For changing volume
# volume = speaker.getProperty('volume')
# print(volume)
# speaker.setProperty('volume',0.8)

#Save voice to audio file
# speaker.save_to_file(text, 'audio.mp3')

speaker.runAndWait()

# For reading whole pdf
for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

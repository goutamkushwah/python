import PyPDF2
import pyttsx3

def pdf_to_speech(pdf_path):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    
    # Open the PDF file
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        
        # Extract text from each page
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text() + "\n"

    # Convert text to speech
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        print("No text found in the PDF!")

# Example usage
pdf_to_speech("LAN Unit3.pdf")

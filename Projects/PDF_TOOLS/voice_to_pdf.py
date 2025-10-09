import speech_recognition as sr
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now, I'm listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)  # Capture audio

    try:
        text = recognizer.recognize_google(audio)  # Convert speech to text
        print("Recognized text:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
    
    return ""

def save_to_pdf(text, filename="output.pdf"):
    if text:
        pdf = canvas.Canvas(filename, pagesize=letter)
        pdf.setFont("Helvetica", 12)
        
        lines = text.split()  # Split text into words
        max_words_per_line = 10  # Adjust for better readability
        y_position = 750  # Start writing from this height
        
        line = ""
        for word in lines:
            if len(line.split()) < max_words_per_line:
                line += word + " "
            else:
                pdf.drawString(100, y_position, line)
                y_position -= 20  # Move to the next line
                line = word + " "

        # Print the last line
        pdf.drawString(100, y_position, line)
        pdf.save()
        print(f"PDF saved as {filename}")
    else:
        print("No text to save!")

if __name__ == "__main__":
    text = record_audio()
    save_to_pdf(text)
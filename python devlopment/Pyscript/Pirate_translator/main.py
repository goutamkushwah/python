from pyscript import document

# Pirate dictionary
pirate_words = {
    "hello": "ahoy",
    "hi": "yo-ho-ho",
    "my": "me",
    "friend": "matey",
    "is": "be",
    "are": "be",
    "you": "ye",
    "money": "booty",
    "stop": "avast",
    "yes": "aye",
    "no": "nay"
}

# Translate function
def translate(event):

    text = document.getElementById("inputText").value

    words = text.lower().split()

    translated = []

    for word in words:

        if word in pirate_words:
            translated.append(pirate_words[word])
        else:
            translated.append(word)

    final_text = " ".join(translated)

    document.getElementById("output").innerText = final_text

# Connect button
document.getElementById("translateBtn").onclick = translate
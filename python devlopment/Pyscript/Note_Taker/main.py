from pyscript import document
from js import document as js_document

# Save note
def save_note(event):

    title_input = document.getElementById(
        "titleInput"
    )

    note_input = document.getElementById(
        "noteInput"
    )

    title = title_input.value.strip()
    note = note_input.value.strip()

    # Ignore empty notes
    if title == "" or note == "":
        return

    # Create note card
    note_div = js_document.createElement("div")

    note_div.className = "note"

    note_div.innerHTML = f"""
        <h2>{title}</h2>
        <p>{note}</p>

        <button class="delete-btn">
            Delete
        </button>
    """

    # Delete button
    delete_btn = note_div.querySelector(
        ".delete-btn"
    )

    def delete_note(event):
        note_div.remove()

    delete_btn.onclick = delete_note

    # Add note
    document.getElementById(
        "notesContainer"
    ).appendChild(note_div)

    # Clear fields
    title_input.value = ""
    note_input.value = ""

# Connect button
document.getElementById(
    "saveBtn"
).onclick = save_note
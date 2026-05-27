from pyscript import document
from js import document as js_document

# Add task
def add_task(event):

    task_input = document.getElementById("taskInput")

    task_text = task_input.value.strip()

    if task_text == "":
        return

    # Create list item
    li = js_document.createElement("li")

    li.innerHTML = f"""
        {task_text}
        <button class="delete-btn">Delete</button>
    """

    # Delete button
    delete_btn = li.querySelector(".delete-btn")

    def delete_task(event):
        li.remove()

    delete_btn.onclick = delete_task

    # Add task to list
    document.getElementById("taskList").appendChild(li)

    # Clear input
    task_input.value = ""

# Connect button
document.getElementById("addBtn").onclick = add_task
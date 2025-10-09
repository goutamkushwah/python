# Date 07-10-2025
# Create two virtual environments, install few packages in the first one. How do you 
# create a similar environment in the second one?


#  Step 1: Create the first virtual environment
# python -m venv env1


# Activate it:

# .\env1\Scripts\activate

# Step 2: Install some packages in env1

# For example:

# pip install flask pyjokes requests

# Step 3: Export the package list to a file

# This creates a record of all installed packages and versions:

# pip freeze > requirements.txt


# Now you’ll have a file called requirements.txt like:

# Flask==3.0.3
# pyjokes==0.6.0
# requests==2.32.3

# Step 4: Create the second environment

# Deactivate the first one:

# deactivate


# Then create and activate a new one:

# python -m venv env2
# .\env2\Scripts\activate

# Step 5: Install the same packages in env2

# Now use the requirements.txt file you made earlier:

# pip install -r requirements.txt


# This automatically installs the exact same packages and versions as in the first environment.

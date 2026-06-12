# create 
python -m venv venv

# Activate
venv\Scripts\activate

# Install packages
pip install pandas

# Check installation
python -c "import pandas as pd; print(pd.__version__)"

# Save dependencies
pip freeze > requirements.txt

# Exit environment
deactivate
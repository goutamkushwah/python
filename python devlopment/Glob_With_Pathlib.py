from pathlib import Path 

# Using Path.glob()
data_dir = Path('data')
csv_files = data_dir.glob('*.csv')
for file in csv_files: 
    print(file) # Returns Path objects, not strings 

# Recursive search with Path.rglob()
all_python = Path('.').rglob('*.py')
for file in all_python: 
    print(file.absolute())
# give the output in folder structure way
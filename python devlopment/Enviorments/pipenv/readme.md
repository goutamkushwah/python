## Install pipenv
```
pip install pipenv
```
## Activate
```
 python -m pipenv shell
```
## Check version of Python
```
python --version
```
## Check path
```
python
>>> import sys
>>> sys.executable
exit()
```
## Install a package
```
pipenv install camelcase
```
## Check local packages
```
pipenv lock -r
```
## Uninstall a package
```
pipenv uninstall camelcase
```
## Install a dev package
```
pipenv install nose --dev
```
##  to make requiremts.txt
pipenv requirements --dev > requirements.txt
## Install from requirements.txt
```
pipenv install -r ./requirements.txt
```
## Check security vulnerabilities
```
pipenv check
```
## Check dependency graph
```
pipenv graph
```
## Ignore pipfile
```
pipenv install --ignore-pipfile
```
## Set lockfile - before deployment
```
pipenv lock
```
## Exiting the virtualenv
```
exit
```
## Run with pipenv
```
pipenv run *
```
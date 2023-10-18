# Empathy Talent Challenge

This repository code is part of the Homework Challenge of Empathy Talent selection process.

## Tech Stack

**Language:** [Python](https://www.python.org/)

**Test Framework:** 
* [Selenium](https://www.selenium.dev/)
* [Behave](https://behave.readthedocs.io/en/latest/)
* [Pytest](https://docs.pytest.org/)

**Most Relevant Libraries/Modules**: 
* [Python's virtualenv](https://docs.python.org/3.11/library/venv.html)
* [Requests](https://requests.readthedocs.io/en/latest/)
* [Webdriver-manager](https://pypi.org/project/webdriver-manager/)

**Website being tested:** https://www.saucedemo.com/

**APIs being tested:** 
* https://rapidapi.com/weatherapi/api/weatherapi-com/
* https://rapidapi.com/googlecloud/api/google-translate1

All used libraries and their version can be checked on the `requirements.txt` file.

## Installation
To properly run the test code, some programs needs to be installed.

* GitHub (See how to, depending on your OS [here](https://github.com/git-guides/install-git))
* Python version 3.11.6, [here](https://www.python.org/downloads/)
* Chrome browser, [here](https://www.google.com/intl/en_us/chrome/)

## Setting up local environment

Clone the project

```bash
git clone https://github.com/gbl3/qa-challenge-et.git
```

Go to the project directory

```bash
cd qa-challenge-et
```
**To install the requirements, you have two options:**

First (recommended) is to create a virtualenv

```bash
python -m venv .
```

Activate the virtualenv (**Note: this runs different depending on your OS**)

For **Windows PowerShell**:
```bash
venv\Scripts\Activate.ps1  
```

For **Windows cmd**:
```bash
venv\Scripts\activate.bat
```

For **Linux/MacOs**:
```bash
source venv/Scripts/activate
```
Install the requirements
```bash
pip install -r requirements.txt 
```

Second option would be to directly run the previous command. The problem with that is that you are going to install
the requirements globally on your computer, which might break something for your other projects. That's why I recommend
going with the virtualenv option.

----
## Running tests

Before going forward, make sure you have the requirements installed and virtualenv activated.
To run the **frontend** tests, simply type on the project root:
```bash
behave
```
For the **api** tests, you have to move to the `api` folder:
```bash
cd api
```
Once you are already on the `api` folder run the following:
```bash
pytest .\test-google-translate-api.py .\test-weather-api.py
```
If an error occurs, please try the setup part again. To deactivate the virtual environment, simply type:   
```bash
deactivate
```
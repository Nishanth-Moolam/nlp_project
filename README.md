# Natural Language Processing Project!

Welcome to my NLP Project! This project is a student study tool where Natural Language Processing 
is used to save key entites, lemmas, and other insights from each note uploaded, which can then be
searched for. This makes it easier to find notes where a specific topic is discussed, or a 
specific person or place is mentioned.

## Running server

create a virtual environment and activate it: 

```
virtualenv env
source env/bin/activate
```

then, in the project folder, install requirements. Please refer to 
https://textract.readthedocs.io/en/latest/installation.html for instructions
on how to install textract on your OS. The following is for OSX. Ensure you
have brew and cask installed:

```
cd server
brew install --cask xquartz
brew install poppler antiword unrtf tesseract swig
pip install -r requirements_pip.txt
```

You must also create your own secrets file:

```
touch secrets.py
```

and add your secrets. Visit https://developer.expert.ai/ui and create an account
to be able to use your credentials in secrets file:

```python
secret_key = ''
expertai_username = ''
expertai_password = ''
```

and finally run on localhost (port 5000):

```
python app.py
```


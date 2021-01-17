# Natural Language Processing Project!

## Running server

create a virtual environment and activate it:

```
virtualenv env
source env/bin/activate
```

then, in the project folder, install requirements:

```
cd server
pip install -r requirements.txt
```

You must also create your own secrets file:

```
touch secrets.py
```

```python
secret_key = ''
rapidapi_key = ''
```

and finally run on localhost:

```
python app.py
```

## Important!

This application uses the following external api's: (you must use your api keys in the secrets.py file you create!)

- Microsoft Computer Vision API
- expert.ai Natural Language API

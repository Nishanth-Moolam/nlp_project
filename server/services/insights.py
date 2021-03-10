from models.entity import Entity, db
from models.lemma import Lemma
from models.phrase import Phrase
from models.topic import Topic

def process_insights(notes_filename, note_id):
    from services.note import read_and_interpret_note
    from services.utils import find_picture_url

    picture_url = find_picture_url(note_id)
    insights_dict = read_and_interpret_note(picture_url)
    upload_insights(insights_dict, note_id)

# handles entities, lemmas, phrases, topics
def upload_insights(insights_dict, note_id):
    '''
    the input of this is a dictionary with insights
    This calls the other functions to upload insights to 
    their respective tables
    '''
    entities = insights_dict['entities']
    lemmas = insights_dict['lemmas']
    phrases = insights_dict['phrases']
    topics = insights_dict['topics']

    for entity in entities:
        CreateEntity(entity, note_id)

    for lemma in lemmas:
        CreateLemma(lemma, note_id)

    for phrase in phrases:
        CreatePhrase(phrase, note_id)

    for topic in topics:
        CreateTopic(topic, note_id)

def delete_insights(note_id):
    '''
    this should gather all insights from a note and delete them.
    '''
    pass


def CreateEntity(value, note_id):
    new_entity = Entity(
        value = value,
        note_id = note_id
    )
    db.session.add(new_entity)
    db.session.commit()

def UpdateEntity(id):
    pass

def DeleteEntity(id):
    pass

def CreateLemma(value, note_id):
    new_lemma = Lemma(
        value = value,
        note_id = note_id
    )
    db.session.add(new_lemma)
    db.session.commit()

def UpdateLemma(id):
    pass

def DeleteLemma(id):
    pass

def CreatePhrase(value, note_id):
    new_phrase = Phrase(
        value = value,
        note_id = note_id
    )
    db.session.add(new_phrase)
    db.session.commit()

def UpdatePhrase(id):
    pass

def DeletePhrase(id):
    pass

def CreateTopic(value, note_id):
    new_topic = Topic(
        value = value,
        note_id = note_id
    )
    db.session.add(new_topic)
    db.session.commit()

def UpdateTopic(id):
    pass

def DeleteTopic(id):
    pass
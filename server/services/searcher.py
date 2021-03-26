from models.note import Note
from models.topic import Topic
from models.phrase import Phrase
from models.lemma import Lemma
from models.entity import Entity


def search_note(text):
    results = []
    results_raw = Note.query.msearch(text, fields = ['notes_filename']).all()
    for result in results_raw:
        results.append({
            'value': result.notes_filename,
            'note_id': result.id
        })

    return results

def search_section(text):
    pass

def search_topic(text):
    results = []
    results_raw = Topic.query.msearch(text, fields = ['value']).all()
    for result in results_raw:
        results.append({
            'value': result.value,
            'note_id': result.note_id
        })

    return results

def search_phrase(text):
    results = []
    results_raw = Phrase.query.msearch(text, fields = ['value']).all()
    for result in results_raw:
        results.append({
            'value': result.value,
            'note_id': result.note_id
        })

    return results

def search_lemma(text):
    results = []
    results_raw = Lemma.query.msearch(text, fields = ['value']).all()
    for result in results_raw:
        results.append({
            'value': result.value,
            'note_id': result.note_id
        })

    return results

def search_entity(text):
    results = []
    results_raw = Entity.query.msearch(text, fields = ['value']).all()
    for result in results_raw:
        results.append({
            'value': result.value,
            'note_id': result.note_id
        })

    return results

def search_insights(text):    
    entity_results = search_entity(text)
    lemma_results = search_lemma(text)
    phrase_results = search_phrase(text)
    topic_results = search_topic(text)

    results = [
        {
            'entity': entity_results,
            'lemma': lemma_results,
            'phrase': phrase_results,
            'topic': topic_results
        }
    ]

    return results
from models.section import Section, db
from datetime import datetime


def CreateSection(section_name):

    date_added = datetime.now()

    new_section = Section(
        section_name=section_name, date_added=date_added)
    db.session.add(new_section)
    db.session.commit()

    return new_section.id

def DeleteSection():
    pass

def UpdateSection():
    pass
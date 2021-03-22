import textract

def read(picture_url):
    '''
    returns a string of all text read on a single line
    '''
    text = textract.process(picture_url).decode('utf-8')
    single_line_text = str.join(' ', text.splitlines())

    configured_text = configure_text(single_line_text)
    print (text)

    return configured_text

def configure_text(text):
    return_text = text.replace('é', 'e')

    return return_text
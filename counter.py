import warnings
warnings.filterwarnings("ignore")

def counter(query:str, doc:str):
    doc=doc.lower()
    list_words=doc.split()
    number = 0
    for word in list_words:
        if query in word:
            number +=1
    return number
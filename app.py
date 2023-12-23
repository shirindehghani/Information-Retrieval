from fastapi import FastAPI
from IR_models.Retrieval import query_builder_andRetrieve, ExactRetrieval, openAI

app = FastAPI()

def query_builder_andRetrieve(query: str):
    tokenize_q = query.split()
    if len(tokenize_q) == 1:
        retriver = ExactRetrieval()
        result = retriver.retrieve_doc(query.lower())
    else:
        retriver = openAI()
        result = retriver.index_embedding(query)
    return result

@app.get("/")
def query_endpoint(query: str):
    result = query_builder_andRetrieve(query)
    return {"result": result}

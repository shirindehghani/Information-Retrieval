from fastapi.testclient import TestClient
from app import app  

client = TestClient(app)

def test1_exact_retrieval():
    query = "mom"
    response = client.get(f"/", params={"query": query})
    assert response.status_code == 200
    assert response.json() == {"result": "LIST_OF_phrases_with_mom"}

def test2_openai():
    query = "mom test"
    response = client.get(f"/", params={"query": query})
    assert response.status_code == 200
    assert response.json() == {"result": "LIST_OF_phrases_with_mom test_or near this"}
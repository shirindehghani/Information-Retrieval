from fastapi.testclient import TestClient
from app import app  

client = TestClient(app)

def test1_exact_retrieval():
    query = "father"
    response = client.get(f"/", params={"query": query})
    assert response.status_code == 200
    assert response.json() == {
  "result": [
    "“what’s the last thing you did on it?” \nget specific about\nexamples in the past to get real, concrete data.\nmom: \n“you know your father and i are planning that trip? i was\nfiguring out where we could stay. “ \nshe uses it for both\nentertainment and utility, which didn’t come up during the",
    "“what’s the last cookbook you did buy for yourself?” \nattack\ngeneric answers like “i don’t buy cookbooks” by asking for\nspecific examples.\nmom: \n“now that you mention it, i bought a vegan cookbook about 3\nmonths ago. your father is trying to eat healthier and thought my"
  ]
}
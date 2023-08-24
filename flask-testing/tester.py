import pytest
import demoapi
import math
import requests

"""TESTS THE FIRST ENDPOINT, /squared"""
def test_squared():
    # get a bunch of numbers (not just 10) and run them ALL against get_value() function
    edgecasenums= [-2, 0, 34534534563453453434534534534343, 3.14159265358979323846, math.sqrt(1)]

    for num in edgecasenums:
       assert demoapi.get_value(num) == {'squared': num ** 2}
# makes an object named "client" that represents a "test connection" to our flask server
# advantage of this is that the flask app doesn't actually need to be running!


"""TESTS THE SECOND ENDPOINT, /static"""
# make sure /static always returns that array
def test_static():
    # executes the "get_static_value" function in our flask script
    returnvalue= demoapi.get_static_value()

    assert type(returnvalue) == list
    assert returnvalue == ["this","is","always","returned"]
    assert len(returnvalue) == 4

"""TESTS THE THIRD ENDPOINT, /answer"""

# this teaches pytest to make a test connection to our flask server for testing purposes!
# this is nice because the server doesn't actually have to be running to be tested
@pytest.fixture
def client():
    with demoapi.app.test_client() as client:
        yield client

def test_posts(client):
    # make a list of answers that should NOT be correct
    # post them all and assert we won't get "Correct!"
    edgecases= [42, "abc", 3.14, "forty two", ""]
    for fail in edgecases:
        resp = client.post('/answer', json={'value': fail})
        print(resp.text)
        assert not resp.data.decode("utf-8") == "Correct!"

    # post the correct answer, "42"
    # assert we will get "Correct!"
    resp = client.post('/answer', json={'value': '42'})
    print(resp.text)
    assert resp.data.decode("utf-8") == "Correct!"

# This test requires the flask app to be running!
# def test_postreq():
#    URL= "http://127.0.0.1:2225/answer"
#    response= requests.post(URL, json={"value":"42"})
#    assert response.text == "Correct!"

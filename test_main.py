from fastapi.testclient import TestClient

from main import app, logger

client = TestClient(app)


def test1():
    data = {
        "tittle": "some tittle",
        "cooking_time": "08:42:00",
        "ingredient_list": ["meat"],
        "description": "cook it",
    }
    response = client.post(json=data, url="/recipes")
    print(response.json())
    logger.info(response.json())
    assert response.json() == data


if __name__ == "__main__":
    test1()

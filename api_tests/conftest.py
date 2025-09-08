import os

import pytest
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent/"creds.env")

access_token = None

@pytest.fixture(scope="session")
def generate_token():
    global access_token
    if access_token is None:
        url = f"{os.getenv('BASE_URL')}/Account/v1/GenerateToken"
        payload = {
          "userName": os.getenv('USER_NAME'),
          "password": os.getenv('PASSWORD')
        }
        response = requests.post(url=url,json=payload)
        response_json = response.json()
        access_token =response_json["token"]
    return {"Authorization":f"Bearer {access_token}","Content-Type":"application/json"}

@pytest.fixture()
def base_url():
    return os.getenv('BASE_URL')

@pytest.fixture()
def user_name():
    return os.getenv('USER_NAME')

@pytest.fixture()
def password():
    return os.getenv('PASSWORD')

def pytest_configure(config):
    config.addinivalue_line(
        "markers","skip_or_continue_test_based_on_value: Skip or continue the test based on marker value"
    )
    config.addinivalue_line(
        "markers", "test_marker: This is just a test marker"
    )

def pytest_runtest_setup(item):
    marker = item.get_closest_marker("skip_or_continue_test_based_on_value")
    if marker:
        value = marker.args[0]
        if value == "skip":
            pytest.skip("Skipping this test as value is skip")
        elif value == "Continue":
            pass
        else:
            raise pytest.UsageError("Invalid marker value")

def pytest_collection_finish(session):
    session.items.reverse()

def pytest_addoption(parser):
    parser.addoption(
        "--testrun",
        action="store",
        default="test"
    )

@pytest.fixture()
def testrun(request):
    env = request.config.getoption("testrun")
    yield env






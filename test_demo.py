import sys
import requests
import pytest

print(sys.version)
print(sys.executable)


# @pytest.fixture(scope="session", name="temp_path")
# def fixture_temp_path(tmp_path_factory):
#     path = tmp_path_factory.mktemp("shreyas_data")
#     return path


def test_data(temp_path):
    test = "Test"
    print(temp_path.joinpath("test.csv"))
    assert 1 == 1


r = requests.get("https://www.google.com")
print(r.status_code)
print(r.ok)

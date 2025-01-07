import pytest
from unittest.mock import MagicMock
from src.util.detector import detect_duplicates

# develop your test cases here

@pytest.mark.unit
def test_detect_duplicates():
    assert True

@pytest.fixture
def article_mock():
    mock_dao = MagicMock()
    return mock_dao

@pytest.mark.unit
def test_len_0():
    data = []
    with pytest.raises(ValueError, match="The input data does not contain enough articles to detect duplicates."):
        detect_duplicates(data)
   

@pytest.mark.unit
def test_article_same_name_doi(article_mock):
    data = ["frattini2023requirements", "fernandez2017naming", "mendez2017naming", "wagner2019status", "frattini2023requirements"]
    article_mock.parse = MagicMock(return_value=[data])
    detect_duplicates(data)
    


import pytest
from unittest.mock import MagicMock
from src.util.detector import detect_duplicates
#from src.util.parser import parse
from unittest.mock import patch

DATA_DUP_KEY_DOI = """@article{SAME,
  title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
  doi={10.1007/s10664-016-9451-7}
}

@article{SAME,
  title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
  doi={10.1007/s10664-016-9451-7}
}"""

DATA_DUP_KEY = """@article{SAME,
  title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
}

@article{SAME,
  title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
}"""

DATA_UNIQ = """@article{SAME,
  title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
}

@article{NOT SAME,
  title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
}"""

# develop your test cases here


@pytest.mark.unit
def test_detect_duplicates():
    assert True

@pytest.mark.unit
def test_len_0():
    with pytest.raises(ValueError, match="The input data does not contain enough articles to detect duplicates."):
        detect_duplicates("")

@pytest.mark.unit
def test_article_same_doi_key():
    res = detect_duplicates(DATA_DUP_KEY_DOI)
    assert len(res) == 1
    
@pytest.mark.unit
def test_article_same_key_no_doi():
    res = detect_duplicates(DATA_DUP_KEY)
    assert len(res) == 1

@pytest.mark.unit
def test_article_no_duplicate():
    res = detect_duplicates(DATA_UNIQ)
    assert len(res) == 0
    

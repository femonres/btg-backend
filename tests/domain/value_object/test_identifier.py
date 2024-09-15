import pytest

from domain import Identifier

@pytest.fixture
def identifier():
    return Identifier(id="12345")

class TestIdentifier:

    def test_identifier_initialization(self, identifier: Identifier):
        assert identifier.id == "12345"

    def test_identifier_generate(self):
        id1 = Identifier.generate()
        id2 = Identifier.generate()
        assert isinstance(id1, Identifier)
        assert isinstance(id2, Identifier)
        assert id1 != id2  # UUIDs should be unique

    def test_identifier_repr(self, identifier: Identifier):
        assert repr(identifier) == "Identifier(id='12345')"

    def test_identifier_equality(self, identifier: Identifier):
        id1 = Identifier(id="12345")
        id2 = Identifier(id="12345")
        id3 = Identifier(id="67890")
        assert id1 == id2
        assert id1 != id3

    def test_identifier_hash(self, identifier: Identifier):
        id1 = Identifier(id="12345")
        id2 = Identifier(id="12345")
        assert hash(id1) == hash(id2)
        assert hash(id1) != hash(Identifier(id="67890"))
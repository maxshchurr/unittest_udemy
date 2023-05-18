import unittest


class Doc:
    def __init__(self, string: str) -> None:
        self.string = string

    def __repr__(self) -> str:
        return f"Doc(string='{self.string}')"

    def __lt__(self, other) -> bool:
        return len(self.string) < len(other.string)

    def __gt__(self, other) -> bool:
        return len(self.string) > len(other.string)

# Enter your solution here
class TestDoc(unittest.TestCase):
    def test_less_than(self):
        doc1 = Doc('Babayka')
        doc2 = Doc('Online')
        doc3 = Doc('Nature')
        self.assertLess(doc2, doc1)
        self.assertLess(doc3, doc1)

    def test_greater_than(self):
        doc1 = Doc('Technology')
        doc2 = Doc('Online')
        doc3 = Doc('Nature')
        self.assertGreater(doc1, doc2)
        self.assertGreater(doc1, doc3)

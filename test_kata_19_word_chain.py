from unittest import TestCase

from kata_19_word_chain import change_word


class Test(TestCase):
    def test_foo(self):
        self.fail()

    def test_change_word(self):
        changed_word = change_word('bat')
        self.assertEqual('cat', changed_word)
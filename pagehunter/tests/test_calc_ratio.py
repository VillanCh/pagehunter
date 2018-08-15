#!/usr/bin/env python3
import unittest
from .. import core


class PageHunterTest(unittest.TestCase):
    """"""

    def test_calc_ratio(self):
        """"""
        text = 'abc123cdef'
        text1 = 'abc123334cdef'

        self.assertIsInstance(core.calc_ratio(text, text1), float)

    def test_dynamic_page_hunter(self):
        text1 = "1112231341adfadfasfadfasdfadqweerhdfgasdf35178512937135"
        text2 = "1112231341adfadfasfadfjksdbfashdfasdfadqw" + \
                "eerhdfgasdf35178512937135"

        markings = core.extract_dynamic_content_marking(text1, text2)
        self.assertIsInstance(markings, list)
        _ret = core.remove_dynamic_content_by_markings(
            text2, markings, repl="")
        print()
        print(text1)
        print(text2)
        print(_ret)
        self.assertTrue(text1 == _ret)

    def test_extract_between_prefix_and_suffix(self):
        text = "abcdefgagagagaga1231231231ababababc"       
        prefix = 'ga'
        suffix = "ab"  # (?=ab)

        texts = core.extract_by_prefix_and_suffix(text, prefix, suffix) 
        self.assertIsInstance(texts, list)

        self.assertTrue(len(texts) > 0)


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/env python3
# coding:utf-8
import json
import itertools
from . import utils

_TYPE_JSON = 'json'
_TYPE_XML = "xml"
_TYPE_HTML = "html"


class Page(object):

    def __init__(self, raw, default_split=" "):
        self._raw = raw
        self._without_script_and_style = utils.get_filtered_page_content(
            raw, onlyText=False, split=default_split
        )
        self._text_without_script_and_style = utils.get_filtered_page_content(
            raw, onlyText=True, split=default_split
        )

    @property
    def raw(self):
        """"""
        return self._raw

    @property
    def without_script_and_style(self):
        """"""
        return self._without_script_and_style

    @property
    def text_without_script_and_style(self):
        """"""
        return self._text_without_script_and_style


class PageHunter(object):

    def __init__(self, base_page, split=" "):
        if isinstance(base_page, Page):
            pass
        else:
            base_page = Page(base_page, split)
        self.first_page = base_page
        self.base_pages = []
        self.base_pages.append(self.first_page)

        # all base_pages are the same in raw
        self._raw_stable = None

        # all base_pages are the same in without_style_and_script
        self._noscript_stable = None

        # all base_pages are the text_only
        self._text_stable = None

        # dynamic markings
        self.raw_dynamic_markings = []
        self.noscript_dynamic_markings = []
        self.text_dynamic_markings = []

    def add_base_page_string(self, raw):
        """"""
        self.add_base_page(Page(raw))

    def add_base_page(self, page):
        """"""
        self._feed_base_page(page)

    @property
    def pass_stable_checking(self):
        """"""
        _ret = self._raw_stable is None and self._noscript_stable is None and\
            self._text_stable is None
        return _ret

    def _feed_base_page(self, page: Page):
        """"""
        self._raw_stable = 0 <= len(
            [base_page for base_page in self.base_pages if base_page.raw == page.raw])

        self._noscript_stable = 0 <= len(
            [base_page for base_page in self.base_pages if base_page.without_script_and_style ==
                page.without_script_and_style]
        )
        self._text_stable = 0 <= len(
            [base_page for base_page in self.base_pages if base_page.text_without_script_and_style ==
                page.text_without_script_and_style]
        )
        self.base_pages.append(page)

        # extrace dynamic markings
        self._update_dynamic_markings()

    def _update_dynamic_markings(self):
        """"""
        if len(self.base_pages) <= 1:
            return []

        for (base1, base2) in self.base_pages:
            for item in utils.extract_dynamic_content_marking(
                    base1.raw, base2.raw):
                if item not in self.raw_dynamic_markings:
                    self.raw_dynamic_markings.append(item)

            for item in utils.extract_dynamic_content_marking(
                    base1.without_script_and_style, base2.without_script_and_style):
                if item not in self.noscript_dynamic_markings:
                    self.noscript_dynamic_markings.append(item)

            for item in utils.extract_dynamic_content_marking(
                    base1.text_without_script_and_style, base2.text_without_script_and_style):
                if item not in self.text_dynamic_markings:
                    self.text_dynamic_markings.append(item)

    def calc_ratio_with_base_page(self, ):
        """"""
        pass

    def remove_dynamic_content_for_raw(self, raw, repl=" "):
        """"""
        return utils.remove_dynamic_content_by_markings(raw, self.raw_dynamic_markings, repl)

    def remove_dynamic_content_for_noscript(self, noscript_text, repl=" "):
        """"""
        return utils.remove_dynamic_content_by_markings(
            noscript_text, self.noscript_dynamic_markings, repl)

    def remove_dynamic_content_for_textonly(self, text, repl=" "):
        """"""
        return utils.remove_dynamic_content_by_markings(text, self.text_dynamic_markings, repl)




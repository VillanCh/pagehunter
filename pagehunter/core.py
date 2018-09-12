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


_PAGE_KEYS = ("raw", "without_script_and_style", "text_without_script_and_style")


class PageHunter(object):

    def __init__(self, base_page, split=" ", diff_char_count=30, fixed_ratio=None):
        if isinstance(base_page, Page):
            pass
        else:
            base_page = Page(base_page, split)
        self.first_page = base_page
        self.base_pages = []
        self.base_pages.append(self.first_page)

        # all base_pages are the same in raw
        self._raw_stable = None
        self._raw_dynamic = None
        self._raw_heavy_dynamic = None

        # all base_pages are the same in without_style_and_script
        self._noscript_stable = None
        self._noscript_dynamic = None
        self._noscript_heavy_dynamic = None

        # all base_pages are the text_only
        self._text_stable = None
        self._text_dynamic = None
        self._text_heavy_dynamic = None

        # tolerence
        self.diff_char_count = 30
        self.fixed_ratio = fixed_ratio

        # dynamic markings
        self.raw_dynamic_markings = []
        self.noscript_dynamic_markings = []
        self.text_dynamic_markings = []

    @property
    def stable_raw(self):
        return self._raw_stable

    @property
    def dynamic_raw(self):
        """"""
        return self._raw_dynamic

    @property
    def heavy_dynamic_raw(self):
        """"""
        return self._raw_heavy_dynamic

    @property
    def stable_noscript(self):
        """"""
        return self._noscript_stable

    @property
    def dynamic_noscript(self):
        """"""
        return self._noscript_dynamic

    @property
    def heavy_dynamic_noscript(self):
        """"""
        return self._noscript_heavy_dynamic

    @property
    def stable_text(self):
        """"""
        return self._text_stable

    @property
    def dynamic_text(self):
        """"""
        return self._text_dynamic

    @property
    def heavy_dynamic_text(self):
        """"""
        return self._text_heavy_dynamic

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
        return not _ret

    def _feed_base_page(self, page: Page):
        """"""
        def heavy_dynamic(str1, str2):
            if not self.fixed_ratio:
                ratio = 1.0 - 1.0 * self.diff_char_count / min(len(str1), len(str2))
            else:
                ratio = self.fixed_ratio
            return ratio > utils.calc_ratio(str1, str2)

        # update stable
        if self._raw_stable or self._raw_stable is None:
            self._raw_stable = 0 == len(
                [base_page for base_page in self.base_pages if base_page.raw != page.raw])

        if not self._raw_heavy_dynamic or self._raw_dynamic is None:
            self._raw_dynamic = not self._raw_stable
            self._raw_heavy_dynamic = 0 < len(
                [base_page for base_page in self.base_pages if heavy_dynamic(base_page.raw, page.raw)]
            )

        if self._noscript_stable or self._noscript_stable is None:
            self._noscript_stable = 0 == len(
                [base_page for base_page in self.base_pages if base_page.without_script_and_style !=
                    page.without_script_and_style]
            )

        if not self._noscript_heavy_dynamic or self._noscript_dynamic is None:
            self._noscript_dynamic = not self._noscript_stable
            self._noscript_heavy_dynamic = 0 < len(
                [base_page for base_page in self.base_pages if heavy_dynamic(
                    page.without_script_and_style, base_page.without_script_and_style
                )]
            )

        if self._text_stable or self._text_stable is None:
            self._text_stable = 0 == len(
                [base_page for base_page in self.base_pages if base_page.text_without_script_and_style !=
                    page.text_without_script_and_style]
            )

        if not self._text_heavy_dynamic:
            self._text_dynamic = not self._text_stable
            self._text_heavy_dynamic = 0 < len(
                [base_page for base_page in self.base_pages if heavy_dynamic(
                    page.text_without_script_and_style, base_page.text_without_script_and_style
                )]
            )
        self.base_pages.append(page)

        # extrace dynamic markings
        self._update_dynamic_markings()

    def _update_dynamic_markings(self):
        """"""
        if len(self.base_pages) <= 1:
            return []

        for (base1, base2) in itertools.combinations(self.base_pages, 2):
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

    def calc_ratio_with_base_page(self, page: Page, remove_dynamic_content=True, repl=" ", types=None,
                                  to_all_base_pages=True):
        """"""
        def _calc_ratio(type):
            if not type:
                return None
            min_raw_ratio = 1.0
            if to_all_base_pages:
                pages = self.base_pages
            else:
                pages = [self.first_page]
            for base_page in pages:
                seq1 = getattr(base_page, type)
                seq2 = getattr(page, type)
                if remove_dynamic_content:
                    if type == "raw":
                        seq1 = self.remove_dynamic_content_for_raw(seq1, repl)
                        seq2 = self.remove_dynamic_content_for_raw(seq2, repl)
                    elif type == 'without_script_and_style':
                        seq1 = self.remove_dynamic_content_for_noscript(seq1, repl)
                        seq2 = self.remove_dynamic_content_for_noscript(seq2, repl)
                    elif type == "text_without_script_and_style":
                        seq1 = self.remove_dynamic_content_for_textonly(seq1, repl)
                        seq2 = self.remove_dynamic_content_for_textonly(seq2, repl)
                ratio = utils.calc_ratio(seq1, seq2)
                min_raw_ratio = min(min_raw_ratio, ratio)
            return min_raw_ratio
        _types = _PAGE_KEYS
        if not types:
            types = _types
        else:
            def _check(_type):
                if _type in types:
                    return _type
                else:
                    return None
            types = tuple([_check(_t) for _t in _types])
        return tuple([_calc_ratio(type) for type in types])

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

    def get_border_ratio(self, len1=None):
        if self.fixed_ratio:
            return self.fixed_ratio
        else:
            if len1:
                return (1.0 - 1.0 * self.diff_char_count / len1)
            else:
                return 0.98

    def compare_with_base_page(self, page: Page, to_all_base_pages=False, remove_dynamic_content=True, repl=' '):
        ks = _PAGE_KEYS

        ratios = self.calc_ratio_with_base_page(page, remove_dynamic_content, repl, to_all_base_pages=to_all_base_pages)
        items = list(zip(ratios,
                         [self.get_border_ratio(self.get_pages_min_length(key, page, *self.base_pages))
                          for key in ks]))
        # rraw >= self.get_border_ratio(self.get_pages_min_length("raw", page, *self.base_pages)),
        return tuple([
            ratio >= border for (ratio, border) in items
        ])

    def get_pages_min_length(self, key, *pages):
        ks = _PAGE_KEYS
        if key not in ks:
            raise ValueError('key: {} not in {}'.format(key, ks))

        def get_len(page):
            return len(getattr(page, key))

        if not pages:
            raise ValueError("empty pages")

        if len(pages) == 1:
            return get_len(pages[0])
        else:
            return min([get_len(page) for page in pages])


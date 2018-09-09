#!/usr/bin/env python3
import re
import typing
from difflib import SequenceMatcher


# from sqlmap
def htmlunescape(value):
    """
    From Sqlmap

    Returns (basic conversion) HTML unescaped value
    >>> htmlunescape('a&lt;b')
    'a<b'
    """

    retVal = value
    if value and isinstance(value, str):
        codes = (("&lt;", '<'), ("&gt;", '>'), ("&quot;", '"'),
                 ("&nbsp;", ' '), ("&amp;", '&'), ("&apos;", "'"))
        retVal = reduce(lambda x, y: x.replace(y[0], y[1]), codes, retVal)
        try:
            retVal = re.sub(
                r"&#x([^ ;]+);", lambda match: chr(int(match.group(1), 16)), retVal)
        except ValueError:
            pass
    return retVal


def get_filtered_page_content(page, onlyText=True, split=" "):
    """
    From Sqlmap

    Returns filtered page content without script, style and/or comments
    or all HTML tags
    >>> getFilteredPageContent(u'<html><title>foobar</title><body>test</body></html>')
    u'foobar test'
    """

    retVal = page

    # only if the page's charset has been successfully identified
    if isinstance(page, str):
        retVal = re.sub(r"(?si)<script.+?</script>|<!--.+?-->|<style.+?</style>%s" %
                        (r"|<[^>]+>|\t|\n|\r" if onlyText else ""), split, page)
        retVal = re.sub(r"%s{2,}" % split, split, retVal)
        retVal = htmlunescape(retVal.strip().strip(split))

    return retVal


def calc_ratio(seq1: str, seq2: str,
               autojunk: bool = True, isjunk=None) -> float:
    _seqmt = SequenceMatcher(isjunk, seq1, seq2, autojunk)
    ret = _seqmt.ratio()
    del _seqmt
    return ret


def extract_dynamic_content_marking(
    seq1: str, seq2: str,
    autojunk: bool = True, isjunk=None, border_length=20
) -> typing.List[typing.Tuple[str, str]]:
    seqm = SequenceMatcher(isjunk, seq1, seq2, autojunk)
    blocks = list(seqm.get_matching_blocks())

    mached_markings = []
    while blocks:
        current_block = blocks.pop(0)
        if current_block.size < border_length:
            continue

        if not blocks:
            break

        for next_block in blocks:
            next_block = blocks[0]
            if next_block.size < border_length:
                continue

            prefix = seq1[
                current_block.a:current_block.a + current_block.size
            ][-border_length:]
            suffix = seq1[
                next_block.a:next_block.a + next_block.size
            ][:border_length]

            mached_markings.append((prefix, suffix))
            break

    return mached_markings


def regex_remove_dynamic_content_by_markings(
    text: str,
    markings: typing.List[typing.Tuple],
    repl: str = " "
) -> str:
    for (prefix, suffix) in markings:
        rgx = re.compile("(?<={}).*(?={})".format(
            re.escape(prefix), re.escape(suffix)
        ))
        text = rgx.sub(repl, text)
    return text


def _extractNremove_by_prefix_and_suffix(text, prefix, suffix, repl=" "):
    if not prefix or not suffix or not text:
        return []
    if (prefix not in text) or (suffix not in text):
        return []

    textlist = list(text)
    frstc_p = prefix[0]
    len_p = len(prefix)
    frstc_s = suffix[0]
    len_s = len(suffix)
    state = "CLOSE"  # NO OPEN CLOSE

    results = []
    freelist = []
    buff = ""
    # print(frstc_p, frstc_s)
    while textlist:
        _chr = textlist[0]
        # print("".join(freelist), "buff:", buff, "_chr:", _chr)
        # import time
        # time.sleep(0.2)

        if _chr == frstc_p:
            if "".join(textlist[:len_p]) == prefix:
                state = "OPEN"
                freelist.append(buff)
                # print("add BUff", buff)
                buff = ""
                [freelist.append(textlist.pop(0)) for _ in range(len_p)]
                continue
            else:
                freelist.append(textlist.pop(0))
        elif _chr == frstc_s:
            if state == "OPEN":
                if "".join(textlist[:len_s]) == suffix:
                    state = "CLOSE"
                    results.append(buff)
                    freelist.append(repl)
                    [freelist.append(textlist.pop(0)) for _ in range(len_s)]
                    continue
                else:
                    buff += _chr
                    textlist.pop(0)
                    # freelist.append(textlist.pop(0))
            else:
                freelist.append(textlist.pop(0))
        else:
            if state == "OPEN":
                buff += _chr
                textlist.pop(0)
            else:
                freelist.append(textlist.pop(0))

    return "".join(freelist), results


def extract_by_prefix_and_suffix(text, prefix, suffix):
    _, results = _extractNremove_by_prefix_and_suffix(text, prefix, suffix)
    return results


def remove_dynamic_content_by_markings(text, markings, repl=" "):
    for (prefix, suffix) in markings:
        text, _ = _extractNremove_by_prefix_and_suffix(
            text, prefix, suffix, repl,
        )
    return text

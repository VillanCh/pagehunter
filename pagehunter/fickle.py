#!/usr/bin/env python3
# coding:utf-8
import argparse
import json as jsonformatter
from collections import OrderedDict
from urllib.parse import urlparse, quote, urlunparse
import requests
import unittest

Q_TYPE_RAW = "raw"
Q_TYPE_KVP = "kvp"
Q_TYPES = [
    Q_TYPE_KVP,
    Q_TYPE_RAW
]

_DEFAULT_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " + \
              "(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"


def define_from_argparser(parser: argparse.ArgumentParser):
    _DEFAULT_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " + \
                  "(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
    parser.add_argument("--url", dest="url", help="target url")
    parser.add_argument("--method", dest="method", help="http method")
    parser.add_argument("--query", dest="query", help="query for http")
    parser.add_argument("--data", dest="data", help="post data for http")
    parser.add_argument("--auth-user", dest="auth_user", help="basic auth user for http")
    parser.add_argument("--auth-pass", dest="auth_pass", help="basic auth pass for http")
    parser.add_argument("--headers", dest="headers", help="http headers (json-formatted)")
    parser.add_argument("--cookies", dest='cookies', help="cookies for http request (raw)")
    parser.add_argument("--ua", dest='user_agent', default=_DEFAULT_UA, help="User-Agent for http request (raw)")


class QueryParam(object):
    def __init__(self, type=Q_TYPE_KVP, key=None, value=None):
        if type not in Q_TYPES:
            raise ValueError("not a valid query param type: {}. available: {}".format(
                type, Q_TYPES))
        self.type = type
        self._key = key
        self._value = value

    @property
    def normal(self):
        if self.key and self.value:
            return "{}={}".format(quote(self.key), quote(self.value))
        else:
            if self.key:
                return self.key
            if self.value:
                return self.value
            return ""

    @property
    def key(self):
        return self._key or ""

    @property
    def value(self):
        return self._value or ""

    @value.setter
    def value(self, new_value):
        self._value = new_value


class QueryParamContainer(object):
    def __init__(self):
        self._params = []

    def add_query(self, query):
        if query:
            self._parse_query(query)

    def add_dict(self, dict_: dict):
        for (k, v) in dict_.items():
            self._params.append(QueryParam(Q_TYPE_KVP, k, v))

    def _parse_kvpair(self, kvpair: str) -> QueryParam:
        """"""
        if "=" in kvpair:
            first_eq_index = kvpair.index('=')
            key = kvpair[:first_eq_index]
            value = kvpair[first_eq_index + 1:]
            return QueryParam(Q_TYPE_KVP, key, value)
        else:
            return QueryParam(Q_TYPE_RAW, kvpair)

    def _parse_query(self, query: str):
        if '&' in query:
            for pair in query.split("&"):
                self._params.append(
                    self._parse_kvpair(pair)
                )
        else:
            self._params.append(
                self._parse_kvpair(query)
            )

    @property
    def keys(self):
        return [param.key for param in self._params
                if param.key]

    def normal(self, allow_repeat=True):
        _base = []
        if allow_repeat:
            _params = self._params
        else:
            _buff = OrderedDict()
            for param in self._params:
                _buff[param.key] = param
            _params = list(_buff.values())
        for param in _params:
            _base.append(param.normal)
        return "&".join(_base)

    def append(self, param: QueryParam, allow_repeat=True):
        _ret = self.normal(allow_repeat)
        if _ret:
            return "&".join((_ret, param.normal))
        else:
            return param.normal

    def mutate(self, param: QueryParam, index=0, allow_repeat=True):
        if not isinstance(param, QueryParam):
            raise ValueError("the param: {} is not a QueryParam but {}".format(
                param, type(param)
            ))
        _base = []
        count = 0
        handled_key = []
        _mx = self.keys.count(param.key)
        index = _mx - 1 if index >= _mx else index
        for _base_param in self._params:
            if _base_param.key not in handled_key:
                handled_key.append(_base_param.key)
            else:
                if not allow_repeat:
                    continue
            if _base_param.key != param.key:
                _base.append(_base_param.normal)
            else:
                if count == index:
                    _base.append(param.normal)
                else:
                    _base.append(_base_param.normal)
                count += 1
        return "&".join(_base)

    def merge(self, key, new_value):
        for i in self._params:
            if key == i.key:
                i.value = new_value


class FickleRequest(object):
    def __init__(self, url, method="GET", headers=None, data=None, params=None,
                 auth=None, cookies=None, json=None):
        self._urlparse = urlparse(url)
        self.headers = headers
        self.auth = auth
        self.cookies = cookies
        self.method = method
        # parse query
        self.query_container = QueryParamContainer()
        self.query_container.add_query(self._urlparse.query)
        if isinstance(params, dict):
            self.query_container.add_dict(params)
        else:
            self.query_container.add_query(params)
        # set body
        # parse json or data
        if json and data:
            raise ValueError("Json and Data shoule be set only one.")
        if json:
            json = quote(jsonformatter.dumps(json))
            self.body = json or ""
        else:
            self.body = self._parse_data(data) or ""

    def _parse_data(self, data):
        if not data:
            return None
        if isinstance(data, dict):
            _base = []
            for (k, v) in data.items():
                _base.append("{}={}".format(
                    quote(k), quote(v)
                ))
            return "&".join(_base)
        else:
            return str(data)

    @classmethod
    def from_request(cls, req: requests.Request):
        requests.Request()
        return cls(url=req.url, method=req.method, headers=req.headers, data=req.data,
                   params=req.params, auth=req.auth, cookies=req.cookies, json=req.json)

    @property
    def scheme(self):
        return self._urlparse.scheme

    @property
    def netloc(self):
        return self._urlparse.netloc

    @property
    def path(self):
        return self._urlparse.path

    @property
    def query(self):
        return self.query_container.normal(allow_repeat=True)

    @property
    def fragment(self):
        return self._urlparse.fragment

    def mutate_query_param(self, key, value, index=0, allow_repeat=True):
        nq = self.query_container.mutate(QueryParam(type=Q_TYPE_KVP, key=key, value=value),
                                         index=index, allow_repeat=allow_repeat)
        return self._build_request(query=nq)

    def append_query_param(self, key, value=None):
        if value is None:
            nq = self.query_container.append(QueryParam(Q_TYPE_RAW, key))
        else:
            nq = self.query_container.append(QueryParam(Q_TYPE_KVP, key, value))
        return self._build_request(query=nq)

    @property
    def url(self):
        return urlunparse(
            (self.scheme, self.netloc, self.path, "", self.query, self.fragment)
        )

    def url_with_query(self, query, url=None):
        if url:
            urli = urlparse(url)
        else:
            urli = self._urlparse

        return urlunparse(
            (urli.scheme, urli.netloc, urli.path, "", query, urli.fragment)
        )

    def _build_request(self, method=None, url=None, query=None, data=None, cookies=None, auth=None):
        return requests.Request(
            method=method or self.method,
            url=self.url_with_query(query, url) if query else self.url,
            data=data or self.body,
            cookies=cookies or cookies,
            auth=auth or self.auth
        )


_raw = """
{
    "method": "GET",
    "query": null,
    "data": null,
    "auth_user": 
}
"""


def get_fickle_request_from_options(options):
    def get_item(key, default=None):
        _item = getattr(options, key, None)
        if _item is not None:
            return _item
        else:
            try:
                return options.get(key, default)
            except:
                return default

    url = get_item("url", None)
    if not url:
        raise ValueError("url cannot be empty")

    method = get_item("method", "GET")
    query = get_item("query", None)
    data = get_item("data", None)
    username = get_item("auth_user", None)
    password = get_item("auth_pass", None)
    if not username and not password:
        auth = None
    else:
        auth = {"username": username, "password": password}

    # parse headers
    headers = jsonformatter.loads(get_item("headers", "{}"))
    ua = get_item("user_agent", _DEFAULT_UA)
    if ua:
        headers["User-Agent"] = ua
    if not headers:
        headers = None

    # parse cookie
    cookies = get_item("cookies", None)

    return FickleRequest(url, method, headers, data, query, auth, cookies)


def get_fickle_request(url, method="GET", query=None, data=None, auth_user=None, auth_pass=None, user_agent=None):
    kwargs = {
        "url": url,
        "method": method,
        "query": query,
        "data": data,
        "auth_user": auth_user,
        "auth_pass": auth_pass,
        "user_agent": user_agent
    }
    return get_fickle_request_from_options(kwargs)


class ParseURLTestCase(unittest.TestCase):
    def test_fickleurl(self):
        furl = FickleRequest(url='https://baidu.com/a/b/c/d?b=1&a=2&adsf=1zz#fragment')
        self.assertEqual(furl.scheme, "https")
        self.assertEqual(furl.netloc, "baidu.com")
        self.assertEqual(furl.path, "/a/b/c/d")
        self.assertEqual(furl.query, "b=1&a=2&adsf=1zz")
        self.assertEqual(furl.fragment, "fragment")
        req = furl.mutate_query_param("b", "123123123123123123sfasdfa")
        _u = req.url
        self.assertEqual(_u,
                         'https://baidu.com/a/b/c/d?b=123123123123123123sfasdfa&a=2&adsf=1zz#fragment')

    def test_get_fickle_request(self):
        f = get_fickle_request(url="http://baidu.com")
        self.assertIsInstance(f, FickleRequest)
        result = QueryParam(key="a", value="1")
        self.assertIsInstance(result.normal, str)

        req = f.append_query_param("a", "1")
        self.assertIsInstance(req, requests.Request)

        s = requests.Session()
        req = s.prepare_request(req)

        self.assertIsInstance(req, requests.PreparedRequest)


if __name__ == "__main__":
    unittest.main()

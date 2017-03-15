# Copyright 2016 The Sensible Code Company
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io

import requests_mock

from unittest import TestCase

from pdftables_api import Client, APIException


class TestEnsureExtFormat(TestCase):
    def test_wrong_format(self):
        self.assertRaises(ValueError, Client.ensure_format_ext, 'foo.csv', 'txt')
        self.assertRaises(ValueError, Client('key').dump, 'foo.pdf', 'txt')

    def test_unmodified(self):
        self.assertEqual(('foo.csv', 'csv'),
                         Client.ensure_format_ext('foo.csv', 'csv'))
        self.assertEqual(('foo.xlsx', 'xlsx-multiple'),
                         Client.ensure_format_ext('foo.xlsx', 'xlsx-multiple'))
        self.assertEqual(('foo.xlsx', 'xlsx-multiple'),
                         Client.ensure_format_ext('foo.xlsx', 'xlsx-multiple'))
        self.assertEqual(('foo.xml', 'xml'),
                         Client.ensure_format_ext('foo.xml', 'xml'))

    def test_missing_format(self):
        self.assertEqual(('foo.xlsx', 'xlsx-multiple'),
                         Client.ensure_format_ext('foo', None))
        self.assertEqual(('foo.txt.xlsx', 'xlsx-multiple'),
                         Client.ensure_format_ext('foo.txt', None))
        self.assertEqual(('foo.xlsx', 'xlsx-multiple'),
                         Client.ensure_format_ext('foo.xlsx', None))

    def test_missing_ext(self):
        self.assertEqual(('foo.csv', 'csv'),
                         Client.ensure_format_ext('foo', 'csv'))

    def test_incorrect_ext(self):
        self.assertEqual(('foo.txt.csv', 'csv'),
                         Client.ensure_format_ext('foo.txt', 'csv'))
        self.assertEqual(('foo.xlsx.csv', 'csv'),
                         Client.ensure_format_ext('foo.xlsx', 'csv'))

    def test_stdout(self):
        self.assertEqual((None, 'xlsx-multiple'),
                         Client.ensure_format_ext(None, None))
        self.assertEqual((None, 'csv'),
                         Client.ensure_format_ext(None, 'csv'))


class TestRequests(TestCase):
    def test_successful_conversion(self):
        with requests_mock.mock() as m:
            m.post('https://pdftables.com/api?key=fake_key', text='xlsx output')

            pdf_fo = io.BytesIO(b'pdf content')
            c = Client('fake_key')
            s = c.dump(pdf_fo, 'csv')
            self.assertEqual(b'xlsx output', consume(s))

    def test_different_api_url(self):
        with requests_mock.mock() as m:
            m.post('http://example.com/api?key=fake_key', text='xlsx output')

            pdf_fo = io.BytesIO(b'pdf content')
            c = Client('fake_key', api_url='http://example.com/api')
            s = c.dump(pdf_fo, 'csv')
            self.assertEqual(b'xlsx output', consume(s))

    def test_missing_api_key(self):
        with requests_mock.mock() as m:
            m.post('https://pdftables.com/api?key=fake_key', text='xlsx output')

            pdf_fo = io.BytesIO(b'pdf content')
            c = Client('')
            self.assertRaisesRegexp(APIException, 'Invalid API key', c.dump, pdf_fo, 'csv')

    def test_invalid_format(self):
        with requests_mock.mock() as m:
            m.post('https://pdftables.com/api?key=fake_key', text='xlsx output')

            pdf_fo = io.BytesIO(b'pdf content')
            c = Client('fake_key')
            self.assertRaisesRegexp(ValueError, 'Invalid output format', c.dump, pdf_fo, 'invalid_format')

    def test_remaining(self):
        pass

    def test_response_invalid_format(self):
        with requests_mock.mock() as m:
            m.post('https://pdftables.com/api?key=fake_key', status_code=400)
            pdf_fo = io.BytesIO(b'pdf content')
            c = Client('fake_key')
            self.assertRaisesRegexp(APIException, 'Unknown file format', c.dump, pdf_fo)

    def test_response_unauthorized(self):
        with requests_mock.mock() as m:
            m.post('https://pdftables.com/api?key=wrong_key', status_code=401)
            pdf_fo = io.BytesIO(b'pdf content')
            c = Client('wrong_key')
            self.assertRaisesRegexp(APIException, 'Unauthorized API key', c.dump, pdf_fo)

    def test_response_limit_exceeded(self):
        with requests_mock.mock() as m:
            m.post('https://pdftables.com/api?key=fake_key', status_code=402)
            pdf_fo = io.BytesIO(b'pdf content')
            c = Client('fake_key')
            self.assertRaisesRegexp(APIException, 'Usage limit exceeded', c.dump, pdf_fo)

    def test_response_unknown_file_format(self):
        with requests_mock.mock() as m:
            m.post('https://pdftables.com/api?key=fake_key', status_code=403)
            png_fo = io.BytesIO(b'png content')
            c = Client('fake_key')
            self.assertRaisesRegexp(APIException, 'Unknown format requested', c.dump, png_fo)


def consume(s):
    r = b''
    for chunk in s:
        r += chunk
    return r

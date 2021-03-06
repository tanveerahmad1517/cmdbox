from model_mommy import mommy

from django.core.urlresolvers import reverse as r
from django.test import TestCase


class ApiSnippetArgsTests(TestCase):
    def setUp(self):
        content = 'Content {0} {1} testing'
        self.snippet = mommy.make('snippets.Snippet', user__username='john', slug='test', content=content)
        data = {'a': 'Test,Format'}
        self.response = self.client.get(
            r('api:snippet', args=('john', 'test')),
            data
        )

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_output(self):
        self.assertContains(self.response, 'Content Test Format testing')

    def test_content_type(self):
        self.assertEqual(self.response['Content-Type'], 'text/plain')


class ApiSnippetKwargsTests(TestCase):
    def setUp(self):
        content = 'Content {key1} {key2} testing'
        self.snippet = mommy.make('snippets.Snippet', user__username='john', slug='test', content=content)
        data = {'key1': 'value1', 'key2': 'value2'}
        self.response = self.client.get(
            r('api:snippet', args=('john', 'test')),
            data
        )

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_output(self):
        self.assertContains(self.response, 'Content value1 value2 testing')

    def test_content_type(self):
        self.assertEqual(self.response['Content-Type'], 'text/plain')


class ApiSnippetHelpTests(TestCase):
    def setUp(self):
        content = 'Content {0} {1} testing'
        self.snippet = mommy.make('snippets.Snippet', user__username='john', slug='test', content=content)
        data = {'help': ''}
        self.response = self.client.get(
            r('api:snippet', args=('john', 'test')),
            data
        )

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_output(self):
        self.assertContains(self.response, 'Content {0} {1} testing')

    def test_content_type(self):
        self.assertEqual(self.response['Content-Type'], 'text/plain')


class ApiSnippetInvalidURLTests(TestCase):
    def setUp(self):
        self.response = self.client.get(r('api:snippet', args=('john', 'test2')))

    def test_get(self):
        self.assertEqual(self.response.status_code, 400)

    def test_output(self):
        self.assertContains(self.response, '[S01]', status_code=400)

    def test_content_type(self):
        self.assertEqual(self.response['Content-Type'], 'text/plain')


class ApiSnippetValueErrorTests(TestCase):
    def setUp(self):
        content = 'Content {0} {1} {} {} testing'
        self.snippet = mommy.make('snippets.Snippet', user__username='john', slug='test', content=content)
        data = {'args': 'arg1,arg2,arg3,arg4'}
        self.response = self.client.get(
            r('api:snippet', args=('john', 'test')),
            data
        )

    def test_get(self):
        self.assertEqual(self.response.status_code, 400)

    def test_output(self):
        self.assertContains(self.response, '[S02]', status_code=400)

    def test_content_type(self):
        self.assertEqual(self.response['Content-Type'], 'text/plain')


class ApiSnippetIndexErrorTests(TestCase):
    def setUp(self):
        content = 'Content {0} {1} testing'
        self.snippet = mommy.make('snippets.Snippet', user__username='john', slug='test', content=content)
        data = {'args': 'arg1'}
        self.response = self.client.get(
            r('api:snippet', args=('john', 'test')),
            data
        )

    def test_get(self):
        self.assertEqual(self.response.status_code, 400)

    def test_output(self):
        self.assertContains(self.response, '[S03]', status_code=400)

    def test_content_type(self):
        self.assertEqual(self.response['Content-Type'], 'text/plain')


class ApiSnippetKeyErrorTests(TestCase):
    def setUp(self):
        content = 'Content {kwarg1} {kwarg2} testing'
        self.snippet = mommy.make('snippets.Snippet', user__username='john', slug='test', content=content)
        data = {'kwarg1': 'value1'}
        self.response = self.client.get(
            r('api:snippet', args=('john', 'test')),
            data
        )

    def test_get(self):
        self.assertEqual(self.response.status_code, 400)

    def test_output(self):
        self.assertContains(self.response, '[S04]', status_code=400)

    def test_content_type(self):
        self.assertEqual(self.response['Content-Type'], 'text/plain')

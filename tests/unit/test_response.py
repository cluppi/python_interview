import unittest

from src.response import Response


class TestResponse(unittest.TestCase):
    def test_response(self):
        Response.handle("Foo", 200)

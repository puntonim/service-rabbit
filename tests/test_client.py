# -*- coding: utf-8 -*-
from service_rabbit.client import RabbitClient

# How to import mock PY3 and PY3 compatible:
# from six import MovedModule, add_move  # isort:skip
# add_move(MovedModule('mock', 'mock', 'unittest.mock'))
# from six.moves import mock  # noqa:E402 isort:skip


class TestGetQueue(object):
    def setup(self):
        self.client = RabbitClient()

    def test_happy_flow(self):
        response = self.client.get_queue('inspire', 'orcid_push')
        response.raise_for_result()
        assert response.ok
        assert response.get_consumers_count() == 5
        assert response.get_messages_count() == 157455

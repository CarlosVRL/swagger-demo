# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.load_list import LoadList  # noqa: E501
from swagger_server.models.parameter_list import ParameterList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLoadController(BaseTestCase):
    """LoadController integration test stubs"""

    def test_get_loads_from_parameters(self):
        """Test case for get_loads_from_parameters

        Convert Parameter Inputs to Load Outputs
        """
        body = ParameterList()
        response = self.client.open(
            '/loads',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

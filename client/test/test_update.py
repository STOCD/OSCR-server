# coding: utf-8

"""
    OSCR API

    OSCR API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from OSCR_django_client.models.update import Update

class TestUpdate(unittest.TestCase):
    """Update unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Update:
        """Test Update
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Update`
        """
        model = Update()
        if include_optional:
            return Update(
                id = 56,
                version = '0',
                url_appimage = '',
                url_msi = '',
                notes = ''
            )
        else:
            return Update(
                version = '0',
        )
        """

    def testUpdate(self):
        """Test Update"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

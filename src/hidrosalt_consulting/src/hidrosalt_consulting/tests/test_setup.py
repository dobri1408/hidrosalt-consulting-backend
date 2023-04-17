"""Setup tests for this package."""
from hidrosalt_consulting.testing import HIDROSALT_CONSULTING_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that hidrosalt_consulting is properly installed."""

    layer = HIDROSALT_CONSULTING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.setup = self.portal.portal_setup
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if hidrosalt_consulting is installed."""
        self.assertTrue(self.installer.is_product_installed("hidrosalt_consulting"))

    def test_browserlayer(self):
        """Test that IHIDROSALT_CONSULTINGLayer is registered."""
        from hidrosalt_consulting.interfaces import IHIDROSALT_CONSULTINGLayer
        from plone.browserlayer import utils

        self.assertIn(IHIDROSALT_CONSULTINGLayer, utils.registered_layers())

    def test_latest_version(self):
        """Test latest version of default profile."""
        self.assertEqual(
            self.setup.getLastVersionForProfile("hidrosalt_consulting:default")[0],
            "20230415001",
        )


class TestUninstall(unittest.TestCase):

    layer = HIDROSALT_CONSULTING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("hidrosalt_consulting")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if hidrosalt_consulting is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("hidrosalt_consulting"))

    def test_browserlayer_removed(self):
        """Test that IHIDROSALT_CONSULTINGLayer is removed."""
        from hidrosalt_consulting.interfaces import IHIDROSALT_CONSULTINGLayer
        from plone.browserlayer import utils

        self.assertNotIn(IHIDROSALT_CONSULTINGLayer, utils.registered_layers())

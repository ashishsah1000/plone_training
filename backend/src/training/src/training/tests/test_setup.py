"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFPlone.utils import get_installer
from training.testing import TRAINING_INTEGRATION_TESTING

import unittest


class TestSetup(unittest.TestCase):
    """Test that training is properly installed."""

    layer = TRAINING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.setup = self.portal.portal_setup
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if training is installed."""
        self.assertTrue(self.installer.is_product_installed("training"))

    def test_browserlayer(self):
        """Test that ITRAININGLayer is registered."""
        from plone.browserlayer import utils
        from training.interfaces import ITRAININGLayer

        self.assertIn(ITRAININGLayer, utils.registered_layers())

    def test_latest_version(self):
        """Test latest version of default profile."""
        self.assertEqual(
            self.setup.getLastVersionForProfile("training:default")[0],
            "20230418001",
        )


class TestUninstall(unittest.TestCase):

    layer = TRAINING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("training")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if training is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("training"))

    def test_browserlayer_removed(self):
        """Test that ITRAININGLayer is removed."""
        from plone.browserlayer import utils
        from training.interfaces import ITRAININGLayer

        self.assertNotIn(ITRAININGLayer, utils.registered_layers())

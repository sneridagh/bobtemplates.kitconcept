# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from kitconcept.policy.testing import KITCONCEPT_POLICY_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that kitconcept.policy is properly installed."""

    layer = KITCONCEPT_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if kitconcept.policy is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'kitconcept.policy'))

    def test_browserlayer(self):
        """Test that IKitconceptPolicyLayer is registered."""
        from kitconcept.policy.interfaces import (
            IKitconceptPolicyLayer)
        from plone.browserlayer import utils
        self.assertIn(IKitconceptPolicyLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = KITCONCEPT_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['kitconcept.policy'])

    def test_product_uninstalled(self):
        """Test if kitconcept.policy is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'kitconcept.policy'))

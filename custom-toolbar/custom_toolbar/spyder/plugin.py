# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Spyder Bot
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------

"""
Custom toolbar plugin.
"""

# Third-party imports
from qtpy.QtGui import QIcon

# Spyder imports
from spyder.api.plugin_registration.decorators import on_plugin_available
from spyder.api.plugins import Plugins, SpyderPluginV2
from spyder.api.translations import get_translation

# Local imports
from custom_toolbar.spyder.container import CustomToolbarContainer

_ = get_translation("custom_toolbar.spyder")


class CustomToolbar(SpyderPluginV2):
    """
    Custom toolbar plugin.
    """

    NAME = "custom_toolbar"
    REQUIRES = [Plugins.Toolbar]
    CONTAINER_CLASS = CustomToolbarContainer
    CONF_SECTION = NAME

    # --- Signals

    # --- SpyderPluginV2 API
    # ------------------------------------------------------------------------
    def get_name(self):
        return _("Custom toolbar")

    def get_description(self):
        return _("Example that shows how to add a custom toolbar to Spyder")

    def get_icon(self):
        return QIcon()

    def on_initialize(self):
        pass

    @on_plugin_available(plugin=Plugins.Toolbar)
    def on_toolbar_available(self):
        container = self.get_container()
        toolbar = self.get_plugin(Plugins.Toolbar)
        toolbar.add_application_toolbar(container.toolbar)

    def on_close(self, cancellable=True):
        return True

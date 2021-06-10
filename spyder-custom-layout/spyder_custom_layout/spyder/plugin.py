# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Spyder Bot
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Custom Layout Plugin.
"""

# Third-party imports
from qtpy.QtGui import QIcon

# Spyder imports
from spyder.api.plugins import Plugins, SpyderDockablePlugin
from spyder.api.translations import get_translation

# Local imports
from spyder_custom_layout.spyder.confpage import SpyderCustomLayoutConfigPage
from spyder_custom_layout.spyder.widgets import SpyderCustomLayoutWidget
from spyder_custom_layout.spyder.api import CustomLayout

_ = get_translation("spyder_custom_layout.spyder")


class SpyderCustomLayout(SpyderDockablePlugin):
    """
    Spyder Custom Layout plugin.
    """

    NAME = "spyder_custom_layout"
    REQUIRES = []
    OPTIONAL = []
    WIDGET_CLASS = SpyderCustomLayoutWidget
    CONF_SECTION = NAME
    CONF_WIDGET_CLASS = SpyderCustomLayoutConfigPage
    CUSTOM_LAYOUTS = [CustomLayout]
    # To force the plugin to be tabbed to a specific plugin even if a layout
    # defines a default area
    # TABIFY = [Plugins.Editor]

    # --- Signals

    # --- SpyderDockablePlugin API
    # ------------------------------------------------------------------------
    def get_name(self):
        return _("Spyder Custom Layout")

    def get_description(self):
        return _("Example plugin that register a programmatic custom layout")

    def get_icon(self):
        return QIcon()

    def register(self):
        widget = self.get_widget()
        

    def check_compatibility(self):
        valid = True
        message = ""  # Note: Remember to use _("") to localize the string
        return valid, message

    def on_close(self, cancellable=True):
        return True

    # --- Public API
    # ------------------------------------------------------------------------

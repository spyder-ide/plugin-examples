# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Spyder Bot
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Status bar widgets Plugin.
"""

# Third-party imports
from qtpy.QtCore import Slot
from qtpy.QtGui import QIcon

# Spyder imports
from spyder.api.plugins import Plugins, SpyderPluginV2
from spyder.api.translations import get_translation

# Local imports
from status_bar_widgets.spyder.container import StatusbarwidgetsContainer

_ = get_translation("status_bar_widgets.spyder")


class StatusbarWidgets(SpyderPluginV2):
    """
    Status bar widgets plugin.
    """

    NAME = "status_bar_widgets"
    REQUIRES = [Plugins.StatusBar, Plugins.Appearance]
    OPTIONAL = []
    CONTAINER_CLASS = StatusbarwidgetsContainer
    CONF_SECTION = NAME

    # --- Signals

    # --- SpyderPluginV2 API
    # ------------------------------------------------------------------------
    def get_name(self):
        return _("Status bar widgets")

    def get_description(self):
        return _("Example that shows how to add wigets to the status bar")

    def get_icon(self):
        return QIcon()

    def register(self):
        container = self.get_container()
        statusbar = self.get_plugin(Plugins.StatusBar)

        # Connect signals
        container = self.get_container()
        container.sig_font_size_change_requested.connect(
            self.on_font_size_change_requested)

        # Add status widgets to status bar
        statusbar.add_status_widget(container.theme_status_widget)
        statusbar.add_status_widget(container.plain_font_size_status)

    def on_close(self, cancellable=True):
        return True

    # --- Public API
    # ------------------------------------------------------------------------
    @Slot(int)
    def on_font_size_change_requested(self, value):
        """This won't be necessary since Spyder 5.1.0!"""
        for __, plugin in self.main._PLUGINS.items():
            plugin.update_font()

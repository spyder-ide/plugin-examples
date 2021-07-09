# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Spyder Bot
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Status bar widgets Main Container.
"""

# Third-party imports
from qtpy.QtCore import Signal

# Spyder imports
from spyder.api.config.decorators import on_conf_change
from spyder.api.translations import get_translation
from spyder.api.widgets.main_container import PluginMainContainer

# Local imports
from status_bar_widgets.spyder.widgets import (
    ThemeStatusWidget, PlainFontSizeStatus)

_ = get_translation("status_bar_widgets.spyder")


class StatusbarwidgetsContainer(PluginMainContainer):

    # Signals
    sig_font_size_change_requested = Signal(int)
    """
    This is signal is emitted to request a plain text font size change
    in Spyder.

    Parameters
    ----------
    font_size: int
        New font size (in pixels).
    """

    # --- PluginMainContainer API
    # ------------------------------------------------------------------------
    def setup(self):
        # Status bar widgets
        self.theme_status_widget = ThemeStatusWidget(self)
        self.plain_font_size_status = PlainFontSizeStatus(self)

        # Set label for font size widget
        self.plain_font_size_status.set_value('Plain font size: ')

        # Connect signal to change font size in the plugin
        self.plain_font_size_status.sig_size_change_requested.connect(
            self.sig_font_size_change_requested)

    def update_actions(self):
        pass

    # --- Public API
    # ------------------------------------------------------------------------
    @on_conf_change(section='appearance', option='selected')
    def on_theme_changed(self, value):
        """Display current syntax highlighting theme in statys bar."""
        self.theme_status_widget.set_value(f'Theme: {value}')

    @on_conf_change(section='appearance', option='font/size')
    def on_font_size_changed(self, value):
        """Display current plain text font size in status bar."""
        self.plain_font_size_status.set_current_size(value)

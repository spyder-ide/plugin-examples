# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Spyder Bot
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Status bar widgets Main Container.
"""
# Spyder imports
from spyder.api.config.decorators import on_conf_change
from spyder.api.translations import get_translation
from spyder.api.widgets.main_container import PluginMainContainer

# Local imports
from status_bar_widgets.spyder.widgets import ThemeStatusWidget

_ = get_translation("status_bar_widgets.spyder")


class StatusbarwidgetsContainer(PluginMainContainer):

    # Signals

    # --- PluginMainContainer API
    # ------------------------------------------------------------------------
    def setup(self):
        # Widget that displays the current syntax highlighting theme.
        self.theme_status_widget = ThemeStatusWidget(self)

    def update_actions(self):
        pass

    # --- Public API
    # ------------------------------------------------------------------------
    @on_conf_change(section='appearance', option='selected')
    def on_theme_changed(self, value):
        self.theme_status_widget.set_value(f'Theme: {value}')

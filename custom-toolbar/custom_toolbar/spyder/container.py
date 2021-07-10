# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Spyder Bot
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------

"""
Custom toolbar main container.
"""

# Third-party imports
from qtpy.QtWidgets import QMessageBox

# Spyder imports
from spyder.api.translations import get_translation
from spyder.api.widgets.main_container import PluginMainContainer

# Local imports
from custom_toolbar.spyder.widgets import CustomToolbar
from custom_toolbar.spyder.api import (
    CustomToolbarActions, CustomToolbarSections)

_ = get_translation("custom_toolbar.spyder")


# ---- Container
# ----------------------------------------------------------------------------
class CustomToolbarContainer(PluginMainContainer):
    """Container for the working directory toolbar."""

    # ---- PluginMainContainer API
    # ------------------------------------------------------------------------
    def setup(self):
        """Create actions and add them to the toolbar"""

        # Widgets
        title = _('Custom toolbar with some simple actions')
        self.toolbar = CustomToolbar(self, title)

        # Actions
        show_info_action = self.create_action(
            CustomToolbarActions.ShowInfo,
            text=_('Show info'),
            tip=_('Show some information to the user'),
            icon=self.create_icon('MessageBoxInformation'),
            triggered=self.show_info_message,
        )

        show_warning_action = self.create_action(
            CustomToolbarActions.ShowWarning,
            text=_('Show warning'),
            tip=_('Show a warning to the user'),
            icon=self.create_icon('MessageBoxWarning'),
            triggered=self.show_warning_message,
        )

        # Add actions to toolbar
        self.add_item_to_toolbar(
            show_info_action,
            self.toolbar,
            section=CustomToolbarSections.First,
        )

        self.add_item_to_toolbar(
            show_warning_action,
            self.toolbar,
            section=CustomToolbarSections.Second,
        )

    def update_actions(self):
        pass

    # ---- API
    # ------------------------------------------------------------------------
    def show_info_message(self):
        """A simple information message."""
        QMessageBox.information(
            self,  # Parent
            _("Information"),  # Window title
            _("You did great by clicking on this button!"),  # Message
            QMessageBox.Ok  # Buttons
        )

    def show_warning_message(self):
        """A simple warning message."""
        QMessageBox.warning(
            self,  # Parent
            _("Warning"),  # Window title
            _("You shouldn't click this button :-p"),  # Message
            QMessageBox.Ok  # Buttons
        )

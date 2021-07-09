# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Spyder Bot
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------

"""
Status bar widgets.
"""

# Third-party imports
from qtpy.QtCore import Signal, Slot
from qtpy.QtWidgets import QComboBox

# Spyder imports
from spyder.api.config.decorators import on_conf_change
from spyder.api.translations import get_translation
from spyder.api.widgets.status import StatusBarWidget


# Localization
_ = get_translation("status_bar_widgets.spyder")


# ---- Constants
class StatusbarWidgets:
    ThemeStatus = 'theme-status'
    PlainFontSizeStatus = 'combobox-status'


# ---- Theme widget
class ThemeStatusWidget(StatusBarWidget):
    """
    Widget to display the current syntax highlighting theme.

    Notes
    -----
    * Status bar widgets need to inherit from StatusBarWidget or
      BaseTimerStatus.
    * See container.py to check how its label is updated and plugin.py
      to see how it's registered in the status bar.
    """

    ID = StatusbarWidgets.ThemeStatus


# ---- Font size widget
class PlainFontSizeComboBox(QComboBox):

    def __init__(self, parent):
        super().__init__(parent)

        # Add some font sizes to choose from.
        self.addItems([str(i) for i in range(9, 16)])


class PlainFontSizeStatus(StatusBarWidget):

    ID = StatusbarWidgets.PlainFontSizeStatus
    CUSTOM_WIDGET_CLASS = PlainFontSizeComboBox

    sig_size_change_requested = Signal(int)
    """
    This is signal is emitted to request for a plain text font size
    change in Spyder.

    Parameters
    ----------
    font_size: int
        New font size (in pixels).
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.custom_widget.currentTextChanged.connect(self.set_size)

    def set_current_size(self, size):
        """Set current font size in combobox."""

        # The value that comes from Spyder config system is an int, but
        # the combobox only accepts strings.
        size = str(size)

        # Add size to combobox in case it's not present among items
        if self.custom_widget.findText(size) == -1:
            self.custom_widget.addItem(size)

        # Set size as default value
        index = self.custom_widget.findText(size)
        self.custom_widget.setCurrentIndex(index)

    @Slot(str)
    def set_size(self, value):
        """
        Set selected size in combobox in Spyder config system and
        request a change.
        """
        # In Spyder this is an int, not a string.
        value = int(value)

        # *Note*: This should be as simple as setting the new font size and
        # seeing the changes happen in Spyder. Unfortunately, that's not the
        # way it's working right now, but it will be in Spyder 5.1.0.
        # For now we have to emit a signal and handle the update manually at
        # the plugin level.
        self.set_conf(section='appearance', option='font/size', value=value)
        self.sig_size_change_requested.emit(value)

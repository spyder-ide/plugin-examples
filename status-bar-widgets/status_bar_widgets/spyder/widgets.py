# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Spyder Bot
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------

"""
Status bar widgets.
"""

# Spyder imports
from spyder.api.config.decorators import on_conf_change
from spyder.api.translations import get_translation
from spyder.api.widgets.status import StatusBarWidget


# Localization
_ = get_translation("status_bar_widgets.spyder")


class StatusbarWidgets:
    ThemeStatus = 'theme-status'


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

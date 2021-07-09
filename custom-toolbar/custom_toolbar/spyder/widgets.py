# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Spyder Bot
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------

"""
Custom toolbar widgets.
"""

# Spyder imports
from spyder.api.widgets.toolbars import ApplicationToolbar


# ---- Widgets
# ----------------------------------------------------------------------------
class CustomToolbar(ApplicationToolbar):
    """Custom toolbar to add to the main application."""

    ID = 'custom_toolbar'

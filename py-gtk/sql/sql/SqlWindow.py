# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('sql')

from sql_lib import Window
from sql.AboutSqlDialog import AboutSqlDialog
from sql.PreferencesSqlDialog import PreferencesSqlDialog

# See sql_lib.Window.py for more details about how this class works
class SqlWindow(Window):
    __gtype_name__ = "SqlWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(SqlWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutSqlDialog
        self.PreferencesDialog = PreferencesSqlDialog

        # Code for other initialization actions should be added here.


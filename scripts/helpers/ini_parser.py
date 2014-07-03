# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#  This file is part of Wrye Bash.
#
#  Wrye Bash is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  Wrye Bash is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Wrye Bash; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#  Wrye Bash copyright (C) 2005-2009 Wrye, 2010-2014 Wrye Bash Team
#  https://github.com/wrye-bash
#
# =============================================================================

"""This module parses the ini file containing info used from the scripts"""

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('values.ini')

def current_oblivion_thread():
    return config.getint('Threads', 'current_oblivion_thread')

def current_skyrim_thread():
    return config.getint('Threads', 'current_skyrim_thread')

def previous_oblivion_thread():
    return config.getint('Threads', 'previous_oblivion_thread')

def previous_skyrim_thread():
    return config.getint('Threads', 'previous_skyrim_thread')

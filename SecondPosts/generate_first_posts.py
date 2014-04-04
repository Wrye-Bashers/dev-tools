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

"""This module generates the first posts for the Bethesda forums threads."""

from generate_changelog import writeChangelog
from globals import _template, Parser, _outFile, hub

# Functions ===================================================================
def _parseArgs():
    return Parser.new(prog='Wrye Bash Version History.html').user().milestone(
        help_='Specify the milestone for latest release.').editor().parse()

import shutil
import os.path
import subprocess

class _Game(object):
    def __init__(self, display, nexusUrl, prev_thread, cur_thread):
        self.display = display
        self.nexusUrl = nexusUrl
        self.prev_thread = prev_thread
        self.cur_thread = cur_thread

OBLIVION = _Game(u'Oblivion', u'[url=http://www.nexusmods'
                              u'.com/oblivion/mods/22368]Oblivion Nexus[/url]',
                 prev_thread=1471926, cur_thread=1482255)
SKYRIM = _Game(u'Skyrim', u'[url=http://www.nexusmods'
                          u'.com/skyrim/mods/1840]Skyrim Nexus[/url]',
               prev_thread=1485637, cur_thread=1497553)
_GAMES = {'oblivion': OBLIVION, 'skyrim': SKYRIM}

POSTS_DIR = '../FirstPosts'
TEMPLATE = _template(name=u'generate_first_posts_lines.txt')

def _previous_thread(num):
    return 'Continuing from the [topic=' + str(
        num) + ']previous thread[/topic]...'

def _thread_history(game):
    if game == 'skyrim':
        with open(_template(name="Thread History.txt"), "r") as threads:
            return threads.read()

def _other_threads(game):
    for _g, g in _GAMES:
        if g != game:
            yield '\n'.join('[*]The Official [topic=' + str(g.cur_thread) +
                            ']Wrye Bash for ' + g.display +
                            ' thread[/topic].[/*]')

def writeFirstPosts(repo, milestone, editor):
    for label, game in _GAMES.iteritems():
        out_ = _outFile(dir_=POSTS_DIR,
                        name=u'Forum thread starter - ' + game.display +
                             u'.txt')
        with open(out_, 'wb') as out:
            out.write(_previous_thread(
                game.prev_thread))  # TODO ask user and/or command line args
            out.write('\n\n')
            history = _thread_history(label)
            if history:
                out.write(history)
                out.write('\n\n')
            with open(TEMPLATE, 'r') as template:
                data = template.read()
            out.write(data % {'game': game.display,
                                  'nexus_url': game.nexusUrl,
                                  'game_threads': _other_threads(game),
                                  'latest_changelog': writeChangelog(repo,
                                                                     milestone)})
            #     if editor:
            #         print('Please review the changelog (mind the
            # date): ' + str(
            #             latestChangelog))
            #         subprocess.call(
            #             [editor, str(latestChangelog)])  # TODO
            # call_check

def main():
    opts = _parseArgs()
    if opts.no_editor:
        editor = None
    else:
        editor = opts.editor
    git_ = hub(opts)
    if not git_: return
    repo, milestone = git_[0], git_[1]
    writeFirstPosts(repo, milestone, editor)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "Aborted"

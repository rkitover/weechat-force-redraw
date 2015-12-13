# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Rafael Kitover <rkitover@gmail.com>
#
# Version History:
#
# 0.1: 10/28/2014
#   * initial release
#
# License (BSD 2-clause):
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

SCRIPT_NAME    = "force_redraw"
SCRIPT_AUTHOR  = "Caelum <rkitover@gmail.com>"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "BSD"
SCRIPT_DESC    = "redraw screen on every new line"

try:
    import weechat
except:
    print("This script must be run under WeeChat.")
    print("Get WeeChat now at: http://www.weechat.org/")
    quit()

import re

weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", "")

def force_redraw(data, modifier, modifier_data, string):
    plugin, buffer_name = re.match('([^;]+);([^;]+)', modifier_data).group(1, 2)

    if weechat.buffer_get_integer(weechat.buffer_search(plugin, buffer_name), 'num_displayed') > 0:
        weechat.command(weechat.current_buffer(), '/window refresh')

    return string

weechat.hook_modifier("weechat_print", "force_redraw", "")

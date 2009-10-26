#                                            -*- coding: utf-8 -*-
# Copyright (c) 2009  Chunlin Yao
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the project nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#
from pyeb import *

if __name__ == "__main__":
    import re, sys
    if len(sys.argv) < 3:
        sys.exit("main.py book word")
    from gaiji import gaijimap
    def text_hook_wide_font(book, appendix, container, hook_code, argc, argv):
        eb.eb_write_text_string(book, (u"[z%04X]" % argv.contents.value).encode("euc-jp"))
        return EB_SUCCESS

    def text_hook_narrow_font(book, appendix, container, hook_code, argc, argv):
        eb.eb_write_text_string(book, (u"[z%04X]" % argv.contents.value).encode("euc-jp"))
        return EB_SUCCESS

    def replaceGaiji(orig):
        r = re.compile("\[(?P<gaiji>z[0-9A-F]{4})\]")
        return r.sub(lambda m: gaijimap[m.group("gaiji")], orig)

    MAX_HITS = 50
    MAXLEN_HEADING = 1024 * 1024
    error_code = 0
    book = EB_Book()
    subbook_list = (c_int * EB_MAX_SUBBOOKS)()
    hits = (EB_Hint * MAX_HITS)()
    heading = (c_char * MAXLEN_HEADING)()
    heading_length = c_size_t()
    subbook_count = c_int()
    hit_count = c_int()

    hookset = EB_Hookset()

    eb.eb_initialize_library()
    eb.eb_initialize_book(byref(book))
    eb.eb_initialize_hookset(byref(hookset))

    wide_font_hook = EB_Hook(code=EB_HOOK_WIDE_FONT, function=HOOKFUNC(text_hook_wide_font))
    narrow_font_hook = EB_Hook(code=EB_HOOK_NARROW_FONT, function=HOOKFUNC(text_hook_narrow_font))

    eb.eb_set_hook(byref(hookset), byref(wide_font_hook))
    eb.eb_set_hook(byref(hookset), byref(narrow_font_hook))

    error_code = eb.eb_bind(byref(book),sys.argv[1])

    if error_code != EB_SUCCESS:
        print eb.eb_error_message(error_code)
        close_dict(book, hookset)

    error_code = eb.eb_subbook_list(byref(book), subbook_list, byref(subbook_count));
    if error_code != EB_SUCCESS:
        print eb.eb_error_message(error_code)
        close_dict(book, hookset)

    subbook_index = 0
    error_code = eb.eb_set_subbook(byref(book), subbook_list[subbook_index]);
    if error_code != EB_SUCCESS:
        print eb.eb_error_message(error_code)
        close_dict(book, hookset)

    error_code = eb.eb_search_word(byref(book), unicode(sys.argv[2],"cp932").encode("euc-jp"));
    if error_code != EB_SUCCESS:
        print eb.eb_error_message(error_code)
        close_dict(book, hookset)
    
    error_code = eb.eb_hit_list(byref(book), MAX_HITS, hits, byref(hit_count));
    if error_code != EB_SUCCESS:
        print eb.eb_error_message(error_code)
        close_dict(book, hookset)
    while hit_count.value > 0:
        for i in range(hit_count.value):
            error_code = eb.eb_seek_text(byref(book), byref(hits[i].heading));
            if error_code != EB_SUCCESS:
                print eb.eb_error_message(error_code)
                close_dict(book, hookset)
            error_code = eb.eb_read_heading(byref(book), None, byref(hookset), None, 
                    MAXLEN_HEADING, heading, byref(heading_length));
            if error_code != EB_SUCCESS:
                print eb.eb_error_message(error_code)
                close_dict(book, hookset)
            print replaceGaiji(unicode(heading.value, "euc-jp")).encode("utf-8")
            print "----------------------------"

            #TEXT
            error_code = eb.eb_seek_text(byref(book), byref(hits[i].text));
            if error_code != EB_SUCCESS:
                print eb.eb_error_message(error_code)
                close_dict(book, hookset)
            error_code = eb.eb_read_text(byref(book), None, byref(hookset), None, 
                    MAXLEN_HEADING, heading, byref(heading_length));
            if error_code != EB_SUCCESS:
                print eb.eb_error_message(error_code)
                close_dict(book, hookset)
            print replaceGaiji(unicode(heading.value, "euc-jp")).encode("utf-8")
        error_code = eb.eb_hit_list(byref(book), MAX_HITS, hits, byref(hit_count));
        if error_code != EB_SUCCESS:
            print eb.eb_error_message(error_code)
            close_dict(book, hookset)
    close_dict(book, hookset)
    

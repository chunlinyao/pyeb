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


from ctypes import *
eb = cdll.LoadLibrary("eb.dll")

#
# Disc code
#
EB_DISC_EB		 =0
EB_DISC_EPWING		 =1
EB_DISC_INVALID		 =-1

#
# Character codes.
#
EB_CHARCODE_ISO8859_1	 =1
EB_CHARCODE_JISX0208	 =2
EB_CHARCODE_JISX0208_GB2312 =3
EB_CHARCODE_INVALID	 =-1

#
# Special book ID for cache to represent "no cache data for any book".
#
EB_BOOK_NONE		 =-1

#
# Special disc code, subbook code, multi search ID, and multi search
# entry ID, for representing error state.
#
EB_SUBBOOK_INVALID	 =-1
EB_MULTI_INVALID	 =-1

#
# Size of a page (The term `page' means `block' in JIS X 4081).
#
EB_SIZE_PAGE		 =2048

#
# Maximum length of a word to be searched.
#
EB_MAX_WORD_LENGTH             =255

#
# Maximum length of an EB* book title.
#
EB_MAX_EB_TITLE_LENGTH	 =30

#
# Maximum length of an EPWING book title.
#
EB_MAX_EPWING_TITLE_LENGTH =80

#
# Maximum length of a book title.
#
EB_MAX_TITLE_LENGTH	 =80

#
# Maximum length of a word to be searched.
# TODO what is the PATH_MAX about eb.dll 4.2.2 on windows??
#if defined(PATH_MAX)
#EB_MAX_PATH_LENGTH	 =PATH_MAX
#elif defined(MAXPATHLEN)
#EB_MAX_PATH_LENGTH	 =MAXPATHLEN
#else
#EB_MAX_PATH_LENGTH	 =1024
#endif
EB_MAX_PATH_LENGTH = 260 -1
#
# Maximum length of a directory name.
#
EB_MAX_DIRECTORY_NAME_LENGTH =8

#
# Maximum length of a file name under a certain directory.
# prefix(8 chars) + '.' + suffix(3 chars) + ';' + digit(1 char)
#
EB_MAX_FILE_NAME_LENGTH	 =14

#
# Maximum length of a label for multi-search entry.
#
EB_MAX_MULTI_LABEL_LENGTH =30

#
# Maximum length of alternation text string for a private character.
#
EB_MAX_ALTERNATION_TEXT_LENGTH =31

#
# Maximum length of title for multi search.
#
EB_MAX_MULTI_TITLE_LENGTH =32

#
# Maximum number of font heights in a subbok.
#
EB_MAX_FONTS		 =4

#
# Maximum number of subbooks in a book.
#
EB_MAX_SUBBOOKS		 =50

#
# Maximum number of multi-search types in a subbook.
#
EB_MAX_MULTI_SEARCHES	 =10

#
# Maximum number of entries in a multi-search.
#
EB_MAX_MULTI_ENTRIES	 =5

#
# Maximum number of entries in a keyword search.
#
EB_MAX_KEYWORDS		 =EB_MAX_MULTI_ENTRIES

#
# Maximum number of entries in a cross search.
#
EB_MAX_CROSS_ENTRIES	 =EB_MAX_MULTI_ENTRIES

#
# Maximum number of characters for alternation cache.
#
EB_MAX_ALTERNATION_CACHE =16

#
# The number of text hooks.
#
EB_NUMBER_OF_HOOKS	 =45

#
# The number of search contexts required by a book.
#
EB_NUMBER_OF_SEARCH_CONTEXTS =EB_MAX_MULTI_ENTRIES

EB_SIZE_BINARY_CACHE_BUFFER	= 128
EB_HOOK_NULL			=-1
EB_HOOK_INITIALIZE		=0
EB_HOOK_BEGIN_NARROW		=1
EB_HOOK_END_NARROW		=2
EB_HOOK_BEGIN_SUBSCRIPT		=3
EB_HOOK_END_SUBSCRIPT		=4

EB_HOOK_SET_INDENT		=5
EB_HOOK_NEWLINE			=6
EB_HOOK_BEGIN_SUPERSCRIPT	=7
EB_HOOK_END_SUPERSCRIPT		=8
EB_HOOK_BEGIN_NO_NEWLINE	=9

EB_HOOK_END_NO_NEWLINE		=10
EB_HOOK_BEGIN_EMPHASIS		=11
EB_HOOK_END_EMPHASIS		=12
EB_HOOK_BEGIN_CANDIDATE		=13
EB_HOOK_END_CANDIDATE_GROUP	=14

EB_HOOK_END_CANDIDATE_LEAF	=15
EB_HOOK_BEGIN_REFERENCE		=16
EB_HOOK_END_REFERENCE		=17
EB_HOOK_BEGIN_KEYWORD		=18
EB_HOOK_END_KEYWORD		=19

EB_HOOK_NARROW_FONT		=20
EB_HOOK_WIDE_FONT		=21
EB_HOOK_ISO8859_1		=22
EB_HOOK_NARROW_JISX0208		=23
EB_HOOK_WIDE_JISX0208		=24

EB_HOOK_GB2312			=25
EB_HOOK_BEGIN_MONO_GRAPHIC	=26
EB_HOOK_END_MONO_GRAPHIC	=27
EB_HOOK_BEGIN_GRAY_GRAPHIC	=28
EB_HOOK_END_GRAY_GRAPHIC	=29

EB_HOOK_BEGIN_COLOR_BMP		=30
EB_HOOK_BEGIN_COLOR_JPEG	=31
EB_HOOK_BEGIN_IN_COLOR_BMP	=32
EB_HOOK_BEGIN_IN_COLOR_JPEG	=33
EB_HOOK_END_COLOR_GRAPHIC	=34

EB_HOOK_END_IN_COLOR_GRAPHIC	=35
EB_HOOK_BEGIN_WAVE		=36
EB_HOOK_END_WAVE		=37
EB_HOOK_BEGIN_MPEG		=38
EB_HOOK_END_MPEG		=39

EB_HOOK_BEGIN_GRAPHIC_REFERENCE	=40
EB_HOOK_END_GRAPHIC_REFERENCE	=41
EB_HOOK_GRAPHIC_REFERENCE	=42
EB_HOOK_BEGIN_DECORATION	=43
EB_HOOK_END_DECORATION		=44
################
# FOR WIN
c_off_t = c_long
################

class EB_Position(Structure):
    _fields_ = [('page', c_int),
            ('offset', c_int),
            ]

class EB_Binary_Context(Structure):
    _fields_ = [('code', c_int),
            #('zio', POINTER(Zio)),
            ('zio', c_void_p),
            ('location', c_off_t),
            ('size', c_size_t),
            ('offset', c_size_t),
            ('cache_buffer', c_char * EB_SIZE_BINARY_CACHE_BUFFER),
            ('cache_length', c_size_t),
            ('cache_offset', c_size_t),
            ('width', c_int),

            ]

class EB_Text_Context(Structure):
    _fields_ = [('code', c_int),
            ('location', c_off_t),
            ('out', c_char_p),
            ('out_rest_length', c_size_t),
            ('unprocessed', c_char_p),
            ('unprocessed_size', c_size_t),
            ('out_step', c_size_t),
            ('narrow_flag', c_int),
            ('printable_count', c_int),
            ('file_end_flag', c_int),
            ('text_status', c_int),
            ('skip_code', c_int),
            ('auto_stop_code', c_int),
            ('candidate', c_char * (EB_MAX_WORD_LENGTH + 1)),
            ('is_candidate', c_int),

            ]

class EB_Search_Context(Structure):
    _fields_ = [('code', c_int),
            ('compare_pre', c_void_p), #func
            ('compare_single', c_void_p), #func
            ('compare_group', c_void_p), #func
            ('comparison_result', c_int),
            ('word', c_char * (EB_MAX_WORD_LENGTH + 1)),
            ('canonicalized_word', c_char * (EB_MAX_WORD_LENGTH + 1)),
            ('page', c_int),
            ('offset', c_int),
            ('page_id', c_int),
            ('entry_count', c_int),
            ('entry_index', c_int),
            ('entry_length', c_int),
            ('entry_arrangement', c_int),
            ('in_group_entry', c_int),
            ('keyword_heading', EB_Position),

            ]

#class EB_Subbook(Structure):
#    _fields_ = [('initialized', c_int),
#            ('index_page', c_int),
#            ('code', c_int),
#            ('text_zio', Zio),
#            ('graphic_zio', Zio),
#            ('sound_zio', Zio),
#            ('movie_zio', Zio),
#            ('title', c_char * (EB_MAX_TITLE_LENGTH + 1)),
#            ('directory_name', c_char * (EB_MAX_DIRECTORY_NAME_LENGTH + 1)),
#            ('data_directory_name', c_char * (EB_MAX_DIRECTORY_NAME_LENGTH + 1)),
#            ('gaiji_directory_name', c_char * (EB_MAX_DIRECTORY_NAME_LENGTH + 1)),
#            ('movie_directory_name', c_char * (EB_MAX_DIRECTORY_NAME_LENGTH + 1)),
#            ('text_file_name', c_char * (EB_MAX_FILE_NAME_LENGTH + 1)),
#            ('graphic_file_name', c_char * (EB_MAX_FILE_NAME_LENGTH + 1)),
#            ('sound_file_name', c_char * (EB_MAX_FILE_NAME_LENGTH + 1)),
#            ('text_hint_zio_code', c_int),
#            ('graphic_hint_zio_code', c_int),
#            ('sound_hint_zio_code', c_int),
#            ('search_title_page', c_int),
#            ('word_alphabet', EB_Search),
#            ('word_asis', EB_Search),
#            ('word_kana', EB_Search),
#            ('endword_alphabet', EB_Search),
#            ('endword_asis', EB_Search),
#            ('endword_kana', EB_Search),
#            ('keyword', EB_Search),
#            ('menu', EB_Search),
#            #('image_menu', EB_Search),
#            ('cross', EB_Search),
#            ('copyright', EB_Search),
#            ('text', EB_Search),
#            ('sound', EB_Search),
#            ('multi_count', EB_Search),
#            ('multis', EB_Multi_Search * EB_MAX_MULTI_SEARCHES),
#            ('narrow_fonts', EB_Font * EB_MAX_FONTS),
#            ('wide_fonts', EB_Font * EB_MAX_FONTS),
#            ('narrow_current', POINTER(EB_Font)),
#            ('wide_current', POINTER(EB_Font)),
#            ]

class EB_Book(Structure):
    _fields_ = [('code', c_int),
            ('disc_code', c_int),
            ('character_code', c_int),
            ('path', c_char_p),
            ('path_length', c_size_t),
            ('subbook_count', c_int),
            #('subbooks', POINTER(EB_Subbook)),
            ('subbooks', c_void_p),
            #('subbook_current', POINTER(EB_Subbook)),
            ('subbook_current', c_void_p),
            ('text_context', EB_Text_Context),
            ('binary_context', EB_Binary_Context),
            ('search_contexts', EB_Search_Context * EB_NUMBER_OF_SEARCH_CONTEXTS),
            ]

HOOKFUNC = CFUNCTYPE(c_int, POINTER(EB_Book), c_void_p, c_void_p,
        c_int, c_int, POINTER(c_uint))

class EB_Hook(Structure):
    _fields_ = [('code', c_int),
            ('function', HOOKFUNC)
            ]

class EB_Hint(Structure):
    _fields_ = [('heading', EB_Position),
            ('text', EB_Position),
            ]


class EB_Hookset(Structure):
    _fields_ = [('hooks', EB_Hook * EB_NUMBER_OF_HOOKS),
            ]

EB_SUCCESS = 0


def close_dict(book, hookset):
    import sys
    eb.eb_finalize_book(byref(book))
    eb.eb_finalize_library()
    eb.eb_finalize_hookset(byref(hookset))
    sys.exit()




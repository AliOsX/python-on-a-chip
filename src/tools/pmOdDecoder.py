#!/usr/bin/env python

# This file is Copyright 2009 Dean Hall.
# This file is part of the Python-on-a-Chip tools.
# This software is licensed under the MIT License.
# See the LICENSE file for details.

"""
PyMite Object Descriptor Decoder
================================

Decodes an object descriptor value into its bit fields.
"""

## @file
#  @copybrief pmOldDecoder

## @package pmOldDecoder
#  @brief PyMite Object Descriptor Decoder
#
#  Decodes an object descriptor value into its bit fields.


import sys


__usage__ = """USAGE:
    ./pmOdDecoder.py odvalue
"""


TYPES = (
    'OBJ_TYPE_NON',
    'OBJ_TYPE_INT',
    'OBJ_TYPE_FLT',
    'OBJ_TYPE_STR',
    'OBJ_TYPE_TUP',
    'OBJ_TYPE_COB',
    'OBJ_TYPE_MOD',
    'OBJ_TYPE_CLO',
    'OBJ_TYPE_FXN',
    'OBJ_TYPE_CLI',
    'OBJ_TYPE_CIM',
    'OBJ_TYPE_NIM',
    'OBJ_TYPE_NOB',
    'OBJ_TYPE_THR',
    0x0E,
    'OBJ_TYPE_BOOL',
    'OBJ_TYPE_CIO',
    'OBJ_TYPE_MTH',
    'OBJ_TYPE_LST',
    'OBJ_TYPE_DIC',
    0x14,0x15,0x16,0x17,0x18,
    'OBJ_TYPE_FRM',
    'OBJ_TYPE_BLK',
    'OBJ_TYPE_SEG',
    'OBJ_TYPE_SGL',
    'OBJ_TYPE_SQI',
    'OBJ_TYPE_NFM',
)


def od_decode(odvalue):
    if odvalue & 0x0002:
        return {
        "val": odvalue,
        "size": odvalue & 0xFFFC,
        "type": "free",
        "free": (odvalue & 0x0002) >> 1,
        "mark": odvalue & 0x0001, # Reserved bit
        }
    
    return {
        "val": odvalue,
        "size": odvalue & 0x07FC,
        "type": TYPES[(odvalue & 0xF800) >> 11],
        "free": (odvalue & 0x0002) >> 1,
        "mark": odvalue & 0x0001,
    }


def to_int(s):
    if s.startswith("0x"):
        return int(s, 16)
    return int(s)


def print_od(od):
    print("%(val)d (0x%(val)04x): %(type)s[%(size)d], f=%(free)d, m=%(mark)d"
          % od)


def main():
    odvalues = sys.argv[1:]
    odvalues = map(to_int, odvalues)
    ods = map(od_decode, odvalues)
    map(print_od, ods)


if __name__ == "__main__":
    main()

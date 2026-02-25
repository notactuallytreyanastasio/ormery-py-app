from temper_std.json import JsonAdapter, JsonProducer, JsonSyntaxTree, InterchangeContext, JsonString
from datetime import date as date67
from builtins import str as str15, int as int20, bool as bool13, list as list2, len as len5
from temper_core import cast_by_type as cast_by_type56, date_to_string as date_to_string63, date_from_iso_string as date_from_iso_string64, arith_int_mod as arith_int_mod65, int_to_string as int_to_string8, string_get as string_get6, string_next as string_next9, string_count_between as string_count_between66, int_sub as int_sub22
from typing import Sequence as Sequence17
from temper_std.json import JsonAdapter, JsonString
date_to_string_2599 = date_to_string63
date_from_iso_string_2600 = date_from_iso_string64
arith_int_mod_2601 = arith_int_mod65
int_to_string_2602 = int_to_string8
len_2603 = len5
string_get_2604 = string_get6
string_next_2606 = string_next9
string_count_between_2607 = string_count_between66
int_sub_2608 = int_sub22
class DateJsonAdapter_109(JsonAdapter['date67']):
    __slots__ = ()
    def encode_to_json(this_120, x_116: 'date67', p_117: 'JsonProducer') -> 'None':
        encode_to_json_90(x_116, p_117)
    def decode_from_json(this_121, t_118: 'JsonSyntaxTree', ic_119: 'InterchangeContext') -> 'date67':
        return decode_from_json_93(t_118, ic_119)
    def __init__(this_122) -> None:
        pass
# Type `std/temporal/`.Date connected to datetime.date
def encode_to_json_90(this_20: 'date67', p_91: 'JsonProducer') -> 'None':
    t_313: 'str15' = date_to_string_2599(this_20)
    p_91.string_value(t_313)
def decode_from_json_93(t_94: 'JsonSyntaxTree', ic_95: 'InterchangeContext') -> 'date67':
    t_190: 'JsonString'
    t_190 = cast_by_type56(t_94, JsonString)
    return date_from_iso_string_2600(t_190.content)
def json_adapter_124() -> 'JsonAdapter[date67]':
    return DateJsonAdapter_109()
days_in_month_34: 'Sequence17[int20]' = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
def is_leap_year_32(year_41: 'int20') -> 'bool13':
    return_21: 'bool13'
    t_263: 'int20'
    if arith_int_mod_2601(year_41, 4) == 0:
        if arith_int_mod_2601(year_41, 100) != 0:
            return_21 = True
        else:
            t_263 = arith_int_mod_2601(year_41, 400)
            return_21 = t_263 == 0
    else:
        return_21 = False
    return return_21
def pad_to_33(min_width_43: 'int20', num_44: 'int20', sb_45: 'list2[str15]') -> 'None':
    "If the decimal representation of \\|num\\| is longer than [minWidth],\nthen appends that representation.\nOtherwise any sign for [num] followed by enough zeroes to bring the\nwhole length up to [minWidth].\n\n```temper\n// When the width is greater than the decimal's length,\n// we pad to that width.\n\"0123\" == do {\n  let sb = new StringBuilder();\n  padTo(4, 123, sb);\n  sb.toString()\n}\n\n// When the width is the same or lesser, we just use the string form.\n\"123\" == do {\n  let sb = new StringBuilder();\n  padTo(2, 123, sb);\n  sb.toString()\n}\n\n// The sign is always on the left.\n\"-01\" == do {\n  let sb = new StringBuilder();\n  padTo(3, -1, sb);\n  sb.toString()\n}\n```\n\nminWidth__43: Int32\n\nnum__44: Int32\n\nsb__45: builtins.list<String>\n"
    t_346: 'int20'
    t_348: 'int20'
    t_257: 'bool13'
    decimal_47: 'str15' = int_to_string_2602(num_44, 10)
    decimal_index_48: 'int20' = 0
    decimal_end_49: 'int20' = len_2603(decimal_47)
    if decimal_index_48 < decimal_end_49:
        t_346 = string_get_2604(decimal_47, decimal_index_48)
        t_257 = t_346 == 45
    else:
        t_257 = False
    if t_257:
        sb_45.append('-')
        t_348 = string_next_2606(decimal_47, decimal_index_48)
        decimal_index_48 = t_348
    t_349: 'int20' = string_count_between_2607(decimal_47, decimal_index_48, decimal_end_49)
    n_needed_50: 'int20' = int_sub_2608(min_width_43, t_349)
    while n_needed_50 > 0:
        sb_45.append('0')
        n_needed_50 = int_sub_2608(n_needed_50, 1)
    sb_45.append(decimal_47[decimal_index_48 : decimal_end_49])
day_of_week_lookup_table_leapy_35: 'Sequence17[int20]' = (0, 0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6)
day_of_week_lookup_table_not_leapy_36: 'Sequence17[int20]' = (0, 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5)

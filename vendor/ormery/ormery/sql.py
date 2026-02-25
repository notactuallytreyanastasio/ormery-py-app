from typing import MutableSequence as MutableSequence12, Sequence as Sequence14, Any as Any18, TypeVar as TypeVar19, Callable as Callable20
from builtins import str as str13, bool as bool15, float as float16, int as int17, list as list5, RuntimeError as RuntimeError22, len as len1, tuple as tuple4
from datetime import date as date11
from abc import ABCMeta as ABCMeta21
from temper_core import string_from_code_point as string_from_code_point23, list_builder_add_all as list_builder_add_all0, list_get as list_get2, int_add as int_add3, date_to_string as date_to_string6, string_for_each as string_for_each7, float64_to_string as float64_to_string8, int_to_string as int_to_string9, str_cat as str_cat10
list_builder_add_all_5760 = list_builder_add_all0
len_5761 = len1
list_get_5762 = list_get2
int_add_5763 = int_add3
tuple_5764 = tuple4
list_5765 = list5
date_to_string_5769 = date_to_string6
string_for_each_5771 = string_for_each7
float64_to_string_5772 = float64_to_string8
int_to_string_5773 = int_to_string9
str_cat_5774 = str_cat10
date_5775 = date11
T_27 = TypeVar19('T_27', bound = Any18)
class SqlBuilder:
    buffer_94: 'MutableSequence12[SqlPart]'
    __slots__ = ('buffer_94',)
    def append_safe(this_9, sql_source_96: 'str13') -> 'None':
        t_1163: 'SqlSource' = SqlSource(sql_source_96)
        this_9.buffer_94.append(t_1163)
    def append_fragment(this_10, fragment_99: 'SqlFragment') -> 'None':
        t_1161: 'Sequence14[SqlPart]' = fragment_99.parts
        list_builder_add_all_5760(this_10.buffer_94, t_1161)
    def append_part(this_11, part_102: 'SqlPart') -> 'None':
        this_11.buffer_94.append(part_102)
    def append_part_list(this_12, values_105: 'Sequence14[SqlPart]') -> 'None':
        def fn_1157(x_107: 'SqlPart') -> 'None':
            this_12.append_part(x_107)
        this_12.append_list_150(values_105, fn_1157)
    def append_boolean(this_13, value_109: 'bool15') -> 'None':
        t_1154: 'SqlBoolean' = SqlBoolean(value_109)
        this_13.buffer_94.append(t_1154)
    def append_boolean_list(this_14, values_112: 'Sequence14[bool15]') -> 'None':
        def fn_1151(x_114: 'bool15') -> 'None':
            this_14.append_boolean(x_114)
        this_14.append_list_150(values_112, fn_1151)
    def append_date(this_15, value_116: 'date11') -> 'None':
        t_1148: 'SqlDate' = SqlDate(value_116)
        this_15.buffer_94.append(t_1148)
    def append_date_list(this_16, values_119: 'Sequence14[date11]') -> 'None':
        def fn_1145(x_121: 'date11') -> 'None':
            this_16.append_date(x_121)
        this_16.append_list_150(values_119, fn_1145)
    def append_float64(this_17, value_123: 'float16') -> 'None':
        t_1142: 'SqlFloat64' = SqlFloat64(value_123)
        this_17.buffer_94.append(t_1142)
    def append_float64_list(this_18, values_126: 'Sequence14[float16]') -> 'None':
        def fn_1139(x_128: 'float16') -> 'None':
            this_18.append_float64(x_128)
        this_18.append_list_150(values_126, fn_1139)
    def append_int32(this_19, value_130: 'int17') -> 'None':
        t_1136: 'SqlInt32' = SqlInt32(value_130)
        this_19.buffer_94.append(t_1136)
    def append_int32_list(this_20, values_133: 'Sequence14[int17]') -> 'None':
        def fn_1133(x_135: 'int17') -> 'None':
            this_20.append_int32(x_135)
        this_20.append_list_150(values_133, fn_1133)
    def append_int64(this_21, value_137: 'int64_21') -> 'None':
        t_1130: 'SqlInt64' = SqlInt64(value_137)
        this_21.buffer_94.append(t_1130)
    def append_int64_list(this_22, values_140: 'Sequence14[int64_21]') -> 'None':
        def fn_1127(x_142: 'int64_21') -> 'None':
            this_22.append_int64(x_142)
        this_22.append_list_150(values_140, fn_1127)
    def append_string(this_23, value_144: 'str13') -> 'None':
        t_1124: 'SqlString' = SqlString(value_144)
        this_23.buffer_94.append(t_1124)
    def append_string_list(this_24, values_147: 'Sequence14[str13]') -> 'None':
        def fn_1121(x_149: 'str13') -> 'None':
            this_24.append_string(x_149)
        this_24.append_list_150(values_147, fn_1121)
    def append_list_150(this_25, values_151: 'Sequence14[T_27]', append_value_152: 'Callable20[[T_27], None]') -> 'None':
        t_1116: 'int17'
        t_1118: 'T_27'
        i_154: 'int17' = 0
        while True:
            t_1116 = len_5761(values_151)
            if not i_154 < t_1116:
                break
            if i_154 > 0:
                this_25.append_safe(', ')
            t_1118 = list_get_5762(values_151, i_154)
            append_value_152(t_1118)
            i_154 = int_add_5763(i_154, 1)
    @property
    def accumulated(this_26) -> 'SqlFragment':
        return SqlFragment(tuple_5764(this_26.buffer_94))
    def __init__(this_42) -> None:
        t_1113: 'MutableSequence12[SqlPart]' = list_5765()
        this_42.buffer_94 = t_1113
class SqlFragment:
    parts_161: 'Sequence14[SqlPart]'
    __slots__ = ('parts_161',)
    def to_source(this_31) -> 'SqlSource':
        return SqlSource(this_31.to_string())
    def to_string(this_32) -> 'str13':
        t_1186: 'int17'
        builder_166: 'list5[str13]' = ['']
        i_167: 'int17' = 0
        while True:
            t_1186 = len_5761(this_32.parts_161)
            if not i_167 < t_1186:
                break
            list_get_5762(this_32.parts_161, i_167).format_to(builder_166)
            i_167 = int_add_5763(i_167, 1)
        return ''.join(builder_166)
    def __init__(this_63, parts_169: 'Sequence14[SqlPart]') -> None:
        this_63.parts_161 = parts_169
    @property
    def parts(this_248) -> 'Sequence14[SqlPart]':
        return this_248.parts_161
class SqlPart(metaclass = ABCMeta21):
    def format_to(this_33, builder_171: 'list5[str13]') -> 'None':
        raise RuntimeError22()
class SqlSource(SqlPart):
    "`SqlSource` represents known-safe SQL source code that doesn't need escaped. This\noften originates from the raw string content in `sql`-tagged strings. For\nexample, in `sql\"select p.name from person p where p.id = ${id}\"`, all except\nthe `${id}` interpolation becomes a `SqlSource` instance."
    source_173: 'str13'
    __slots__ = ('source_173',)
    def format_to(this_34, builder_175: 'list5[str13]') -> 'None':
        builder_175.append(this_34.source_173)
    def __init__(this_69, source_178: 'str13') -> None:
        this_69.source_173 = source_178
    @property
    def source(this_245) -> 'str13':
        return this_245.source_173
class SqlBoolean(SqlPart):
    value_179: 'bool15'
    __slots__ = ('value_179',)
    def format_to(this_35, builder_181: 'list5[str13]') -> 'None':
        t_718: 'str13'
        if this_35.value_179:
            t_718 = 'TRUE'
        else:
            t_718 = 'FALSE'
        builder_181.append(t_718)
    def __init__(this_72, value_184: 'bool15') -> None:
        this_72.value_179 = value_184
    @property
    def value(this_251) -> 'bool15':
        return this_251.value_179
class SqlDate(SqlPart):
    value_185: 'date11'
    __slots__ = ('value_185',)
    def format_to(this_36, builder_187: 'list5[str13]') -> 'None':
        builder_187.append("'")
        s_189: 'str13' = date_to_string_5769(this_36.value_185)
        def fn_1178(c_190: 'int17') -> 'None':
            if c_190 == 39:
                builder_187.append("''")
            else:
                builder_187.append(string_from_code_point23(c_190))
        string_for_each_5771(s_189, fn_1178)
        builder_187.append("'")
    def __init__(this_75, value_192: 'date11') -> None:
        this_75.value_185 = value_192
    @property
    def value(this_254) -> 'date11':
        return this_254.value_185
class SqlFloat64(SqlPart):
    value_193: 'float16'
    __slots__ = ('value_193',)
    def format_to(this_37, builder_195: 'list5[str13]') -> 'None':
        t_1175: 'str13' = float64_to_string_5772(this_37.value_193)
        builder_195.append(t_1175)
    def __init__(this_78, value_198: 'float16') -> None:
        this_78.value_193 = value_198
    @property
    def value(this_257) -> 'float16':
        return this_257.value_193
class SqlInt32(SqlPart):
    value_199: 'int17'
    __slots__ = ('value_199',)
    def format_to(this_38, builder_201: 'list5[str13]') -> 'None':
        t_1173: 'str13' = int_to_string_5773(this_38.value_199)
        builder_201.append(t_1173)
    def __init__(this_81, value_204: 'int17') -> None:
        this_81.value_199 = value_204
    @property
    def value(this_260) -> 'int17':
        return this_260.value_199
class SqlInt64(SqlPart):
    value_205: 'int64_21'
    __slots__ = ('value_205',)
    def format_to(this_39, builder_207: 'list5[str13]') -> 'None':
        t_1171: 'str13' = int_to_string_5773(this_39.value_205)
        builder_207.append(t_1171)
    def __init__(this_84, value_210: 'int64_21') -> None:
        this_84.value_205 = value_210
    @property
    def value(this_263) -> 'int64_21':
        return this_263.value_205
class SqlString(SqlPart):
    '`SqlString` represents text data that needs escaped.'
    value_211: 'str13'
    __slots__ = ('value_211',)
    def format_to(this_40, builder_213: 'list5[str13]') -> 'None':
        builder_213.append("'")
        def fn_1166(c_215: 'int17') -> 'None':
            if c_215 == 39:
                builder_213.append("''")
            else:
                builder_213.append(string_from_code_point23(c_215))
        string_for_each_5771(this_40.value_211, fn_1166)
        builder_213.append("'")
    def __init__(this_87, value_217: 'str13') -> None:
        this_87.value_211 = value_217
    @property
    def value(this_266) -> 'str13':
        return this_266.value_211

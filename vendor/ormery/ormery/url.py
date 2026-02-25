from builtins import int as int17, list as list5, str as str13
from temper_core import string_from_code_point as string_from_code_point23, int_add as int_add3, int_div as int_div33
int_add_5787 = int_add3
int_div_5790 = int_div33
def append_hex_3(n_7: 'int17', sb_8: 'list5[str13]') -> 'None':
    t_26: 'int17'
    i_10: 'int17' = n_7 & 15
    if i_10 < 10:
        t_26 = 48
    else:
        t_26 = 87
    sb_8.append(string_from_code_point23(int_add_5787(i_10, t_26)))
def percent_escape_octet_to(octet_4: 'int17', sb_5: 'list5[str13]') -> 'None':
    sb_5.append('%')
    t_21: 'int17' = int_div_5790(octet_4 & 255, 16)
    append_hex_3(t_21, sb_5)
    t_23: 'int17' = octet_4 & 15
    append_hex_3(t_23, sb_5)

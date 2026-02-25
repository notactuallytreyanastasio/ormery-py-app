from builtins import bool as bool13, str as str15, Exception as Exception19, int as int20, list as list2, tuple as tuple0, len as len5
from typing import MutableSequence as MutableSequence14, Callable as Callable16, Sequence as Sequence17, Union as Union18
from temper_core import Pair as Pair3, Label as Label21, list_join as list_join1, list_map as list_map4, string_get as string_get6, str_cat as str_cat7, int_to_string as int_to_string8, string_next as string_next9, int_add as int_add10, listed_reduce_from as listed_reduce_from11, list_get as list_get12
tuple_2526 = tuple0
list_join_2528 = list_join1
list_2529 = list2
pair_2530 = Pair3
list_map_2531 = list_map4
len_2533 = len5
string_get_2534 = string_get6
str_cat_2535 = str_cat7
int_to_string_2536 = int_to_string8
string_next_2539 = string_next9
int_add_2541 = int_add10
listed_reduce_from_2542 = listed_reduce_from11
list_get_2543 = list_get12
class Test:
    failed_on_assert_65: 'bool13'
    passing_66: 'bool13'
    messages_67: 'MutableSequence14[str15]'
    __slots__ = ('failed_on_assert_65', 'passing_66', 'messages_67')
    def assert_(this_13, success_43: 'bool13', message_44: 'Callable16[[], str15]') -> 'None':
        t_406: 'str15'
        if not success_43:
            this_13.passing_66 = False
            t_406 = message_44()
            this_13.messages_67.append(t_406)
    def assert_hard(this_14, success_47: 'bool13', message_48: 'Callable16[[], str15]') -> 'None':
        this_14.assert_(success_47, message_48)
        if not success_47:
            this_14.failed_on_assert_65 = True
            assert False, str15(this_14.messages_combined())
    def soft_fail_to_hard(this_15) -> 'None':
        if this_15.has_unhandled_fail:
            this_15.failed_on_assert_65 = True
            assert False, str15(this_15.messages_combined())
    @property
    def passing(this_17) -> 'bool13':
        return this_17.passing_66
    def messages(this_18) -> 'Sequence17[str15]':
        "Messages access is presented as a function because it likely allocates. Also,\nmessages might be automatically constructed in some cases, so it's possibly\nunwise to depend on their exact formatting.\n\nthis__18: Test\n"
        return tuple_2526(this_18.messages_67)
    @property
    def failed_on_assert(this_19) -> 'bool13':
        return this_19.failed_on_assert_65
    @property
    def has_unhandled_fail(this_20) -> 'bool13':
        t_264: 'bool13'
        if this_20.failed_on_assert_65:
            t_264 = True
        else:
            t_264 = this_20.passing_66
        return not t_264
    def messages_combined(this_21) -> 'Union18[str15, None]':
        return_35: 'Union18[str15, None]'
        if not this_21.messages_67:
            return_35 = None
        else:
            def fn_399(it_64: 'str15') -> 'str15':
                return it_64
            return_35 = list_join_2528(this_21.messages_67, ', ', fn_399)
        return return_35
    def __init__(this_25) -> None:
        this_25.failed_on_assert_65 = False
        this_25.passing_66 = True
        t_398: 'MutableSequence14[str15]' = list_2529()
        this_25.messages_67 = t_398
def process_test_cases(test_cases_69: 'Sequence17[(Pair3[str15, (Callable16[[Test], None])])]') -> 'Sequence17[(Pair3[str15, (Sequence17[str15])])]':
    def fn_395(test_case_71: 'Pair3[str15, (Callable16[[Test], None])]') -> 'Pair3[str15, (Sequence17[str15])]':
        t_390: 'bool13'
        t_393: 'Sequence17[str15]'
        t_246: 'bool13'
        t_248: 'bool13'
        key_73: 'str15' = test_case_71.key
        fun_74: 'Callable16[[Test], None]' = test_case_71.value
        test_75: 'Test' = Test()
        had_bubble_76: 'bool13' = False
        try:
            fun_74(test_75)
        except Exception19:
            had_bubble_76 = True
        messages_77: 'Sequence17[str15]' = test_75.messages()
        failures_78: 'Sequence17[str15]'
        if test_75.passing:
            t_246 = not had_bubble_76
        else:
            t_246 = False
        if t_246:
            failures_78 = ()
        else:
            if had_bubble_76:
                t_390 = test_75.failed_on_assert
                t_248 = not t_390
            else:
                t_248 = False
            if t_248:
                all_messages_79: 'MutableSequence14[str15]' = list_2529(messages_77)
                all_messages_79.append('Bubble')
                t_393 = tuple_2526(all_messages_79)
                failures_78 = t_393
            else:
                failures_78 = messages_77
        return pair_2530(key_73, failures_78)
    return list_map_2531(test_cases_69, fn_395)
def escape_xml_41(s_103: 'str15') -> 'str15':
    'escapeXml takes a string and escapes it so that it has the same meaning as an\nXML text node or attribute value.\n\ns__103: String\n'
    return_40: 'str15'
    t_381: 'int20'
    t_382: 'int20'
    t_225: 'bool13'
    t_226: 'bool13'
    t_227: 'bool13'
    t_228: 'bool13'
    t_230: 'str15'
    t_231: 'str15'
    sb_105: 'list2[str15]' = ['']
    end_106: 'int20' = len_2533(s_103)
    emitted_107: 'int20' = 0
    i_108: 'int20' = 0
    while i_108 < end_106:
        with Label21() as continue_408:
            c_109: 'int20' = string_get_2534(s_103, i_108)
            if c_109 == 38:
                t_231 = '&amp;'
            elif c_109 == 60:
                t_231 = '&lt;'
            elif c_109 == 62:
                t_231 = '&gt;'
            elif c_109 == 39:
                t_231 = '&#39;'
            elif c_109 == 34:
                t_231 = '&#34;'
            else:
                if c_109 == 10:
                    t_226 = True
                else:
                    if c_109 == 13:
                        t_225 = True
                    else:
                        t_225 = c_109 == 9
                    t_226 = t_225
                if t_226:
                    continue_408.break_()
                else:
                    if c_109 < 32:
                        t_228 = True
                    else:
                        if c_109 == 65534:
                            t_227 = True
                        else:
                            t_227 = c_109 == 65535
                        t_228 = t_227
                    if t_228:
                        t_230 = str_cat_2535('[0x', int_to_string_2536(c_109, 16), ']')
                    else:
                        continue_408.break_()
                    t_231 = t_230
            esc_110: 'str15' = t_231
            sb_105.append(s_103[emitted_107 : i_108])
            sb_105.append(esc_110)
            t_381 = string_next_2539(s_103, i_108)
            emitted_107 = t_381
        t_382 = string_next_2539(s_103, i_108)
        i_108 = t_382
    if emitted_107 == 0:
        return_40 = s_103
    else:
        sb_105.append(s_103[emitted_107 : end_106])
        return_40 = ''.join(sb_105)
    return return_40
def report_test_results(test_results_80: 'Sequence17[(Pair3[str15, (Sequence17[str15])])]', write_line_81: 'Callable16[[str15], None]') -> 'None':
    t_360: 'int20'
    t_363: 'str15'
    t_369: 'str15'
    write_line_81('<testsuites>')
    total_83: 'str15' = int_to_string_2536(len_2533(test_results_80))
    def fn_352(fails_85: 'int20', test_result_86: 'Pair3[str15, (Sequence17[str15])]') -> 'int20':
        t_203: 'int20'
        if not test_result_86.value:
            t_203 = 0
        else:
            t_203 = 1
        return int_add_2541(fails_85, t_203)
    fails_84: 'str15' = int_to_string_2536(listed_reduce_from_2542(test_results_80, 0, fn_352))
    totals_88: 'str15' = str_cat_2535("tests='", total_83, "' failures='", fails_84, "'")
    write_line_81(str_cat_2535("  <testsuite name='suite' ", totals_88, " time='0.0'>"))
    i_89: 'int20' = 0
    while True:
        t_360 = len_2533(test_results_80)
        if not i_89 < t_360:
            break
        test_result_90: 'Pair3[str15, (Sequence17[str15])]' = list_get_2543(test_results_80, i_89)
        failure_messages_91: 'Sequence17[str15]' = test_result_90.value
        t_363 = test_result_90.key
        name_92: 'str15' = escape_xml_41(t_363)
        basics_93: 'str15' = str_cat_2535("name='", name_92, "' classname='", name_92, "' time='0.0'")
        if not failure_messages_91:
            write_line_81(str_cat_2535('    <testcase ', basics_93, ' />'))
        else:
            write_line_81(str_cat_2535('    <testcase ', basics_93, '>'))
            def fn_351(it_95: 'str15') -> 'str15':
                return it_95
            t_369 = list_join_2528(failure_messages_91, ', ', fn_351)
            message_94: 'str15' = escape_xml_41(t_369)
            write_line_81(str_cat_2535("      <failure message='", message_94, "' />"))
            write_line_81('    </testcase>')
        i_89 = int_add_2541(i_89, 1)
    write_line_81('  </testsuite>')
    write_line_81('</testsuites>')
def run_test_cases(test_cases_96: 'Sequence17[(Pair3[str15, (Callable16[[Test], None])])]') -> 'str15':
    report_98: 'list2[str15]' = ['']
    t_345: 'Sequence17[(Pair3[str15, (Sequence17[str15])])]' = process_test_cases(test_cases_96)
    def fn_343(line_99: 'str15') -> 'None':
        report_98.append(line_99)
        report_98.append('\n')
    report_test_results(t_345, fn_343)
    return ''.join(report_98)
def run_test(test_fun_100: 'Callable16[[Test], None]') -> 'None':
    test_102: 'Test' = Test()
    try:
        test_fun_100(test_102)
    except Exception19:
        def fn_337() -> 'str15':
            return 'bubble during test running'
        test_102.assert_(False, fn_337)
    test_102.soft_fail_to_hard()

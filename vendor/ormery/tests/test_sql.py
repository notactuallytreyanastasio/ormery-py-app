from temper_std.testing import Test
from unittest import TestCase as TestCase25
from builtins import str as str13, bool as bool15
from datetime import date as date11
from typing import Sequence as Sequence14
from ormery.sql import SqlBuilder, str_cat_5774, date_5775, SqlFragment, SqlString, SqlInt32, SqlPart
class TestCase24(TestCase25):
    def test___stringEscaping__268(self) -> None:
        'string escaping'
        test_4: Test = Test()
        try:
            def build_219(name_221: 'str13') -> 'str13':
                t_1095: 'SqlBuilder' = SqlBuilder()
                t_1095.append_safe('select * from hi where name = ')
                t_1095.append_string(name_221)
                return t_1095.accumulated.to_string()
            def build_wrong_220(name_223: 'str13') -> 'str13':
                return str_cat_5774("select * from hi where name = '", name_223, "'")
            actual_270: 'str13' = build_219('world')
            t_1105: 'bool15' = actual_270 == "select * from hi where name = 'world'"
            def fn_1102() -> 'str13':
                return str_cat_5774('expected build("world") == (', "select * from hi where name = 'world'", ') not (', actual_270, ')')
            test_4.assert_(t_1105, fn_1102)
            bobby_tables_225: 'str13' = "Robert'); drop table hi;--"
            actual_272: 'str13' = build_219("Robert'); drop table hi;--")
            t_1109: 'bool15' = actual_272 == "select * from hi where name = 'Robert''); drop table hi;--'"
            def fn_1101() -> 'str13':
                return str_cat_5774('expected build(bobbyTables) == (', "select * from hi where name = 'Robert''); drop table hi;--'", ') not (', actual_272, ')')
            test_4.assert_(t_1109, fn_1101)
            def fn_1100() -> 'str13':
                return "expected buildWrong(bobbyTables) == (select * from hi where name = 'Robert'); drop table hi;--') not (select * from hi where name = 'Robert'); drop table hi;--')"
            test_4.assert_(True, fn_1100)
        finally:
            test_4.soft_fail_to_hard()
class TestCase26(TestCase25):
    def test___stringEdgeCases__276(self) -> None:
        'string edge cases'
        test_5: Test = Test()
        try:
            t_1063: 'SqlBuilder' = SqlBuilder()
            t_1063.append_safe('v = ')
            t_1063.append_string('')
            actual_277: 'str13' = t_1063.accumulated.to_string()
            t_1069: 'bool15' = actual_277 == "v = ''"
            def fn_1062() -> 'str13':
                return str_cat_5774('expected stringExpr(`-work/src//sql/`.sql, true, "v = ", \\interpolate, "").toString() == (', "v = ''", ') not (', actual_277, ')')
            test_5.assert_(t_1069, fn_1062)
            t_1071: 'SqlBuilder' = SqlBuilder()
            t_1071.append_safe('v = ')
            t_1071.append_string("a''b")
            actual_280: 'str13' = t_1071.accumulated.to_string()
            t_1077: 'bool15' = actual_280 == "v = 'a''''b'"
            def fn_1061() -> 'str13':
                return str_cat_5774("expected stringExpr(`-work/src//sql/`.sql, true, \"v = \", \\interpolate, \"a''b\").toString() == (", "v = 'a''''b'", ') not (', actual_280, ')')
            test_5.assert_(t_1077, fn_1061)
            t_1079: 'SqlBuilder' = SqlBuilder()
            t_1079.append_safe('v = ')
            t_1079.append_string('Hello \u4e16\u754c')
            actual_283: 'str13' = t_1079.accumulated.to_string()
            t_1085: 'bool15' = actual_283 == "v = 'Hello \u4e16\u754c'"
            def fn_1060() -> 'str13':
                return str_cat_5774('expected stringExpr(`-work/src//sql/`.sql, true, "v = ", \\interpolate, "Hello \u4e16\u754c").toString() == (', "v = 'Hello \u4e16\u754c'", ') not (', actual_283, ')')
            test_5.assert_(t_1085, fn_1060)
            t_1087: 'SqlBuilder' = SqlBuilder()
            t_1087.append_safe('v = ')
            t_1087.append_string('Line1\nLine2')
            actual_286: 'str13' = t_1087.accumulated.to_string()
            t_1093: 'bool15' = actual_286 == "v = 'Line1\nLine2'"
            def fn_1059() -> 'str13':
                return str_cat_5774('expected stringExpr(`-work/src//sql/`.sql, true, "v = ", \\interpolate, "Line1\\nLine2").toString() == (', "v = 'Line1\nLine2'", ') not (', actual_286, ')')
            test_5.assert_(t_1093, fn_1059)
        finally:
            test_5.soft_fail_to_hard()
class TestCase27(TestCase25):
    def test___numbersAndBooleans__289(self) -> None:
        'numbers and booleans'
        test_6: Test = Test()
        try:
            t_1034: 'SqlBuilder' = SqlBuilder()
            t_1034.append_safe('select ')
            t_1034.append_int32(42)
            t_1034.append_safe(', ')
            t_1034.append_int64(43)
            t_1034.append_safe(', ')
            t_1034.append_float64(19.99)
            t_1034.append_safe(', ')
            t_1034.append_boolean(True)
            t_1034.append_safe(', ')
            t_1034.append_boolean(False)
            actual_290: 'str13' = t_1034.accumulated.to_string()
            t_1048: 'bool15' = actual_290 == 'select 42, 43, 19.99, TRUE, FALSE'
            def fn_1033() -> 'str13':
                return str_cat_5774('expected stringExpr(`-work/src//sql/`.sql, true, "select ", \\interpolate, 42, ", ", \\interpolate, 43, ", ", \\interpolate, 19.99, ", ", \\interpolate, true, ", ", \\interpolate, false).toString() == (', 'select 42, 43, 19.99, TRUE, FALSE', ') not (', actual_290, ')')
            test_6.assert_(t_1048, fn_1033)
            t_624: 'date11'
            t_624 = date_5775(2024, 12, 25)
            date_228: 'date11' = t_624
            t_1050: 'SqlBuilder' = SqlBuilder()
            t_1050.append_safe('insert into t values (')
            t_1050.append_date(date_228)
            t_1050.append_safe(')')
            actual_293: 'str13' = t_1050.accumulated.to_string()
            t_1057: 'bool15' = actual_293 == "insert into t values ('2024-12-25')"
            def fn_1032() -> 'str13':
                return str_cat_5774('expected stringExpr(`-work/src//sql/`.sql, true, "insert into t values (", \\interpolate, date, ")").toString() == (', "insert into t values ('2024-12-25')", ') not (', actual_293, ')')
            test_6.assert_(t_1057, fn_1032)
        finally:
            test_6.soft_fail_to_hard()
class TestCase28(TestCase25):
    def test___lists__296(self) -> None:
        'lists'
        test_7: Test = Test()
        try:
            t_978: 'SqlBuilder' = SqlBuilder()
            t_978.append_safe('v IN (')
            t_978.append_string_list(('a', 'b', "c'd"))
            t_978.append_safe(')')
            actual_297: 'str13' = t_978.accumulated.to_string()
            t_985: 'bool15' = actual_297 == "v IN ('a', 'b', 'c''d')"
            def fn_977() -> 'str13':
                return str_cat_5774("expected stringExpr(`-work/src//sql/`.sql, true, \"v IN (\", \\interpolate, list(\"a\", \"b\", \"c'd\"), \")\").toString() == (", "v IN ('a', 'b', 'c''d')", ') not (', actual_297, ')')
            test_7.assert_(t_985, fn_977)
            t_987: 'SqlBuilder' = SqlBuilder()
            t_987.append_safe('v IN (')
            t_987.append_int32_list((1, 2, 3))
            t_987.append_safe(')')
            actual_300: 'str13' = t_987.accumulated.to_string()
            t_994: 'bool15' = actual_300 == 'v IN (1, 2, 3)'
            def fn_976() -> 'str13':
                return str_cat_5774('expected stringExpr(`-work/src//sql/`.sql, true, "v IN (", \\interpolate, list(1, 2, 3), ")").toString() == (', 'v IN (1, 2, 3)', ') not (', actual_300, ')')
            test_7.assert_(t_994, fn_976)
            t_996: 'SqlBuilder' = SqlBuilder()
            t_996.append_safe('v IN (')
            t_996.append_int64_list((1, 2))
            t_996.append_safe(')')
            actual_303: 'str13' = t_996.accumulated.to_string()
            t_1003: 'bool15' = actual_303 == 'v IN (1, 2)'
            def fn_975() -> 'str13':
                return str_cat_5774('expected stringExpr(`-work/src//sql/`.sql, true, "v IN (", \\interpolate, list(1, 2), ")").toString() == (', 'v IN (1, 2)', ') not (', actual_303, ')')
            test_7.assert_(t_1003, fn_975)
            t_1005: 'SqlBuilder' = SqlBuilder()
            t_1005.append_safe('v IN (')
            t_1005.append_float64_list((1.0, 2.0))
            t_1005.append_safe(')')
            actual_306: 'str13' = t_1005.accumulated.to_string()
            t_1012: 'bool15' = actual_306 == 'v IN (1.0, 2.0)'
            def fn_974() -> 'str13':
                return str_cat_5774('expected stringExpr(`-work/src//sql/`.sql, true, "v IN (", \\interpolate, list(1.0, 2.0), ")").toString() == (', 'v IN (1.0, 2.0)', ') not (', actual_306, ')')
            test_7.assert_(t_1012, fn_974)
            t_1014: 'SqlBuilder' = SqlBuilder()
            t_1014.append_safe('v IN (')
            t_1014.append_boolean_list((True, False))
            t_1014.append_safe(')')
            actual_309: 'str13' = t_1014.accumulated.to_string()
            t_1021: 'bool15' = actual_309 == 'v IN (TRUE, FALSE)'
            def fn_973() -> 'str13':
                return str_cat_5774('expected stringExpr(`-work/src//sql/`.sql, true, "v IN (", \\interpolate, list(true, false), ")").toString() == (', 'v IN (TRUE, FALSE)', ') not (', actual_309, ')')
            test_7.assert_(t_1021, fn_973)
            t_596: 'date11'
            t_596 = date_5775(2024, 1, 1)
            t_597: 'date11' = t_596
            t_598: 'date11'
            t_598 = date_5775(2024, 12, 25)
            t_599: 'date11' = t_598
            dates_230: 'Sequence14[date11]' = (t_597, t_599)
            t_1023: 'SqlBuilder' = SqlBuilder()
            t_1023.append_safe('v IN (')
            t_1023.append_date_list(dates_230)
            t_1023.append_safe(')')
            actual_312: 'str13' = t_1023.accumulated.to_string()
            t_1030: 'bool15' = actual_312 == "v IN ('2024-01-01', '2024-12-25')"
            def fn_972() -> 'str13':
                return str_cat_5774('expected stringExpr(`-work/src//sql/`.sql, true, "v IN (", \\interpolate, dates, ")").toString() == (', "v IN ('2024-01-01', '2024-12-25')", ') not (', actual_312, ')')
            test_7.assert_(t_1030, fn_972)
        finally:
            test_7.soft_fail_to_hard()
class TestCase29(TestCase25):
    def test___nesting__315(self) -> None:
        'nesting'
        test_8: Test = Test()
        try:
            name_232: 'str13' = 'Someone'
            t_941: 'SqlBuilder' = SqlBuilder()
            t_941.append_safe('where p.last_name = ')
            t_941.append_string('Someone')
            condition_233: 'SqlFragment' = t_941.accumulated
            t_945: 'SqlBuilder' = SqlBuilder()
            t_945.append_safe('select p.id from person p ')
            t_945.append_fragment(condition_233)
            actual_317: 'str13' = t_945.accumulated.to_string()
            t_951: 'bool15' = actual_317 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_940() -> 'str13':
                return str_cat_5774('expected stringExpr(`-work/src//sql/`.sql, true, "select p.id from person p ", \\interpolate, condition).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_317, ')')
            test_8.assert_(t_951, fn_940)
            t_953: 'SqlBuilder' = SqlBuilder()
            t_953.append_safe('select p.id from person p ')
            t_953.append_part(condition_233.to_source())
            actual_320: 'str13' = t_953.accumulated.to_string()
            t_960: 'bool15' = actual_320 == "select p.id from person p where p.last_name = 'Someone'"
            def fn_939() -> 'str13':
                return str_cat_5774('expected stringExpr(`-work/src//sql/`.sql, true, "select p.id from person p ", \\interpolate, condition.toSource()).toString() == (', "select p.id from person p where p.last_name = 'Someone'", ') not (', actual_320, ')')
            test_8.assert_(t_960, fn_939)
            parts_234: 'Sequence14[SqlPart]' = (SqlString("a'b"), SqlInt32(3))
            t_964: 'SqlBuilder' = SqlBuilder()
            t_964.append_safe('select ')
            t_964.append_part_list(parts_234)
            actual_323: 'str13' = t_964.accumulated.to_string()
            t_970: 'bool15' = actual_323 == "select 'a''b', 3"
            def fn_938() -> 'str13':
                return str_cat_5774('expected stringExpr(`-work/src//sql/`.sql, true, "select ", \\interpolate, parts).toString() == (', "select 'a''b', 3", ') not (', actual_323, ')')
            test_8.assert_(t_970, fn_938)
        finally:
            test_8.soft_fail_to_hard()

from ormery.sql import SqlFragment, SqlBuilder
from temper_std.testing import Test
from unittest import TestCase as TestCase25
from builtins import str as str13, bool as bool15, int as int17
from types import MappingProxyType as MappingProxyType46
from typing import Sequence as Sequence14
from ormery.ormery import schema, field, Schema, InMemoryStore, Query, str_cat_5818, map_constructor_5847, pair_5846, to_insert_sql, to_sql_query, WhereClause, OrderClause, is_valid_identifier, Record, len_5816, int_to_string_5821
from ormery.sql import SqlFragment
class TestCase69(TestCase25):
    def test___toSqlSelectAll__830(self) -> None:
        'toSql: select all'
        test_17: Test = Test()
        try:
            s_527: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_528: 'InMemoryStore' = InMemoryStore()
            q_529: 'Query' = Query(s_527, store_528)
            actual_831: 'str13' = q_529.to_sql().to_string()
            t_3717: 'bool15' = actual_831 == 'SELECT * FROM users'
            def fn_3710() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT * FROM users', ') not (', actual_831, ')')
            test_17.assert_(t_3717, fn_3710)
        finally:
            test_17.soft_fail_to_hard()
class TestCase70(TestCase25):
    def test___toSqlSelectColumns__833(self) -> None:
        'toSql: select columns'
        test_18: Test = Test()
        try:
            s_531: 'Schema' = schema('users', (field('name', 'String', False, False), field('age', 'Int', False, False)))
            store_532: 'InMemoryStore' = InMemoryStore()
            q_533: 'Query' = Query(s_531, store_532).select(('name', 'age'))
            actual_834: 'str13' = q_533.to_sql().to_string()
            t_3708: 'bool15' = actual_834 == 'SELECT name, age FROM users'
            def fn_3700() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT name, age FROM users', ') not (', actual_834, ')')
            test_18.assert_(t_3708, fn_3700)
        finally:
            test_18.soft_fail_to_hard()
class TestCase71(TestCase25):
    def test___toSqlWhereString__836(self) -> None:
        'toSql: where string'
        test_19: Test = Test()
        try:
            s_535: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_536: 'InMemoryStore' = InMemoryStore()
            q_537: 'Query' = Query(s_535, store_536).where('name', '=', 'Alice')
            actual_837: 'str13' = q_537.to_sql().to_string()
            t_3698: 'bool15' = actual_837 == "SELECT * FROM users WHERE name = 'Alice'"
            def fn_3690() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', "SELECT * FROM users WHERE name = 'Alice'", ') not (', actual_837, ')')
            test_19.assert_(t_3698, fn_3690)
        finally:
            test_19.soft_fail_to_hard()
class TestCase72(TestCase25):
    def test___toSqlWhereInt__839(self) -> None:
        'toSql: where int'
        test_20: Test = Test()
        try:
            s_539: 'Schema' = schema('users', (field('age', 'Int', False, False),))
            store_540: 'InMemoryStore' = InMemoryStore()
            q_541: 'Query' = Query(s_539, store_540).where('age', '>=', '18')
            actual_840: 'str13' = q_541.to_sql().to_string()
            t_3688: 'bool15' = actual_840 == 'SELECT * FROM users WHERE age >= 18'
            def fn_3680() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT * FROM users WHERE age >= 18', ') not (', actual_840, ')')
            test_20.assert_(t_3688, fn_3680)
        finally:
            test_20.soft_fail_to_hard()
class TestCase73(TestCase25):
    def test___toSqlSqlInjectionBlocked__842(self) -> None:
        'toSql: SQL injection blocked'
        test_21: Test = Test()
        try:
            s_543: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_544: 'InMemoryStore' = InMemoryStore()
            bobby_545: 'str13' = "Robert'); DROP TABLE users;--"
            q_546: 'Query' = Query(s_543, store_544).where('name', '=', "Robert'); DROP TABLE users;--")
            result_547: 'str13' = q_546.to_sql().to_string()
            actual_843: 'str13' = result_547
            t_3678: 'bool15' = actual_843 == "SELECT * FROM users WHERE name = 'Robert''); DROP TABLE users;--'"
            def fn_3670() -> 'str13':
                return str_cat_5818('expected result == (', "SELECT * FROM users WHERE name = 'Robert''); DROP TABLE users;--'", ') not (', actual_843, ')')
            test_21.assert_(t_3678, fn_3670)
        finally:
            test_21.soft_fail_to_hard()
class TestCase74(TestCase25):
    def test___toSqlOperatorNormalization__845(self) -> None:
        'toSql: operator normalization'
        test_22: Test = Test()
        try:
            s_549: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_550: 'InMemoryStore' = InMemoryStore()
            q_551: 'Query' = Query(s_549, store_550).where('name', '==', 'Alice')
            actual_846: 'str13' = q_551.to_sql().to_string()
            t_3668: 'bool15' = actual_846 == "SELECT * FROM users WHERE name = 'Alice'"
            def fn_3660() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', "SELECT * FROM users WHERE name = 'Alice'", ') not (', actual_846, ')')
            test_22.assert_(t_3668, fn_3660)
        finally:
            test_22.soft_fail_to_hard()
class TestCase75(TestCase25):
    def test___toSqlInvalidOperatorFallback__848(self) -> None:
        'toSql: invalid operator fallback'
        test_23: Test = Test()
        try:
            s_553: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_554: 'InMemoryStore' = InMemoryStore()
            q_555: 'Query' = Query(s_553, store_554).where('name', 'LIKE', 'Alice')
            actual_849: 'str13' = q_555.to_sql().to_string()
            t_3658: 'bool15' = actual_849 == "SELECT * FROM users WHERE name = 'Alice'"
            def fn_3650() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', "SELECT * FROM users WHERE name = 'Alice'", ') not (', actual_849, ')')
            test_23.assert_(t_3658, fn_3650)
        finally:
            test_23.soft_fail_to_hard()
class TestCase76(TestCase25):
    def test___toSqlMultipleWhere__851(self) -> None:
        'toSql: multiple where'
        test_24: Test = Test()
        try:
            s_557: 'Schema' = schema('users', (field('age', 'Int', False, False),))
            store_558: 'InMemoryStore' = InMemoryStore()
            q_559: 'Query' = Query(s_557, store_558).where('age', '>=', '18').where('age', '<', '30')
            actual_852: 'str13' = q_559.to_sql().to_string()
            t_3648: 'bool15' = actual_852 == 'SELECT * FROM users WHERE age >= 18 AND age < 30'
            def fn_3639() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT * FROM users WHERE age >= 18 AND age < 30', ') not (', actual_852, ')')
            test_24.assert_(t_3648, fn_3639)
        finally:
            test_24.soft_fail_to_hard()
class TestCase77(TestCase25):
    def test___toSqlOrderBy__854(self) -> None:
        'toSql: order by'
        test_25: Test = Test()
        try:
            s_561: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_562: 'InMemoryStore' = InMemoryStore()
            q_563: 'Query' = Query(s_561, store_562).order_by('name', 'asc')
            actual_855: 'str13' = q_563.to_sql().to_string()
            t_3637: 'bool15' = actual_855 == 'SELECT * FROM users ORDER BY name ASC'
            def fn_3629() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT * FROM users ORDER BY name ASC', ') not (', actual_855, ')')
            test_25.assert_(t_3637, fn_3629)
        finally:
            test_25.soft_fail_to_hard()
class TestCase78(TestCase25):
    def test___toSqlOrderByDesc__857(self) -> None:
        'toSql: order by desc'
        test_26: Test = Test()
        try:
            s_565: 'Schema' = schema('users', (field('age', 'Int', False, False),))
            store_566: 'InMemoryStore' = InMemoryStore()
            q_567: 'Query' = Query(s_565, store_566).order_by('age', 'desc')
            actual_858: 'str13' = q_567.to_sql().to_string()
            t_3627: 'bool15' = actual_858 == 'SELECT * FROM users ORDER BY age DESC'
            def fn_3619() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT * FROM users ORDER BY age DESC', ') not (', actual_858, ')')
            test_26.assert_(t_3627, fn_3619)
        finally:
            test_26.soft_fail_to_hard()
class TestCase79(TestCase25):
    def test___toSqlLimit__860(self) -> None:
        'toSql: limit'
        test_27: Test = Test()
        try:
            s_569: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_570: 'InMemoryStore' = InMemoryStore()
            q_571: 'Query' = Query(s_569, store_570).limit(10)
            actual_861: 'str13' = q_571.to_sql().to_string()
            t_3617: 'bool15' = actual_861 == 'SELECT * FROM users LIMIT 10'
            def fn_3609() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT * FROM users LIMIT 10', ') not (', actual_861, ')')
            test_27.assert_(t_3617, fn_3609)
        finally:
            test_27.soft_fail_to_hard()
class TestCase80(TestCase25):
    def test___toSqlOffset__863(self) -> None:
        'toSql: offset'
        test_28: Test = Test()
        try:
            s_573: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_574: 'InMemoryStore' = InMemoryStore()
            q_575: 'Query' = Query(s_573, store_574).offset(5)
            actual_864: 'str13' = q_575.to_sql().to_string()
            t_3607: 'bool15' = actual_864 == 'SELECT * FROM users OFFSET 5'
            def fn_3599() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT * FROM users OFFSET 5', ') not (', actual_864, ')')
            test_28.assert_(t_3607, fn_3599)
        finally:
            test_28.soft_fail_to_hard()
class TestCase81(TestCase25):
    def test___toSqlComplexQuery__866(self) -> None:
        'toSql: complex query'
        test_29: Test = Test()
        try:
            s_577: 'Schema' = schema('users', (field('name', 'String', False, False), field('age', 'Int', False, False)))
            store_578: 'InMemoryStore' = InMemoryStore()
            q_579: 'Query' = Query(s_577, store_578).select(('name', 'age')).where('age', '>=', '18').order_by('age', 'desc').limit(10).offset(20)
            actual_867: 'str13' = q_579.to_sql().to_string()
            t_3597: 'bool15' = actual_867 == 'SELECT name, age FROM users WHERE age >= 18 ORDER BY age DESC LIMIT 10 OFFSET 20'
            def fn_3585() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT name, age FROM users WHERE age >= 18 ORDER BY age DESC LIMIT 10 OFFSET 20', ') not (', actual_867, ')')
            test_29.assert_(t_3597, fn_3585)
        finally:
            test_29.soft_fail_to_hard()
class TestCase82(TestCase25):
    def test___toSqlUnicodeEscaping__869(self) -> None:
        'toSql: unicode escaping'
        test_30: Test = Test()
        try:
            s_581: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_582: 'InMemoryStore' = InMemoryStore()
            q_583: 'Query' = Query(s_581, store_582).where('name', '=', 'Hello \u4e16\u754c')
            actual_870: 'str13' = q_583.to_sql().to_string()
            t_3583: 'bool15' = actual_870 == "SELECT * FROM users WHERE name = 'Hello \u4e16\u754c'"
            def fn_3575() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', "SELECT * FROM users WHERE name = 'Hello \u4e16\u754c'", ') not (', actual_870, ')')
            test_30.assert_(t_3583, fn_3575)
        finally:
            test_30.soft_fail_to_hard()
class TestCase83(TestCase25):
    def test___toSqlEmbeddedQuotes__872(self) -> None:
        'toSql: embedded quotes'
        test_31: Test = Test()
        try:
            s_585: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_586: 'InMemoryStore' = InMemoryStore()
            q_587: 'Query' = Query(s_585, store_586).where('name', '=', "O'Brien")
            actual_873: 'str13' = q_587.to_sql().to_string()
            t_3573: 'bool15' = actual_873 == "SELECT * FROM users WHERE name = 'O''Brien'"
            def fn_3565() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', "SELECT * FROM users WHERE name = 'O''Brien'", ') not (', actual_873, ')')
            test_31.assert_(t_3573, fn_3565)
        finally:
            test_31.soft_fail_to_hard()
class TestCase84(TestCase25):
    def test___toSqlEmptyString__875(self) -> None:
        'toSql: empty string'
        test_32: Test = Test()
        try:
            s_589: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_590: 'InMemoryStore' = InMemoryStore()
            q_591: 'Query' = Query(s_589, store_590).where('name', '=', '')
            actual_876: 'str13' = q_591.to_sql().to_string()
            t_3563: 'bool15' = actual_876 == "SELECT * FROM users WHERE name = ''"
            def fn_3555() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', "SELECT * FROM users WHERE name = ''", ') not (', actual_876, ')')
            test_32.assert_(t_3563, fn_3555)
        finally:
            test_32.soft_fail_to_hard()
class TestCase85(TestCase25):
    def test___toInsertSqlBasicInsert__878(self) -> None:
        'toInsertSql: basic insert'
        test_33: Test = Test()
        try:
            s_593: 'Schema' = schema('users', (field('name', 'String', False, False), field('age', 'Int', False, False)))
            vals_594: 'MappingProxyType46[str13, str13]' = map_constructor_5847((pair_5846('name', 'Alice'), pair_5846('age', '25')))
            result_595: 'SqlFragment' = to_insert_sql(s_593, vals_594)
            actual_879: 'str13' = result_595.to_string()
            t_3553: 'bool15' = actual_879 == "INSERT INTO users (name, age) VALUES ('Alice', 25)"
            def fn_3545() -> 'str13':
                return str_cat_5818('expected result.toString() == (', "INSERT INTO users (name, age) VALUES ('Alice', 25)", ') not (', actual_879, ')')
            test_33.assert_(t_3553, fn_3545)
        finally:
            test_33.soft_fail_to_hard()
class TestCase86(TestCase25):
    def test___toInsertSqlInjectionBlocked__881(self) -> None:
        'toInsertSql: injection blocked'
        test_34: Test = Test()
        try:
            s_597: 'Schema' = schema('users', (field('name', 'String', False, False),))
            vals_598: 'MappingProxyType46[str13, str13]' = map_constructor_5847((pair_5846('name', "Robert'); DROP TABLE users;--"),))
            result_599: 'SqlFragment' = to_insert_sql(s_597, vals_598)
            actual_882: 'str13' = result_599.to_string()
            t_3543: 'bool15' = actual_882 == "INSERT INTO users (name) VALUES ('Robert''); DROP TABLE users;--')"
            def fn_3536() -> 'str13':
                return str_cat_5818('expected result.toString() == (', "INSERT INTO users (name) VALUES ('Robert''); DROP TABLE users;--')", ') not (', actual_882, ')')
            test_34.assert_(t_3543, fn_3536)
        finally:
            test_34.soft_fail_to_hard()
class TestCase87(TestCase25):
    def test___toSqlQueryStandalone__884(self) -> None:
        'toSqlQuery: standalone'
        test_35: Test = Test()
        try:
            s_601: 'Schema' = schema('users', (field('name', 'String', False, False), field('age', 'Int', False, False)))
            result_602: 'SqlFragment' = to_sql_query(s_601, ('name',), (WhereClause('age', '>', '21'),), (OrderClause('name', 'asc'),), 5, 0)
            actual_885: 'str13' = result_602.to_string()
            t_3534: 'bool15' = actual_885 == 'SELECT name FROM users WHERE age > 21 ORDER BY name ASC LIMIT 5'
            def fn_3525() -> 'str13':
                return str_cat_5818('expected result.toString() == (', 'SELECT name FROM users WHERE age > 21 ORDER BY name ASC LIMIT 5', ') not (', actual_885, ')')
            test_35.assert_(t_3534, fn_3525)
        finally:
            test_35.soft_fail_to_hard()
class TestCase88(TestCase25):
    def test___toSqlAdversarialFieldNameBlocked__887(self) -> None:
        'toSql: adversarial field name blocked'
        test_36: Test = Test()
        try:
            s_604: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_605: 'InMemoryStore' = InMemoryStore()
            q_606: 'Query' = Query(s_604, store_605).where('1=1; DROP TABLE users; --', '=', 'Alice')
            actual_888: 'str13' = q_606.to_sql().to_string()
            t_3523: 'bool15' = actual_888 == 'SELECT * FROM users'
            def fn_3515() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT * FROM users', ') not (', actual_888, ')')
            test_36.assert_(t_3523, fn_3515)
        finally:
            test_36.soft_fail_to_hard()
class TestCase89(TestCase25):
    def test___toSqlAdversarialSelectColumnBlocked__890(self) -> None:
        'toSql: adversarial select column blocked'
        test_37: Test = Test()
        try:
            s_608: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_609: 'InMemoryStore' = InMemoryStore()
            q_610: 'Query' = Query(s_608, store_609).select(('name', '1; DROP TABLE users'))
            actual_891: 'str13' = q_610.to_sql().to_string()
            t_3513: 'bool15' = actual_891 == 'SELECT name FROM users'
            def fn_3505() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT name FROM users', ') not (', actual_891, ')')
            test_37.assert_(t_3513, fn_3505)
        finally:
            test_37.soft_fail_to_hard()
class TestCase90(TestCase25):
    def test___toSqlAdversarialOrderByBlocked__893(self) -> None:
        'toSql: adversarial order by blocked'
        test_38: Test = Test()
        try:
            s_612: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_613: 'InMemoryStore' = InMemoryStore()
            q_614: 'Query' = Query(s_612, store_613).order_by('1; DROP TABLE users', 'asc')
            actual_894: 'str13' = q_614.to_sql().to_string()
            t_3503: 'bool15' = actual_894 == 'SELECT * FROM users'
            def fn_3495() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT * FROM users', ') not (', actual_894, ')')
            test_38.assert_(t_3503, fn_3495)
        finally:
            test_38.soft_fail_to_hard()
class TestCase91(TestCase25):
    def test___isValidIdentifierValidNames__896(self) -> None:
        'isValidIdentifier: valid names'
        test_39: Test = Test()
        try:
            t_3480: 'bool15' = is_valid_identifier('users')
            def fn_3479() -> 'str13':
                return 'expected `-work/src//`.isValidIdentifier("users")'
            test_39.assert_(t_3480, fn_3479)
            t_3483: 'bool15' = is_valid_identifier('user_table')
            def fn_3478() -> 'str13':
                return 'expected `-work/src//`.isValidIdentifier("user_table")'
            test_39.assert_(t_3483, fn_3478)
            t_3486: 'bool15' = is_valid_identifier('Table1')
            def fn_3477() -> 'str13':
                return 'expected `-work/src//`.isValidIdentifier("Table1")'
            test_39.assert_(t_3486, fn_3477)
            t_3489: 'bool15' = is_valid_identifier('_private')
            def fn_3476() -> 'str13':
                return 'expected `-work/src//`.isValidIdentifier("_private")'
            test_39.assert_(t_3489, fn_3476)
            t_3492: 'bool15' = is_valid_identifier('a')
            def fn_3475() -> 'str13':
                return 'expected `-work/src//`.isValidIdentifier("a")'
            test_39.assert_(t_3492, fn_3475)
        finally:
            test_39.soft_fail_to_hard()
class TestCase92(TestCase25):
    def test___isValidIdentifierInvalidNames__897(self) -> None:
        'isValidIdentifier: invalid names'
        test_40: Test = Test()
        try:
            t_3453: 'bool15' = not is_valid_identifier('')
            def fn_3450() -> 'str13':
                return 'expected !`-work/src//`.isValidIdentifier("")'
            test_40.assert_(t_3453, fn_3450)
            t_3457: 'bool15' = not is_valid_identifier('users; DROP TABLE')
            def fn_3449() -> 'str13':
                return 'expected !`-work/src//`.isValidIdentifier("users; DROP TABLE")'
            test_40.assert_(t_3457, fn_3449)
            t_3461: 'bool15' = not is_valid_identifier('users--')
            def fn_3448() -> 'str13':
                return 'expected !`-work/src//`.isValidIdentifier("users--")'
            test_40.assert_(t_3461, fn_3448)
            t_3465: 'bool15' = not is_valid_identifier('ta ble')
            def fn_3447() -> 'str13':
                return 'expected !`-work/src//`.isValidIdentifier("ta ble")'
            test_40.assert_(t_3465, fn_3447)
            t_3469: 'bool15' = not is_valid_identifier('table.name')
            def fn_3446() -> 'str13':
                return 'expected !`-work/src//`.isValidIdentifier("table.name")'
            test_40.assert_(t_3469, fn_3446)
            t_3473: 'bool15' = not is_valid_identifier("Robert'); DROP TABLE users;--")
            def fn_3445() -> 'str13':
                return "expected !`-work/src//`.isValidIdentifier(\"Robert'); DROP TABLE users;--\")"
            test_40.assert_(t_3473, fn_3445)
        finally:
            test_40.soft_fail_to_hard()
class TestCase93(TestCase25):
    def test___toSqlNonNumericIntValueProducesAlwaysFalse__898(self) -> None:
        'toSql: non-numeric Int value produces always-false'
        test_41: Test = Test()
        try:
            s_618: 'Schema' = schema('users', (field('age', 'Int', False, False),))
            store_619: 'InMemoryStore' = InMemoryStore()
            q_620: 'Query' = Query(s_618, store_619).where('age', '=', 'admin')
            actual_899: 'str13' = q_620.to_sql().to_string()
            t_3443: 'bool15' = actual_899 == 'SELECT * FROM users WHERE 1 = 0'
            def fn_3435() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT * FROM users WHERE 1 = 0', ') not (', actual_899, ')')
            test_41.assert_(t_3443, fn_3435)
        finally:
            test_41.soft_fail_to_hard()
class TestCase94(TestCase25):
    def test___inMemoryNonNumericIntValueMatchesNothing__901(self) -> None:
        'in-memory: non-numeric Int value matches nothing'
        test_42: Test = Test()
        try:
            s_622: 'Schema' = schema('users', (field('name', 'String', False, False), field('age', 'Int', False, False)))
            store_623: 'InMemoryStore' = InMemoryStore()
            store_623.insert('users', map_constructor_5847((pair_5846('name', 'Alice'), pair_5846('age', '0'))))
            results_624: 'Sequence14[Record]' = Query(s_622, store_623).where('age', '=', 'admin').all()
            actual_902: 'int17' = len_5816(results_624)
            t_3433: 'bool15' = actual_902 == 0
            def fn_3421() -> 'str13':
                return str_cat_5818('expected results.length == (', int_to_string_5821(0), ') not (', int_to_string_5821(actual_902), ')')
            test_42.assert_(t_3433, fn_3421)
        finally:
            test_42.soft_fail_to_hard()
class TestCase95(TestCase25):
    def test___toSqlLimitZeroEmitsLimit0__904(self) -> None:
        'toSql: limit zero emits LIMIT 0'
        test_43: Test = Test()
        try:
            s_626: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_627: 'InMemoryStore' = InMemoryStore()
            q_628: 'Query' = Query(s_626, store_627).limit(0)
            actual_905: 'str13' = q_628.to_sql().to_string()
            t_3417: 'bool15' = actual_905 == 'SELECT * FROM users LIMIT 0'
            def fn_3409() -> 'str13':
                return str_cat_5818('expected q.toSql().toString() == (', 'SELECT * FROM users LIMIT 0', ') not (', actual_905, ')')
            test_43.assert_(t_3417, fn_3409)
        finally:
            test_43.soft_fail_to_hard()
class TestCase96(TestCase25):
    def test___inMemoryLimitZeroReturnsEmpty__907(self) -> None:
        'in-memory: limit zero returns empty'
        test_44: Test = Test()
        try:
            s_630: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_631: 'InMemoryStore' = InMemoryStore()
            store_631.insert('users', map_constructor_5847((pair_5846('name', 'Alice'),)))
            results_632: 'Sequence14[Record]' = Query(s_630, store_631).limit(0).all()
            actual_908: 'int17' = len_5816(results_632)
            t_3407: 'bool15' = actual_908 == 0
            def fn_3396() -> 'str13':
                return str_cat_5818('expected results.length == (', int_to_string_5821(0), ') not (', int_to_string_5821(actual_908), ')')
            test_44.assert_(t_3407, fn_3396)
        finally:
            test_44.soft_fail_to_hard()
class TestCase97(TestCase25):
    def test___inMemoryNegativeLimitClampedToZero__910(self) -> None:
        'in-memory: negative limit clamped to zero'
        test_45: Test = Test()
        try:
            s_634: 'Schema' = schema('users', (field('name', 'String', False, False),))
            store_635: 'InMemoryStore' = InMemoryStore()
            store_635.insert('users', map_constructor_5847((pair_5846('name', 'Alice'),)))
            results_636: 'Sequence14[Record]' = Query(s_634, store_635).limit(-5).all()
            actual_911: 'int17' = len_5816(results_636)
            t_3392: 'bool15' = actual_911 == 0
            def fn_3381() -> 'str13':
                return str_cat_5818('expected results.length == (', int_to_string_5821(0), ') not (', int_to_string_5821(actual_911), ')')
            test_45.assert_(t_3392, fn_3381)
        finally:
            test_45.soft_fail_to_hard()
class TestCase98(TestCase25):
    def test___toInsertSqlNoMatchingFieldsReturnsEmpty__913(self) -> None:
        'toInsertSql: no matching fields returns empty'
        test_46: Test = Test()
        try:
            s_638: 'Schema' = schema('users', (field('name', 'String', False, False),))
            vals_639: 'MappingProxyType46[str13, str13]' = map_constructor_5847((pair_5846('nonexistent', 'value'),))
            result_640: 'SqlFragment' = to_insert_sql(s_638, vals_639)
            actual_914: 'str13' = result_640.to_string()
            t_3377: 'bool15' = actual_914 == ''
            def fn_3370() -> 'str13':
                return str_cat_5818('expected result.toString() == (', '', ') not (', actual_914, ')')
            test_46.assert_(t_3377, fn_3370)
        finally:
            test_46.soft_fail_to_hard()

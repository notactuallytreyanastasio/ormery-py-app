from ormery.sql import SqlFragment, SqlBuilder
from ormery.html import SafeHtmlBuilder, SafeHtml
from temper_core import LoggingConsole as LoggingConsole30, Label as Label41, int_add as int_add3, str_cat as str_cat10, list_map as list_map57, list_join as list_join58, int_to_string as int_to_string9, list_get as list_get2, mapped_has as mapped_has59, map_builder_set as map_builder_set38, mapped_to_map as mapped_to_map39, string_to_int32 as string_to_int3237, mapped_to_list_with as mapped_to_list_with60, list_for_each as list_for_each40, generic_cmp as generic_cmp61, int_negate as int_negate62, list_filter as list_filter63, listed_sorted as listed_sorted64, list_slice as list_slice65, string_get as string_get34, string_next as string_next35, list_builder_add_all as list_builder_add_all0, Pair as Pair66, map_constructor as map_constructor67, string_split as string_split68
from builtins import int as int17, str as str13, bool as bool15, RuntimeError as RuntimeError22, Exception as Exception42, len as len1, list as list5, tuple as tuple4
from typing import Sequence as Sequence14, Dict as Dict45, MutableSequence as MutableSequence12
from types import MappingProxyType as MappingProxyType46
from ormery.sql import SqlBuilder, SqlFragment
len_5816 = len1
int_add_5817 = int_add3
str_cat_5818 = str_cat10
list_map_5819 = list_map57
list_join_5820 = list_join58
int_to_string_5821 = int_to_string9
list_get_5822 = list_get2
mapped_has_5824 = mapped_has59
list_5825 = list5
map_builder_set_5826 = map_builder_set38
mapped_to_map_5829 = mapped_to_map39
tuple_5831 = tuple4
string_to_int32_5833 = string_to_int3237
mapped_to_list_with_5834 = mapped_to_list_with60
list_for_each_5835 = list_for_each40
generic_cmp_5836 = generic_cmp61
int_negate_5837 = int_negate62
list_filter_5838 = list_filter63
listed_sorted_5839 = listed_sorted64
list_slice_5840 = list_slice65
string_get_5843 = string_get34
string_next_5844 = string_next35
list_builder_add_all_5845 = list_builder_add_all0
pair_5846 = Pair66
map_constructor_5847 = map_constructor67
string_split_5848 = string_split68
console_737: 'LoggingConsole30' = LoggingConsole30(__name__)
class DemoController:
    schema_207: 'Schema'
    store_208: 'InMemoryStore'
    query_count_209: 'int17'
    __slots__ = ('schema_207', 'store_208', 'query_count_209')
    def __init__(this_47, schema_211: 'Schema', store_212: 'InMemoryStore') -> None:
        this_47.schema_207 = schema_211
        this_47.store_208 = store_212
        this_47.query_count_209 = 0
    def get_record_count(this_48) -> 'int17':
        t_3833: 'str13' = this_48.schema_207.table_name
        return this_48.store_208.count(t_3833)
    def get_adult_count(this_49) -> 'int17':
        return len_5816(Query(this_49.schema_207, this_49.store_208).where('age', '>=', '18').all())
    def get_query_count(this_50) -> 'int17':
        return this_50.query_count_209
    def increment_query_count_220(this_51) -> 'None':
        t_734: 'int17' = int_add_5817(this_51.query_count_209, 1)
        this_51.query_count_209 = t_734
    def format_records_222(this_52, records_223: 'Sequence14[Record]') -> 'str13':
        def fn_3824(record_226: 'Record') -> 'str13':
            return str_cat_5818('  ', record_226.describe())
        lines_225: 'Sequence14[str13]' = list_map_5819(records_223, fn_3824)
        def fn_3823(s_228: 'str13') -> 'str13':
            return s_228
        return list_join_5820(lines_225, '\n', fn_3823)
    def run_demo1(this_53) -> 'str13':
        this_53.increment_query_count_220()
        results_232: 'Sequence14[Record]' = Query(this_53.schema_207, this_53.store_208).all()
        formatted_233: 'str13' = this_53.format_records_222(results_232)
        return str_cat_5818('=== Demo 1: All Users ===', '\n', '\n', 'Query: new Query(userSchema, store).all()', '\n', '\n', 'Results:', '\n', formatted_233, '\n', '\n', 'Total: ', int_to_string_5821(len_5816(results_232)), ' records')
    def run_demo2(this_54) -> 'str13':
        this_54.increment_query_count_220()
        results_236: 'Sequence14[Record]' = Query(this_54.schema_207, this_54.store_208).where('age', '>=', '18').all()
        formatted_237: 'str13' = this_54.format_records_222(results_236)
        return str_cat_5818('=== Demo 2: Filter Adults ===', '\n', '\n', 'Query: new Query(userSchema, store)', '\n', '  .where(', '"', 'age', '"', ', ', '"', '>=', '"', ', ', '"', '18', '"', ')', '\n', '  .all()', '\n', '\n', 'Results:', '\n', formatted_237, '\n', '\n', 'Total: ', int_to_string_5821(len_5816(results_236)), ' adults found')
    def run_demo3(this_55) -> 'str13':
        this_55.increment_query_count_220()
        results_240: 'Sequence14[Record]' = Query(this_55.schema_207, this_55.store_208).order_by('age', 'desc').all()
        formatted_241: 'str13' = this_55.format_records_222(results_240)
        return str_cat_5818('=== Demo 3: Sort by Age (Descending) ===', '\n', '\n', 'Query: new Query(userSchema, store)', '\n', '  .orderBy(', '"', 'age', '"', ', ', '"', 'desc', '"', ')', '\n', '  .all()', '\n', '\n', 'Results (ordered by age, oldest first):', '\n', formatted_241)
    def run_demo4(this_56) -> 'str13':
        this_56.increment_query_count_220()
        page1_244: 'Sequence14[Record]' = Query(this_56.schema_207, this_56.store_208).order_by('id', 'asc').limit(2).all()
        page2_245: 'Sequence14[Record]' = Query(this_56.schema_207, this_56.store_208).order_by('id', 'asc').offset(2).limit(2).all()
        formatted1_246: 'str13' = this_56.format_records_222(page1_244)
        formatted2_247: 'str13' = this_56.format_records_222(page2_245)
        return str_cat_5818('=== Demo 4: Pagination ===', '\n', '\n', 'Page 1: .orderBy(', '"', 'id', '"', ', ', '"', 'asc', '"', ').limit(2)', '\n', '\n', formatted1_246, '\n', '\n', 'Page 2: .orderBy(', '"', 'id', '"', ', ', '"', 'asc', '"', ').offset(2).limit(2)', '\n', '\n', formatted2_247)
    def run_demo5(this_57) -> 'str13':
        this_57.increment_query_count_220()
        results_250: 'Sequence14[Record]' = Query(this_57.schema_207, this_57.store_208).where('age', '>=', '18').where('email', '!=', '').order_by('age', 'desc').select(('name', 'age')).limit(2).all()
        formatted_251: 'str13' = this_57.format_records_222(results_250)
        return str_cat_5818('=== Demo 5: Complex Query ===', '\n', '\n', 'Query: new Query(userSchema, store)', '\n', '  .where(', '"', 'age', '"', ', ', '"', '>=', '"', ', ', '"', '18', '"', ')', '\n', '  .where(', '"', 'email', '"', ', ', '"', '!=', '"', ', ', '"', '"', ')', '\n', '  .orderBy(', '"', 'age', '"', ', ', '"', 'desc', '"', ')', '\n', '  .select([', '"', 'name', '"', ', ', '"', 'age', '"', '])', '\n', '  .limit(2)', '\n', '  .all()', '\n', '\n', 'Results (adults with email, showing name/age only, oldest first, max 2):', '\n', formatted_251)
    @property
    def schema(this_819) -> 'Schema':
        return this_819.schema_207
    @property
    def store(this_822) -> 'InMemoryStore':
        return this_822.store_208
class Field:
    name_252: 'str13'
    field_type_253: 'str13'
    primary_key_254: 'bool15'
    nullable_255: 'bool15'
    __slots__ = ('name_252', 'field_type_253', 'primary_key_254', 'nullable_255')
    @property
    def description(this_58) -> 'str13':
        pk_258: 'str13'
        if this_58.primary_key_254:
            pk_258 = ' (PK)'
        else:
            pk_258 = ''
        null_259: 'str13'
        if this_58.nullable_255:
            null_259 = ' (nullable)'
        else:
            null_259 = ''
        return str_cat_5818(this_58.name_252, ': ', this_58.field_type_253, pk_258, null_259)
    def __init__(this_109, name_261: 'str13', field_type_262: 'str13', primary_key_263: 'bool15', nullable_264: 'bool15') -> None:
        this_109.name_252 = name_261
        this_109.field_type_253 = field_type_262
        this_109.primary_key_254 = primary_key_263
        this_109.nullable_255 = nullable_264
    @property
    def name(this_739) -> 'str13':
        return this_739.name_252
    @property
    def field_type(this_742) -> 'str13':
        return this_742.field_type_253
    @property
    def primary_key(this_745) -> 'bool15':
        return this_745.primary_key_254
    @property
    def nullable(this_748) -> 'bool15':
        return this_748.nullable_255
class Schema:
    table_name_265: 'str13'
    fields_266: 'Sequence14[Field]'
    __slots__ = ('table_name_265', 'fields_266')
    def get_field(this_59, name_268: 'str13') -> 'Field':
        return_117: 'Field'
        with Label41() as fn_269:
            this_2501: 'Sequence14[Field]' = this_59.fields_266
            n_2502: 'int17' = len_5816(this_2501)
            i_2503: 'int17' = 0
            while i_2503 < n_2502:
                el_2504: 'Field' = list_get_5822(this_2501, i_2503)
                i_2503 = int_add_5817(i_2503, 1)
                field_270: 'Field' = el_2504
                if field_270.name == name_268:
                    return_117 = field_270
                    fn_269.break_()
            raise RuntimeError22()
        return return_117
    def has_field(this_60, name_272: 'str13') -> 'bool15':
        return_118: 'bool15'
        with Label41() as fn_273:
            this_2506: 'Sequence14[Field]' = this_60.fields_266
            n_2507: 'int17' = len_5816(this_2506)
            i_2508: 'int17' = 0
            while i_2508 < n_2507:
                el_2509: 'Field' = list_get_5822(this_2506, i_2508)
                i_2508 = int_add_5817(i_2508, 1)
                field_274: 'Field' = el_2509
                if field_274.name == name_272:
                    return_118 = True
                    fn_273.break_()
            return_118 = False
        return return_118
    @property
    def primary_key_field(this_61) -> 'Field':
        return_119: 'Field'
        with Label41() as fn_276:
            this_2511: 'Sequence14[Field]' = this_61.fields_266
            n_2512: 'int17' = len_5816(this_2511)
            i_2513: 'int17' = 0
            while i_2513 < n_2512:
                el_2514: 'Field' = list_get_5822(this_2511, i_2513)
                i_2513 = int_add_5817(i_2513, 1)
                field_277: 'Field' = el_2514
                if field_277.primary_key:
                    return_119 = field_277
                    fn_276.break_()
            raise RuntimeError22()
        return return_119
    @property
    def field_names(this_62) -> 'Sequence14[str13]':
        def fn_4076(f_280: 'Field') -> 'str13':
            return f_280.name
        return list_map_5819(this_62.fields_266, fn_4076)
    def describe(this_63) -> 'str13':
        header_284: 'str13' = str_cat_5818('Schema: ', this_63.table_name_265, '\n')
        def fn_4070(f_286: 'Field') -> 'str13':
            return str_cat_5818('  - ', f_286.description)
        t_4072: 'Sequence14[str13]' = list_map_5819(this_63.fields_266, fn_4070)
        def fn_4069(s_288: 'str13') -> 'str13':
            return s_288
        field_list_285: 'str13' = list_join_5820(t_4072, '\n', fn_4069)
        return str_cat_5818(header_284, field_list_285)
    def __init__(this_114, table_name_291: 'str13', fields_292: 'Sequence14[Field]') -> None:
        this_114.table_name_265 = table_name_291
        this_114.fields_266 = fields_292
    @property
    def table_name(this_751) -> 'str13':
        return this_751.table_name_265
    @property
    def fields(this_754) -> 'Sequence14[Field]':
        return this_754.fields_266
class InMemoryStore:
    tables_330: 'Dict45[str13, (MutableSequence12[Record])]'
    next_ids_331: 'Dict45[str13, int17]'
    __slots__ = ('tables_330', 'next_ids_331')
    def __init__(this_69) -> None:
        t_4058: 'Dict45[str13, (MutableSequence12[Record])]' = {}
        this_69.tables_330 = t_4058
        t_4059: 'Dict45[str13, int17]' = {}
        this_69.next_ids_331 = t_4059
    def ensure_table_334(this_70, table_name_335: 'str13') -> 'None':
        t_4055: 'MutableSequence12[Record]'
        if not mapped_has_5824(this_70.tables_330, table_name_335):
            t_4055 = list_5825()
            map_builder_set_5826(this_70.tables_330, table_name_335, t_4055)
            map_builder_set_5826(this_70.next_ids_331, table_name_335, 1)
    def insert(this_71, table_name_338: 'str13', data_339: 'MappingProxyType46[str13, str13]') -> 'Record':
        this_71.ensure_table_334(table_name_338)
        id_341: 'int17' = this_71.next_ids_331.get(table_name_338, 1)
        map_builder_set_5826(this_71.next_ids_331, table_name_338, int_add_5817(id_341, 1))
        data_builder_342: 'Dict45[str13, str13]' = dict(data_339)
        map_builder_set_5826(data_builder_342, 'id', int_to_string_5821(id_341))
        record_343: 'Record' = Record(mapped_to_map_5829(data_builder_342))
        t_4051: 'MutableSequence12[Record]' = list_5825()
        table_344: 'MutableSequence12[Record]' = this_71.tables_330.get(table_name_338, t_4051)
        table_344.append(record_343)
        return record_343
    def all(this_72, table_name_346: 'str13') -> 'Sequence14[Record]':
        this_72.ensure_table_334(table_name_346)
        t_4040: 'MutableSequence12[Record]' = list_5825()
        table_348: 'MutableSequence12[Record]' = this_72.tables_330.get(table_name_346, t_4040)
        return tuple_5831(table_348)
    def get(this_73, table_name_350: 'str13', id_351: 'int17') -> 'Record':
        return_138: 'Record'
        t_4034: 'MutableSequence12[Record]'
        with Label41() as fn_352:
            this_73.ensure_table_334(table_name_350)
            t_4034 = list_5825()
            table_353: 'MutableSequence12[Record]' = this_73.tables_330.get(table_name_350, t_4034)
            this_2516: 'Sequence14[Record]' = tuple_5831(table_353)
            n_2517: 'int17' = len_5816(this_2516)
            i_2518: 'int17' = 0
            while i_2518 < n_2517:
                el_2519: 'Record' = list_get_5822(this_2516, i_2518)
                i_2518 = int_add_5817(i_2518, 1)
                record_354: 'Record' = el_2519
                record_id_355: 'int17'
                record_id_355 = record_354.id
                if record_id_355 == id_351:
                    return_138 = record_354
                    fn_352.break_()
            raise RuntimeError22()
        return return_138
    def count(this_74, table_name_357: 'str13') -> 'int17':
        this_74.ensure_table_334(table_name_357)
        t_4030: 'MutableSequence12[Record]' = list_5825()
        table_359: 'MutableSequence12[Record]' = this_74.tables_330.get(table_name_357, t_4030)
        return len_5816(table_359)
class Record:
    data_306: 'MappingProxyType46[str13, str13]'
    __slots__ = ('data_306',)
    def get(this_64, field_308: 'str13') -> 'str13':
        return this_64.data_306[field_308]
    def get_or(this_65, field_311: 'str13', fallback_312: 'str13') -> 'str13':
        return this_65.data_306.get(field_311, fallback_312)
    def has(this_66, field_315: 'str13') -> 'bool15':
        return mapped_has_5824(this_66.data_306, field_315)
    @property
    def id(this_67) -> 'int17':
        id_str_319: 'str13'
        id_str_319 = this_67.data_306['id']
        return string_to_int32_5833(id_str_319)
    def describe(this_68) -> 'str13':
        def fn_4061(k_323: 'str13', v_324: 'str13') -> 'str13':
            return str_cat_5818(k_323, ': ', v_324)
        pairs_322: 'Sequence14[str13]' = mapped_to_list_with_5834(this_68.data_306, fn_4061)
        def fn_4060(s_326: 'str13') -> 'str13':
            return s_326
        return list_join_5820(pairs_322, ', ', fn_4060)
    def __init__(this_126, data_329: 'MappingProxyType46[str13, str13]') -> None:
        this_126.data_306 = data_329
    @property
    def data(this_757) -> 'MappingProxyType46[str13, str13]':
        return this_757.data_306
class Query:
    schema_376: 'Schema'
    store_377: 'InMemoryStore'
    where_clauses_378: 'MutableSequence12[WhereClause]'
    select_fields_379: 'Sequence14[str13]'
    order_by_clauses_380: 'MutableSequence12[OrderClause]'
    limit_value_381: 'int17'
    offset_value_382: 'int17'
    __slots__ = ('schema_376', 'store_377', 'where_clauses_378', 'select_fields_379', 'order_by_clauses_380', 'limit_value_381', 'offset_value_382')
    def __init__(this_77, schema_384: 'Schema', store_385: 'InMemoryStore') -> None:
        this_77.schema_376 = schema_384
        this_77.store_377 = store_385
        t_3898: 'MutableSequence12[WhereClause]' = list_5825()
        this_77.where_clauses_378 = t_3898
        t_2220: 'Sequence14[str13]' = ()
        this_77.select_fields_379 = t_2220
        t_3899: 'MutableSequence12[OrderClause]' = list_5825()
        this_77.order_by_clauses_380 = t_3899
        this_77.limit_value_381 = -1
        this_77.offset_value_382 = 0
    def where(this_78, field_388: 'str13', operator_389: 'str13', value_390: 'str13') -> 'Query':
        t_3896: 'WhereClause' = WhereClause(field_388, operator_389, value_390)
        this_78.where_clauses_378.append(t_3896)
        return this_78
    def select(this_79, fields_393: 'Sequence14[str13]') -> 'Query':
        this_79.select_fields_379 = fields_393
        return this_79
    def order_by(this_80, field_396: 'str13', direction_397: 'str13') -> 'Query':
        t_3894: 'OrderClause' = OrderClause(field_396, direction_397)
        this_80.order_by_clauses_380.append(t_3894)
        return this_80
    def limit(this_81, n_400: 'int17') -> 'Query':
        t_2209: 'int17'
        if n_400 < 0:
            t_2209 = 0
        else:
            t_2209 = n_400
        this_81.limit_value_381 = t_2209
        return this_81
    def offset(this_82, n_403: 'int17') -> 'Query':
        this_82.offset_value_382 = n_403
        return this_82
    def matches_where_405(this_83, record_406: 'Record') -> 'bool15':
        return_152: 'bool15'
        t_3883: 'str13'
        t_3885: 'str13'
        t_3887: 'str13'
        t_3889: 'str13'
        t_3890: 'str13'
        t_3891: 'bool15'
        t_3892: 'str13'
        t_3893: 'str13'
        with Label41() as fn_407:
            this_2521: 'Sequence14[WhereClause]' = tuple_5831(this_83.where_clauses_378)
            n_2522: 'int17' = len_5816(this_2521)
            i_2523: 'int17' = 0
            while i_2523 < n_2522:
                el_2524: 'WhereClause' = list_get_5822(this_2521, i_2523)
                i_2523 = int_add_5817(i_2523, 1)
                clause_408: 'WhereClause' = el_2524
                t_3883 = clause_408.field
                record_value_409: 'str13' = record_406.get_or(t_3883, '')
                t_3885 = clause_408.field
                if not this_83.schema_376.has_field(t_3885):
                    return_152 = False
                    fn_407.break_()
                t_3887 = clause_408.field
                t_2198: 'Field'
                t_2198 = this_83.schema_376.get_field(t_3887)
                field_info_410: 'Field' = t_2198
                field_type_411: 'str13' = field_info_410.field_type
                matches_412: 'bool15'
                if field_type_411 == 'Int':
                    t_3889 = clause_408.operator
                    t_3890 = clause_408.value
                    t_3891 = compare_int_195(record_value_409, t_3889, t_3890)
                    matches_412 = t_3891
                elif field_type_411 == 'String':
                    t_3892 = clause_408.operator
                    t_3893 = clause_408.value
                    matches_412 = compare_string_196(record_value_409, t_3892, t_3893)
                else:
                    matches_412 = False
                if not matches_412:
                    return_152 = False
                    fn_407.break_()
            return_152 = True
        return return_152
    def project_record_413(this_84, record_414: 'Record') -> 'Record':
        return_153: 'Record'
        t_3878: 'MappingProxyType46[str13, str13]'
        with Label41() as fn_415:
            if len_5816(this_84.select_fields_379) == 0:
                return_153 = record_414
                fn_415.break_()
            builder_416: 'Dict45[str13, str13]' = {}
            def fn_3873(field_name_417: 'str13') -> 'None':
                value_418: 'str13' = record_414.get_or(field_name_417, '')
                map_builder_set_5826(builder_416, field_name_417, value_418)
            list_for_each_5835(this_84.select_fields_379, fn_3873)
            t_3878 = mapped_to_map_5829(builder_416)
            return_153 = Record(t_3878)
        return return_153
    def compare_records_419(this_85, a_420: 'Record', b_421: 'Record', order_clauses_422: 'Sequence14[OrderClause]') -> 'int17':
        return_154: 'int17'
        t_3862: 'str13'
        t_3864: 'str13'
        t_3866: 'str13'
        t_3868: 'str13'
        with Label41() as fn_423:
            this_2526: 'Sequence14[OrderClause]' = order_clauses_422
            n_2527: 'int17' = len_5816(this_2526)
            i_2528: 'int17' = 0
            while i_2528 < n_2527:
                el_2529: 'OrderClause' = list_get_5822(this_2526, i_2528)
                i_2528 = int_add_5817(i_2528, 1)
                clause_424: 'OrderClause' = el_2529
                t_2177: 'int17'
                t_2179: 'int17'
                t_3862 = clause_424.field
                a_val_425: 'str13' = a_420.get_or(t_3862, '')
                t_3864 = clause_424.field
                b_val_426: 'str13' = b_421.get_or(t_3864, '')
                t_3866 = clause_424.field
                if not this_85.schema_376.has_field(t_3866):
                    continue
                t_3868 = clause_424.field
                t_2174: 'Field'
                t_2174 = this_85.schema_376.get_field(t_3868)
                field_info_427: 'Field' = t_2174
                field_type_428: 'str13' = field_info_427.field_type
                cmp_429: 'int17'
                if field_type_428 == 'Int':
                    a_int_430: 'int17'
                    try:
                        t_2177 = string_to_int32_5833(a_val_425)
                        a_int_430 = t_2177
                    except Exception42:
                        a_int_430 = 0
                    b_int_431: 'int17'
                    try:
                        t_2179 = string_to_int32_5833(b_val_426)
                        b_int_431 = t_2179
                    except Exception42:
                        b_int_431 = 0
                    cmp_429 = generic_cmp_5836(a_int_430, b_int_431)
                elif field_type_428 == 'String':
                    cmp_429 = generic_cmp_5836(a_val_425, b_val_426)
                else:
                    cmp_429 = 0
                if cmp_429 != 0:
                    if clause_424.direction == 'desc':
                        return_154 = int_negate_5837(cmp_429)
                    else:
                        return_154 = cmp_429
                    fn_423.break_()
            return_154 = 0
        return return_154
    def all(this_86) -> 'Sequence14[Record]':
        t_3853: 'Sequence14[Record]'
        t_3854: 'Sequence14[Record]'
        t_3855: 'int17'
        t_3856: 'int17'
        t_3857: 'Sequence14[Record]'
        t_3846: 'str13' = this_86.schema_376.table_name
        all_records_434: 'Sequence14[Record]' = this_86.store_377.all(t_3846)
        def fn_3845(r_436: 'Record') -> 'bool15':
            return this_86.matches_where_405(r_436)
        filtered_435: 'Sequence14[Record]' = list_filter_5838(all_records_434, fn_3845)
        sorted_438: 'Sequence14[Record]'
        if len_5816(this_86.order_by_clauses_380) > 0:
            clauses_439: 'Sequence14[OrderClause]' = tuple_5831(this_86.order_by_clauses_380)
            def fn_3844(a_440: 'Record', b_441: 'Record') -> 'int17':
                return this_86.compare_records_419(a_440, b_441, clauses_439)
            t_3853 = listed_sorted_5839(filtered_435, fn_3844)
            sorted_438 = t_3853
        else:
            sorted_438 = filtered_435
        sliced_443: 'Sequence14[Record]'
        if this_86.limit_value_381 >= 0:
            start_444: 'int17' = this_86.offset_value_382
            end_445: 'int17' = int_add_5817(this_86.offset_value_382, this_86.limit_value_381)
            t_3854 = list_slice_5840(sorted_438, start_444, end_445)
            sliced_443 = t_3854
        elif this_86.offset_value_382 > 0:
            t_3856 = this_86.offset_value_382
            t_3855 = len_5816(sorted_438)
            t_3857 = list_slice_5840(sorted_438, t_3856, t_3855)
            sliced_443 = t_3857
        else:
            sliced_443 = sorted_438
        def fn_3843(r_446: 'Record') -> 'Record':
            return this_86.project_record_413(r_446)
        return list_map_5819(sliced_443, fn_3843)
    def to_sql(this_87) -> 'SqlFragment':
        return to_sql_query(this_87.schema_376, this_87.select_fields_379, tuple_5831(this_87.where_clauses_378), tuple_5831(this_87.order_by_clauses_380), this_87.limit_value_381, this_87.offset_value_382)
    @property
    def schema(this_809) -> 'Schema':
        return this_809.schema_376
    @property
    def store(this_812) -> 'InMemoryStore':
        return this_812.store_377
class WhereClause:
    field_360: 'str13'
    operator_361: 'str13'
    value_362: 'str13'
    __slots__ = ('field_360', 'operator_361', 'value_362')
    def describe(this_75) -> 'str13':
        return str_cat_5818(this_75.field_360, ' ', this_75.operator_361, ' ', this_75.value_362)
    def __init__(this_140, field_366: 'str13', operator_367: 'str13', value_368: 'str13') -> None:
        this_140.field_360 = field_366
        this_140.operator_361 = operator_367
        this_140.value_362 = value_368
    @property
    def field(this_760) -> 'str13':
        return this_760.field_360
    @property
    def operator(this_763) -> 'str13':
        return this_763.operator_361
    @property
    def value(this_766) -> 'str13':
        return this_766.value_362
class OrderClause:
    field_369: 'str13'
    direction_370: 'str13'
    __slots__ = ('field_369', 'direction_370')
    def describe(this_76) -> 'str13':
        return str_cat_5818(this_76.field_369, ' ', this_76.direction_370)
    def __init__(this_143, field_374: 'str13', direction_375: 'str13') -> None:
        this_143.field_369 = field_374
        this_143.direction_370 = direction_375
    @property
    def field(this_769) -> 'str13':
        return this_769.field_369
    @property
    def direction(this_772) -> 'str13':
        return this_772.direction_370
def compare_int_195(record_value_450: 'str13', operator_451: 'str13', clause_value_452: 'str13') -> 'bool15':
    return_157: 'bool15'
    t_4028: 'str13'
    t_2376: 'int17'
    t_2378: 'int17'
    with Label41() as fn_453:
        rv_454: 'int17'
        try:
            t_2376 = string_to_int32_5833(record_value_450)
            rv_454 = t_2376
        except Exception42:
            rv_454 = 0
        cv_455: 'int17'
        try:
            t_2378 = string_to_int32_5833(clause_value_452)
            cv_455 = t_2378
        except Exception42:
            cv_455 = 0
        t_4028 = int_to_string_5821(cv_455)
        if clause_value_452 != t_4028:
            return_157 = False
            fn_453.break_()
        if operator_451 == '==':
            return_157 = rv_454 == cv_455
        elif operator_451 == '!=':
            return_157 = rv_454 != cv_455
        elif operator_451 == '>':
            return_157 = rv_454 > cv_455
        elif operator_451 == '<':
            return_157 = rv_454 < cv_455
        elif operator_451 == '>=':
            return_157 = rv_454 >= cv_455
        elif operator_451 == '<=':
            return_157 = rv_454 <= cv_455
        else:
            return_157 = False
    return return_157
def compare_string_196(record_value_456: 'str13', operator_457: 'str13', clause_value_458: 'str13') -> 'bool15':
    return_158: 'bool15'
    if operator_457 == '==':
        return_158 = record_value_456 == clause_value_458
    elif operator_457 == '!=':
        return_158 = record_value_456 != clause_value_458
    elif operator_457 == '>':
        return_158 = record_value_456 > clause_value_458
    elif operator_457 == '<':
        return_158 = record_value_456 < clause_value_458
    elif operator_457 == '>=':
        return_158 = record_value_456 >= clause_value_458
    elif operator_457 == '<=':
        return_158 = record_value_456 <= clause_value_458
    else:
        return_158 = False
    return return_158
def safe_sql_198(trusted_462: 'str13') -> 'SqlFragment':
    b_464: 'SqlBuilder' = SqlBuilder()
    b_464.append_safe(trusted_462)
    return b_464.accumulated
def column_list_sql_199(select_fields_465: 'Sequence14[str13]') -> 'SqlFragment':
    return_161: 'SqlFragment'
    t_4009: 'SqlBuilder'
    t_4012: 'str13'
    t_4014: 'SqlBuilder'
    t_4016: 'SqlFragment'
    t_4017: 'int17'
    t_4018: 'str13'
    t_4020: 'SqlBuilder'
    t_4024: 'SqlFragment'
    if len_5816(select_fields_465) == 0:
        t_4009 = SqlBuilder()
        t_4009.append_safe('*')
        return_161 = t_4009.accumulated
    else:
        t_4012 = list_get_5822(select_fields_465, 0)
        first_467: 'SqlFragment' = safe_sql_198(t_4012)
        t_4014 = SqlBuilder()
        t_4014.append_fragment(first_467)
        t_4016 = t_4014.accumulated
        result_468: 'SqlFragment' = t_4016
        i_469: 'int17' = 1
        while True:
            t_4017 = len_5816(select_fields_465)
            if not i_469 < t_4017:
                break
            t_4018 = list_get_5822(select_fields_465, i_469)
            col_470: 'SqlFragment' = safe_sql_198(t_4018)
            t_4020 = SqlBuilder()
            t_4020.append_fragment(result_468)
            t_4020.append_safe(', ')
            t_4020.append_fragment(col_470)
            t_4024 = t_4020.accumulated
            result_468 = t_4024
            i_469 = int_add_5817(i_469, 1)
        return_161 = result_468
    return return_161
def valid_operator_197(op_460: 'str13') -> 'str13':
    return_159: 'str13'
    if op_460 == '=':
        return_159 = '='
    elif op_460 == '==':
        return_159 = '='
    elif op_460 == '!=':
        return_159 = '!='
    elif op_460 == '<>':
        return_159 = '<>'
    elif op_460 == '>':
        return_159 = '>'
    elif op_460 == '<':
        return_159 = '<'
    elif op_460 == '>=':
        return_159 = '>='
    elif op_460 == '<=':
        return_159 = '<='
    else:
        return_159 = '='
    return return_159
def where_condition_sql_200(clause_471: 'WhereClause', schema_472: 'Schema') -> 'SqlFragment':
    return_162: 'SqlFragment'
    t_3990: 'SqlBuilder'
    t_3993: 'SqlBuilder'
    t_4001: 'SqlBuilder'
    t_2320: 'int17'
    t_3981: 'str13' = clause_471.field
    col_474: 'SqlFragment' = safe_sql_198(t_3981)
    t_3983: 'str13' = clause_471.operator
    op_475: 'SqlFragment' = safe_sql_198(valid_operator_197(t_3983))
    t_3985: 'str13' = clause_471.field
    t_2316: 'Field'
    t_2316 = schema_472.get_field(t_3985)
    field_info_476: 'Field' = t_2316
    if field_info_476.field_type == 'Int':
        int_val_477: 'int17'
        try:
            t_2320 = string_to_int32_5833(clause_471.value)
            int_val_477 = t_2320
        except Exception42:
            int_val_477 = 0
        if clause_471.value != int_to_string_5821(int_val_477):
            t_3990 = SqlBuilder()
            t_3990.append_safe('1 = 0')
            return_162 = t_3990.accumulated
        else:
            t_3993 = SqlBuilder()
            t_3993.append_fragment(col_474)
            t_3993.append_safe(' ')
            t_3993.append_fragment(op_475)
            t_3993.append_safe(' ')
            t_3993.append_int32(int_val_477)
            return_162 = t_3993.accumulated
    else:
        str_val_478: 'str13' = clause_471.value
        t_4001 = SqlBuilder()
        t_4001.append_fragment(col_474)
        t_4001.append_safe(' ')
        t_4001.append_fragment(op_475)
        t_4001.append_safe(' ')
        t_4001.append_string(str_val_478)
        return_162 = t_4001.accumulated
    return return_162
def order_by_sql_201(clauses_479: 'Sequence14[OrderClause]') -> 'SqlFragment':
    t_3961: 'SqlFragment'
    t_3962: 'SqlFragment'
    t_3967: 'int17'
    t_3969: 'str13'
    t_3973: 'SqlFragment'
    t_3974: 'SqlFragment'
    t_3975: 'SqlBuilder'
    t_3980: 'SqlFragment'
    t_2303: 'SqlFragment'
    t_3957: 'str13' = list_get_5822(clauses_479, 0).field
    first_481: 'SqlFragment' = safe_sql_198(t_3957)
    first_dir_482: 'SqlFragment'
    if list_get_5822(clauses_479, 0).direction == 'desc':
        t_3961 = safe_sql_198(' DESC')
        first_dir_482 = t_3961
    else:
        t_3962 = safe_sql_198(' ASC')
        first_dir_482 = t_3962
    t_3963: 'SqlBuilder' = SqlBuilder()
    t_3963.append_fragment(first_481)
    t_3963.append_fragment(first_dir_482)
    t_3966: 'SqlFragment' = t_3963.accumulated
    result_483: 'SqlFragment' = t_3966
    i_484: 'int17' = 1
    while True:
        t_3967 = len_5816(clauses_479)
        if not i_484 < t_3967:
            break
        t_3969 = list_get_5822(clauses_479, i_484).field
        col_485: 'SqlFragment' = safe_sql_198(t_3969)
        if list_get_5822(clauses_479, i_484).direction == 'desc':
            t_3973 = safe_sql_198(' DESC')
            t_2303 = t_3973
        else:
            t_3974 = safe_sql_198(' ASC')
            t_2303 = t_3974
        dir_486: 'SqlFragment' = t_2303
        t_3975 = SqlBuilder()
        t_3975.append_fragment(result_483)
        t_3975.append_safe(', ')
        t_3975.append_fragment(col_485)
        t_3975.append_fragment(dir_486)
        t_3980 = t_3975.accumulated
        result_483 = t_3980
        i_484 = int_add_5817(i_484, 1)
    return result_483
def to_sql_query(schema_487: 'Schema', select_fields_488: 'Sequence14[str13]', where_clauses_489: 'Sequence14[WhereClause]', order_clauses_490: 'Sequence14[OrderClause]', limit_value_491: 'int17', offset_value_492: 'int17') -> 'SqlFragment':
    t_3924: 'WhereClause'
    t_3925: 'SqlFragment'
    t_3926: 'int17'
    t_3927: 'WhereClause'
    t_3929: 'SqlBuilder'
    t_3933: 'SqlFragment'
    t_3934: 'SqlBuilder'
    t_3938: 'SqlFragment'
    t_3941: 'SqlBuilder'
    t_3945: 'SqlFragment'
    t_3946: 'SqlBuilder'
    t_3950: 'SqlFragment'
    t_3951: 'SqlBuilder'
    t_3955: 'SqlFragment'
    def fn_3907(f_495: 'str13') -> 'bool15':
        return schema_487.has_field(f_495)
    valid_select_494: 'Sequence14[str13]' = list_filter_5838(select_fields_488, fn_3907)
    def fn_3906(c_498: 'WhereClause') -> 'bool15':
        t_3902: 'str13' = c_498.field
        return schema_487.has_field(t_3902)
    valid_where_497: 'Sequence14[WhereClause]' = list_filter_5838(where_clauses_489, fn_3906)
    def fn_3905(c_501: 'OrderClause') -> 'bool15':
        t_3900: 'str13' = c_501.field
        return schema_487.has_field(t_3900)
    valid_order_500: 'Sequence14[OrderClause]' = list_filter_5838(order_clauses_490, fn_3905)
    t_3914: 'str13' = schema_487.table_name
    table_503: 'SqlFragment' = safe_sql_198(t_3914)
    cols_504: 'SqlFragment' = column_list_sql_199(valid_select_494)
    t_3917: 'SqlBuilder' = SqlBuilder()
    t_3917.append_safe('SELECT ')
    t_3917.append_fragment(cols_504)
    t_3917.append_safe(' FROM ')
    t_3917.append_fragment(table_503)
    t_3922: 'SqlFragment' = t_3917.accumulated
    result_505: 'SqlFragment' = t_3922
    if len_5816(valid_where_497) > 0:
        t_3924 = list_get_5822(valid_where_497, 0)
        t_3925 = where_condition_sql_200(t_3924, schema_487)
        conditions_506: 'SqlFragment' = t_3925
        i_507: 'int17' = 1
        while True:
            t_3926 = len_5816(valid_where_497)
            if not i_507 < t_3926:
                break
            t_3927 = list_get_5822(valid_where_497, i_507)
            next_508: 'SqlFragment' = where_condition_sql_200(t_3927, schema_487)
            t_3929 = SqlBuilder()
            t_3929.append_fragment(conditions_506)
            t_3929.append_safe(' AND ')
            t_3929.append_fragment(next_508)
            t_3933 = t_3929.accumulated
            conditions_506 = t_3933
            i_507 = int_add_5817(i_507, 1)
        t_3934 = SqlBuilder()
        t_3934.append_fragment(result_505)
        t_3934.append_safe(' WHERE ')
        t_3934.append_fragment(conditions_506)
        t_3938 = t_3934.accumulated
        result_505 = t_3938
    if len_5816(valid_order_500) > 0:
        ordering_509: 'SqlFragment' = order_by_sql_201(valid_order_500)
        t_3941 = SqlBuilder()
        t_3941.append_fragment(result_505)
        t_3941.append_safe(' ORDER BY ')
        t_3941.append_fragment(ordering_509)
        t_3945 = t_3941.accumulated
        result_505 = t_3945
    if limit_value_491 >= 0:
        t_3946 = SqlBuilder()
        t_3946.append_fragment(result_505)
        t_3946.append_safe(' LIMIT ')
        t_3946.append_int32(limit_value_491)
        t_3950 = t_3946.accumulated
        result_505 = t_3950
    if offset_value_492 > 0:
        t_3951 = SqlBuilder()
        t_3951.append_fragment(result_505)
        t_3951.append_safe(' OFFSET ')
        t_3951.append_int32(offset_value_492)
        t_3955 = t_3951.accumulated
        result_505 = t_3955
    return result_505
class TokenType:
    name_657: 'str13'
    __slots__ = ('name_657',)
    @property
    def is_keyword(this_88) -> 'bool15':
        return this_88.name_657 == 'keyword'
    @property
    def is_type(this_89) -> 'bool15':
        return this_89.name_657 == 'type'
    @property
    def is_string(this_90) -> 'bool15':
        return this_90.name_657 == 'string'
    @property
    def is_number(this_91) -> 'bool15':
        return this_91.name_657 == 'number'
    @property
    def is_comment(this_92) -> 'bool15':
        return this_92.name_657 == 'comment'
    @property
    def is_operator(this_93) -> 'bool15':
        return this_93.name_657 == 'operator'
    @property
    def is_identifier(this_94) -> 'bool15':
        return this_94.name_657 == 'identifier'
    def __init__(this_174, name_673: 'str13') -> None:
        this_174.name_657 = name_673
    @property
    def name(this_917) -> 'str13':
        return this_917.name_657
class Token:
    token_type_674: 'TokenType'
    value_675: 'str13'
    __slots__ = ('token_type_674', 'value_675')
    def css_class(this_95) -> 'str13':
        return_185: 'str13'
        name_678: 'str13' = this_95.token_type_674.name
        if name_678 == 'keyword':
            return_185 = 'kw'
        elif name_678 == 'type':
            return_185 = 'typ'
        elif name_678 == 'string':
            return_185 = 'str'
        elif name_678 == 'number':
            return_185 = 'num'
        elif name_678 == 'comment':
            return_185 = 'cmt'
        elif name_678 == 'operator':
            return_185 = 'op'
        else:
            return_185 = 'id'
        return return_185
    def to_html(this_96) -> 'SafeHtml':
        cls_681: 'str13' = this_96.css_class()
        t_3288: 'SafeHtmlBuilder' = SafeHtmlBuilder()
        t_3288.append_safe("<span class='")
        t_3288.append_string(cls_681)
        t_3288.append_safe("'>")
        t_3288.append_string(this_96.value_675)
        t_3288.append_safe('</span>')
        return t_3288.accumulated
    def __init__(this_183, token_type_683: 'TokenType', value_684: 'str13') -> None:
        this_183.token_type_674 = token_type_683
        this_183.value_675 = value_684
    @property
    def token_type(this_920) -> 'TokenType':
        return this_920.token_type_674
    @property
    def value(this_923) -> 'str13':
        return this_923.value_675
def field(name_293: 'str13', field_type_294: 'str13', primary_key_295: 'bool15', nullable_296: 'bool15') -> 'Field':
    return Field(name_293, field_type_294, primary_key_295, nullable_296)
def is_valid_identifier(name_298: 'str13') -> 'bool15':
    return_123: 'bool15'
    t_3781: 'int17'
    with Label41() as fn_299:
        if not name_298:
            return_123 = False
            fn_299.break_()
        this_2531: 'str13' = name_298
        index_2533: 'int17' = 0
        while True:
            if not len1(this_2531) > index_2533:
                break
            code_point_2534: 'int17' = string_get_5843(this_2531, index_2533)
            c_300: 'int17' = code_point_2534
            if c_300 != 95:
                if c_300 >= 97:
                    if c_300 > 122:
                        return_123 = False
                        fn_299.break_()
                elif c_300 >= 65:
                    if c_300 > 90:
                        return_123 = False
                        fn_299.break_()
                elif c_300 >= 48:
                    if c_300 > 57:
                        return_123 = False
                        fn_299.break_()
                else:
                    return_123 = False
                    fn_299.break_()
            t_3781 = string_next_5844(this_2531, index_2533)
            index_2533 = t_3781
        return_123 = True
    return return_123
def schema(table_name_301: 'str13', fields_302: 'Sequence14[Field]') -> 'Schema':
    if not is_valid_identifier(table_name_301):
        raise RuntimeError22()
    id_field_304: 'Field' = Field('id', 'Int', True, False)
    all_fields_305: 'MutableSequence12[Field]' = list_5825()
    all_fields_305.append(id_field_304)
    list_builder_add_all_5845(all_fields_305, fields_302)
    t_3776: 'Sequence14[Field]' = tuple_5831(all_fields_305)
    return Schema(table_name_301, t_3776)
def to_insert_sql(schema_510: 'Schema', values_511: 'MappingProxyType46[str13, str13]') -> 'SqlFragment':
    return_165: 'SqlFragment'
    t_3724: 'str13'
    t_3726: 'Sequence14[Field]'
    t_3730: 'SqlBuilder'
    t_3733: 'Sequence14[str13]'
    t_3736: 'str13'
    t_3740: 'SqlBuilder'
    t_3742: 'SqlFragment'
    t_3743: 'SqlBuilder'
    t_3745: 'SqlFragment'
    t_3746: 'int17'
    t_3748: 'str13'
    t_3752: 'SqlBuilder'
    t_3756: 'SqlFragment'
    t_3757: 'SqlBuilder'
    t_3761: 'SqlFragment'
    t_3762: 'SqlBuilder'
    t_2047: 'int17'
    t_2058: 'SqlFragment'
    t_2065: 'int17'
    t_2066: 'int17'
    with Label41() as fn_512:
        t_3724 = schema_510.table_name
        table_513: 'SqlFragment' = safe_sql_198(t_3724)
        t_3726 = schema_510.fields
        def fn_3723(f_515: 'Field') -> 'bool15':
            t_3720: 'str13' = f_515.name
            return mapped_has_5824(values_511, t_3720)
        field_list_514: 'Sequence14[Field]' = list_filter_5838(t_3726, fn_3723)
        if len_5816(field_list_514) == 0:
            t_3730 = SqlBuilder()
            return_165 = t_3730.accumulated
            fn_512.break_()
        def fn_3722(f_518: 'Field') -> 'str13':
            return f_518.name
        t_3733 = list_map_5819(field_list_514, fn_3722)
        col_names_517: 'SqlFragment' = column_list_sql_199(t_3733)
        t_3736 = list_get_5822(field_list_514, 0).name
        first_val_520: 'str13' = values_511.get(t_3736, '')
        if list_get_5822(field_list_514, 0).field_type == 'Int':
            iv_522: 'int17'
            try:
                t_2047 = string_to_int32_5833(first_val_520)
                iv_522 = t_2047
            except Exception42:
                iv_522 = 0
            t_3740 = SqlBuilder()
            t_3740.append_int32(iv_522)
            t_3742 = t_3740.accumulated
            t_2058 = t_3742
        else:
            t_3743 = SqlBuilder()
            t_3743.append_string(first_val_520)
            t_3745 = t_3743.accumulated
            t_2058 = t_3745
        vals_521: 'SqlFragment' = t_2058
        i_523: 'int17' = 1
        while True:
            t_3746 = len_5816(field_list_514)
            if not i_523 < t_3746:
                break
            t_3748 = list_get_5822(field_list_514, i_523).name
            val_524: 'str13' = values_511.get(t_3748, '')
            if list_get_5822(field_list_514, i_523).field_type == 'Int':
                try:
                    t_2065 = string_to_int32_5833(val_524)
                    t_2066 = t_2065
                except Exception42:
                    t_2066 = 0
                iv_525: 'int17' = t_2066
                t_3752 = SqlBuilder()
                t_3752.append_fragment(vals_521)
                t_3752.append_safe(', ')
                t_3752.append_int32(iv_525)
                t_3756 = t_3752.accumulated
                vals_521 = t_3756
            else:
                t_3757 = SqlBuilder()
                t_3757.append_fragment(vals_521)
                t_3757.append_safe(', ')
                t_3757.append_string(val_524)
                t_3761 = t_3757.accumulated
                vals_521 = t_3761
            i_523 = int_add_5817(i_523, 1)
        t_3762 = SqlBuilder()
        t_3762.append_safe('INSERT INTO ')
        t_3762.append_fragment(table_513)
        t_3762.append_safe(' (')
        t_3762.append_fragment(col_names_517)
        t_3762.append_safe(') VALUES (')
        t_3762.append_fragment(vals_521)
        t_3762.append_safe(')')
        return_165 = t_3762.accumulated
    return return_165
def main() -> 'None':
    console_737.log('=== ORMery Demo ===\n')
    user_fields_642: 'Sequence14[Field]' = (field('name', 'String', False, False), field('age', 'Int', False, False), field('email', 'String', False, True))
    user_schema_643: 'Schema' = schema('users', user_fields_642)
    t_3304: 'str13' = user_schema_643.describe()
    console_737.log(t_3304)
    console_737.log('')
    store_644: 'InMemoryStore' = InMemoryStore()
    rec1_645: 'Record' = store_644.insert('users', map_constructor_5847((pair_5846('name', 'Alice'), pair_5846('age', '25'), pair_5846('email', 'alice@example.com'))))
    rec2_646: 'Record' = store_644.insert('users', map_constructor_5847((pair_5846('name', 'Bob'), pair_5846('age', '30'), pair_5846('email', 'bob@example.com'))))
    rec3_647: 'Record' = store_644.insert('users', map_constructor_5847((pair_5846('name', 'Charlie'), pair_5846('age', '17'), pair_5846('email', 'charlie@example.com'))))
    console_737.log('Inserted 3 users:')
    t_3324: 'str13' = rec1_645.describe()
    console_737.log(str_cat_5818('  ', t_3324))
    t_3326: 'str13' = rec2_646.describe()
    console_737.log(str_cat_5818('  ', t_3326))
    t_3328: 'str13' = rec3_647.describe()
    console_737.log(str_cat_5818('  ', t_3328))
    console_737.log('')
    console_737.log('=== In-Memory Queries ===\n')
    console_737.log('All users:')
    all_users_648: 'Sequence14[Record]' = Query(user_schema_643, store_644).all()
    def fn_3301(u_649: 'Record') -> 'None':
        t_3298: 'str13' = u_649.describe()
        console_737.log(str_cat_5818('  ', t_3298))
    list_for_each_5835(all_users_648, fn_3301)
    console_737.log('')
    console_737.log('Adults (age >= 18):')
    adults_650: 'Sequence14[Record]' = Query(user_schema_643, store_644).where('age', '>=', '18').all()
    def fn_3300(u_651: 'Record') -> 'None':
        t_3296: 'str13' = u_651.describe()
        console_737.log(str_cat_5818('  ', t_3296))
    list_for_each_5835(adults_650, fn_3300)
    console_737.log('')
    console_737.log('=== SQL Generation (secure-composition) ===\n')
    q1_652: 'Query' = Query(user_schema_643, store_644)
    t_3348: 'str13' = q1_652.to_sql().to_string()
    console_737.log(str_cat_5818('SELECT all: ', t_3348))
    q2_653: 'Query' = Query(user_schema_643, store_644).select(('name', 'age')).where('age', '>=', '18').order_by('age', 'desc').limit(10)
    t_3356: 'str13' = q2_653.to_sql().to_string()
    console_737.log(str_cat_5818('Complex:    ', t_3356))
    bobby_654: 'str13' = "Robert'); DROP TABLE users;--"
    q3_655: 'Query' = Query(user_schema_643, store_644).where('name', '=', "Robert'); DROP TABLE users;--")
    t_3361: 'str13' = q3_655.to_sql().to_string()
    console_737.log(str_cat_5818('Injection:  ', t_3361))
    insert_vals_656: 'MappingProxyType46[str13, str13]' = map_constructor_5847((pair_5846('name', "O'Malley"), pair_5846('age', '42')))
    t_3367: 'str13' = to_insert_sql(user_schema_643, insert_vals_656).to_string()
    console_737.log(str_cat_5818('INSERT:     ', t_3367))
    console_737.log('\n=== Demo Complete ===')
temper_keywords_204: 'Sequence14[str13]' = ('if', 'else', 'for', 'while', 'do', 'when', 'break', 'continue', 'return', 'let', 'var', 'class', 'export', 'import', 'public', 'private', 'protected', 'throws', 'new', 'this', 'get', 'set', 'static', 'extends', 'implements', 'true', 'false', 'null', 'bubble', 'orelse', 'of')
temper_types_205: 'Sequence14[str13]' = ('String', 'Int', 'Boolean', 'List', 'Map', 'Bubble', 'Pair', 'Float', 'Double', 'Byte', 'Short', 'Long', 'Char', 'Void', 'Record', 'Schema', 'Field', 'Query', 'InMemoryStore', 'ListBuilder', 'MapBuilder', 'WhereClause', 'OrderClause')
def classify_word(word_685: 'str13') -> 'TokenType':
    return_187: 'TokenType'
    with Label41() as fn_686:
        this_2536: 'Sequence14[str13]' = temper_keywords_204
        n_2537: 'int17' = len_5816(this_2536)
        i_2538: 'int17' = 0
        while i_2538 < n_2537:
            el_2539: 'str13' = list_get_5822(this_2536, i_2538)
            i_2538 = int_add_5817(i_2538, 1)
            kw_687: 'str13' = el_2539
            if kw_687 == word_685:
                return_187 = TokenType('keyword')
                fn_686.break_()
        this_2541: 'Sequence14[str13]' = temper_types_205
        n_2542: 'int17' = len_5816(this_2541)
        i_2543: 'int17' = 0
        while i_2543 < n_2542:
            el_2544: 'str13' = list_get_5822(this_2541, i_2543)
            i_2543 = int_add_5817(i_2543, 1)
            tp_688: 'str13' = el_2544
            if tp_688 == word_685:
                return_187 = TokenType('type')
                fn_686.break_()
        return_187 = TokenType('identifier')
    return return_187
def highlight_word(word_689: 'str13') -> 'SafeHtml':
    return_188: 'SafeHtml'
    t_3275: 'SafeHtmlBuilder'
    with Label41() as fn_690:
        if word_689 == '':
            t_3275 = SafeHtmlBuilder()
            return_188 = t_3275.accumulated
            fn_690.break_()
        token_type_691: 'TokenType' = classify_word(word_689)
        token_692: 'Token' = Token(token_type_691, word_689)
        return_188 = token_692.to_html()
    return return_188
def highlight_line(line_693: 'str13') -> 'SafeHtml':
    return_189: 'SafeHtml'
    t_3263: 'SafeHtmlBuilder'
    t_3266: 'SafeHtml'
    t_3267: 'int17'
    t_3270: 'SafeHtmlBuilder'
    t_3274: 'SafeHtml'
    with Label41() as fn_694:
        words_695: 'Sequence14[str13]' = string_split_5848(line_693, ' ')
        if len_5816(words_695) == 0:
            t_3263 = SafeHtmlBuilder()
            return_189 = t_3263.accumulated
            fn_694.break_()
        t_3266 = highlight_word(list_get_5822(words_695, 0))
        result_696: 'SafeHtml' = t_3266
        i_697: 'int17' = 1
        while True:
            t_3267 = len_5816(words_695)
            if not i_697 < t_3267:
                break
            word_698: 'SafeHtml' = highlight_word(list_get_5822(words_695, i_697))
            t_3270 = SafeHtmlBuilder()
            t_3270.append_safe_html(result_696)
            t_3270.append_safe(' ')
            t_3270.append_safe_html(word_698)
            t_3274 = t_3270.accumulated
            result_696 = t_3274
            i_697 = int_add_5817(i_697, 1)
        return_189 = result_696
    return return_189
def highlight_source(source_699: 'str13') -> 'SafeHtml':
    return_190: 'SafeHtml'
    t_3249: 'SafeHtmlBuilder'
    t_3252: 'SafeHtml'
    t_3253: 'int17'
    t_3256: 'SafeHtmlBuilder'
    t_3260: 'SafeHtml'
    with Label41() as fn_700:
        lines_701: 'Sequence14[str13]' = string_split_5848(source_699, '\n')
        if len_5816(lines_701) == 0:
            t_3249 = SafeHtmlBuilder()
            return_190 = t_3249.accumulated
            fn_700.break_()
        t_3252 = highlight_line(list_get_5822(lines_701, 0))
        result_702: 'SafeHtml' = t_3252
        i_703: 'int17' = 1
        while True:
            t_3253 = len_5816(lines_701)
            if not i_703 < t_3253:
                break
            line_704: 'SafeHtml' = highlight_line(list_get_5822(lines_701, i_703))
            t_3256 = SafeHtmlBuilder()
            t_3256.append_safe_html(result_702)
            t_3256.append_safe('\\n')
            t_3256.append_safe_html(line_704)
            t_3260 = t_3256.accumulated
            result_702 = t_3260
            i_703 = int_add_5817(i_703, 1)
        return_190 = result_702
    return return_190
def highlight_block(source_705: 'str13') -> 'SafeHtml':
    highlighted_707: 'SafeHtml' = highlight_source(source_705)
    t_3242: 'SafeHtmlBuilder' = SafeHtmlBuilder()
    t_3242.append_safe("<pre class='temper-code'><code>")
    t_3242.append_safe_html(highlighted_707)
    t_3242.append_safe('</code></pre>')
    return t_3242.accumulated

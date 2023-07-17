from os import PathLike
from pathlib import Path
from typing import List, Optional, Any

from tests4py.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


class Pandas(Project):
    def __init__(
        self,
        bug_id: int,
        buggy_commit_id: str,
        fixed_commit_id: str,
        test_file: List[Path],
        test_cases: List[str],
        test_status_fixed: TestStatus = TestStatus.PASSING,
        test_status_buggy: TestStatus = TestStatus.FAILING,
        unittests: Optional[UnittestGenerator] = None,
        systemtests: Optional[SystemtestGenerator] = None,
        api: Optional[API] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name="pandas",
            github_url="https://github.com/pandas-dev/pandas",
            status=Status.OK,
            cause="N.A.",
            python_version="3.8.3",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_file=test_file,
            test_cases=test_cases,
            darwin_python_version="3.8.4",
            python_fallback_version="3.8.4",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
        )  # TODO adjust parameters


def register():
    Pandas(
        bug_id=1,
        buggy_commit_id="3fd150c",
        fixed_commit_id="e41ee47a90bb1d8a1fa28fcefcd45ed8ef5cb946",
        test_file=[Path("pandas", "tests", "dtypes", "test_dtypes.py")],
        test_cases=[
            "pandas/tests/dtypes/test_dtypes.py::TestCategoricalDtype::test_not_string"
        ],
    )
    Pandas(
        bug_id=2,
        buggy_commit_id="2740fb4",
        fixed_commit_id="55e8891f6d33be14e0db73ac06513129503f995c",
        test_file=[Path("pandas", "tests", "indexing", "test_scalar.py")],
        test_cases=[
            "pandas/tests/indexing/test_scalar.py::test_at_with_tuple_index_get",
            "pandas/tests/indexing/test_scalar.py::test_at_with_tuple_index_set",
            "pandas/tests/indexing/test_scalar.py::test_multiindex_at_get",
            "pandas/tests/indexing/test_scalar.py::test_multiindex_at_set",
        ],
    )
    Pandas(
        bug_id=3,
        buggy_commit_id="45fee32",
        fixed_commit_id="d3a6a3a58e1a6eb68b8b8399ff252b8f4501950e",
        test_file=[
            Path("pandas", "tests", "series", "methods", "test_to_period.py"),
            Path("pandas", "tests", "series", "methods", "test_to_timestamp.py"),
        ],
        test_cases=[
            "pandas/tests/series/methods/test_to_period.py::TestToPeriod::test_to_period_raises",
            "pandas/tests/series/methods/test_to_timestamp.py::TestToTimestamp::test_to_timestamp_raises",
        ],
    )
    Pandas(
        bug_id=4,
        buggy_commit_id="cca710b",
        fixed_commit_id="2250ddfaff92abaff20a5bcd78315f5d4bd44981",
        test_file=[Path("pandas", "tests", "indexes", "multi", "test_join.py")],
        test_cases=[
            "pandas/tests/indexes/multi/test_join.py::test_join_multi_return_indexers"
        ],
    )
    Pandas(
        bug_id=5,
        buggy_commit_id="cca710b",
        fixed_commit_id="2250ddfaff92abaff20a5bcd78315f5d4bd44981",
        test_file=[Path("pandas", "tests", "groupby", "test_function.py")],
        test_cases=["pandas/tests/groupby/test_function.py::test_ops_not_as_index"],
    )
    Pandas(
        bug_id=6,
        buggy_commit_id="21a10d1",
        fixed_commit_id="8cd8ed3657e52ad9f67e17b7f5c20f7340ab6a2c",
        test_file=[Path("pandas", "tests", "groupby", "test_size.py")],
        test_cases=["pandas/tests/groupby/test_size.py::test_size_period_index"],
    )
    Pandas(
        bug_id=7,
        buggy_commit_id="27f365d",
        fixed_commit_id="64336ff8414f8977ff94adb9a5bc000a3a4ef454",
        test_file=[Path("pandas", "tests", "frame", "indexing", "test_indexing.py")],
        test_cases=[
            "pandas/tests/frame/indexing/test_indexing.py::TestDataFrameIndexing::test_reindex_nearest_tz"
        ],
    )
    Pandas(
        bug_id=8,
        buggy_commit_id="ddbeca6",
        fixed_commit_id="d09f20e29bdfa82f5efc071986e2633001d552f6",
        test_file=[Path("pandas", "tests", "frame", "methods", "test_replace.py")],
        test_cases=[
            "pandas/tests/frame/methods/test_replace.py::TestDataFrameReplace::test_replace_no_replacement_dtypes"
        ],
    )
    Pandas(
        bug_id=9,
        buggy_commit_id="c557ab5",
        fixed_commit_id="ebb727e5cd8865a7f5d6cfb4b22d3278b6bf5e6b",
        test_file=[
            Path("pandas", "tests", "indexes", "categorical", "test_indexing.py")
        ],
        test_cases=[
            "pandas/tests/indexes/categorical/test_indexing.py::TestContains::test_contains_na_dtype"
        ],
    )
    Pandas(
        bug_id=10,
        buggy_commit_id="de8ca78",
        fixed_commit_id="e1ee2b0679e5999c993a787606d30e75faaba7a2",
        test_file=[Path("pandas", "tests", "series", "methods", "test_update.py")],
        test_cases=[
            "pandas/tests/series/methods/test_update.py::TestUpdate::test_update_extension_array_series"
        ],
    )
    Pandas(
        bug_id=11,
        buggy_commit_id="1c88e6a",
        fixed_commit_id="b7f061c3d24df943e16918ad3932e767f5639a38",
        test_file=[Path("pandas", "tests", "reshape", "test_concat.py")],
        test_cases=["pandas/tests/reshape/test_concat.py::test_duplicate_keys"],
    )
    Pandas(
        bug_id=12,
        buggy_commit_id="9bd296c",
        fixed_commit_id="8aa707298428801199280b2b994632080591700a",
        test_file=[Path("pandas", "tests", "frame", "methods", "test_cov_corr.py")],
        test_cases=[
            "pandas/tests/frame/methods/test_cov_corr.py::TestDataFrameCov::test_cov_nullable_integer"
        ],
    )
    Pandas(
        bug_id=13,
        buggy_commit_id="08f9bd2",
        fixed_commit_id="91150d976ac41bd93a0e6516b2090c534f91aff2",
        test_file=[Path("pandas", "tests", "arrays", "categorical", "test_missing.py")],
        test_cases=[
            "pandas/tests/arrays/categorical/test_missing.py::TestCategoricalMissing::test_use_inf_as_na",
            "pandas/tests/arrays/categorical/test_missing.py::TestCategoricalMissing"
            "::test_use_inf_as_na_outside_context",
        ],
    )
    Pandas(
        bug_id=14,
        buggy_commit_id="e7b23d4",
        fixed_commit_id="dd71064327721c1ec7366000f357b0c08bcec4d2",
        test_file=[
            Path("pandas", "tests", "arithmetic", "test_datetime64.py"),
            Path("pandas", "tests", "arithmetic", "test_timedelta64.py"),
        ],
        test_cases=[
            "pandas/tests/arithmetic/test_datetime64.py::TestDatetime64DateOffsetArithmetic"
            "::test_dt64arr_add_sub_offset_array",
            "pandas/tests/arithmetic/test_timedelta64.py::TestTimedeltaArraylikeAddSubOps"
            "::test_td64arr_add_offset_index",
        ],
    )
    Pandas(
        bug_id=15,
        buggy_commit_id="f3fdab3",
        fixed_commit_id="71d610596ed128055614eb660f13c88168bfe22f",
        test_file=[Path("pandas", "tests", "indexes", "datetimes", "test_datetime.py")],
        test_cases=[
            "pandas/tests/indexes/datetimes/test_datetime.py::TestDatetimeIndex::test_pickle_after_set_freq"
        ],
    )
    Pandas(
        bug_id=16,
        buggy_commit_id="f159734",
        fixed_commit_id="74e8607cb163b76ccf272ac72ae6b7848fe930c8",
        test_file=[Path("pandas", "tests", "arithmetic", "test_period.py")],
        test_cases=[
            "pandas/tests/arithmetic/test_period.py::TestPeriodIndexSeriesMethods::test_pi_sub_period"
        ],
    )
    Pandas(
        bug_id=17,
        buggy_commit_id="1e5ff23",
        fixed_commit_id="afb04645b5b3361814f7d00ef68ce8d68e19ddb8",
        test_file=[Path("pandas", "tests", "indexes", "datetimes", "test_insert.py")],
        test_cases=[
            "pandas/tests/indexes/datetimes/test_insert.py::TestInsert::test_insert_mismatched_types_raises"
        ],
    )
    Pandas(
        bug_id=18,
        buggy_commit_id="e008a0a",
        fixed_commit_id="cb71376385c33270fa1922aec9eb6c49de4336f4",
        test_file=[Path("pandas", "tests", "window", "test_base_indexer.py")],
        test_cases=[
            "pandas/tests/window/test_base_indexer.py::test_rolling_forward_skewness"
        ],
    )
    Pandas(
        bug_id=19,
        buggy_commit_id="17dc6b0",
        fixed_commit_id="c6a1638bcd99df677a8f76f036c0b30027eb243c",
        test_file=[
            Path("pandas", "tests", "indexing", "multiindex", "test_loc.py"),
            Path("pandas", "tests", "indexing", "multiindex", "test_slice.py"),
            Path("pandas", "tests", "series", "indexing", "test_getitem.py"),
        ],
        test_cases=[
            "pandas/tests/indexing/multiindex/test_loc.py::TestMultiIndexLoc::test_loc_multiindex_list_missing_label",
            "pandas/tests/indexing/multiindex/test_slice.py::TestMultiIndexSlicers::test_per_axis_per_level_getitem",
            "pandas/tests/series/indexing/test_getitem.py::TestSeriesGetitemListLike"
            "::test_getitem_intlist_multiindex_numeric_level",
        ],
    )
    Pandas(
        bug_id=20,
        buggy_commit_id="ea09d50",
        fixed_commit_id="92afd5c2c08216e4e9c80eb6b92b1660f91846e0",
        test_file=[
            Path("pandas", "tests", "tseries", "offsets", "test_yqm_offsets.py")
        ],
        test_cases=[
            "pandas/tests/tseries/offsets/test_yqm_offsets.py::test_apply_index"
        ],
    )
    Pandas(
        bug_id=21,
        buggy_commit_id="4071c3b",
        fixed_commit_id="56d0934092b8296c90f940c56fce3b731e0de81b",
        test_file=[
            Path("pandas", "tests", "series", "indexing", "test_boolean.py"),
            Path("pandas", "tests", "series", "indexing", "test_getitem.py"),
        ],
        test_cases=[
            "pandas/tests/series/indexing/test_getitem.py::TestSeriesGetitemListLike::test_getitem_no_matches"
        ],
    )
    Pandas(
        bug_id=22,
        buggy_commit_id="38b669a",
        fixed_commit_id="299e27da8a75d02d84870c1ca5971f4dd0f046e6",
        test_file=[Path("pandas", "tests", "window", "test_base_indexer.py")],
        test_cases=[
            "pandas/tests/window/test_base_indexer.py::test_rolling_forward_window"
        ],
    )
    Pandas(
        bug_id=23,
        buggy_commit_id="ab9f3c9",
        fixed_commit_id="38b669a206b151e0a2bb985200d4a493c4ac078f",
        test_file=[Path("pandas", "tests", "indexes", "datetimes", "test_setops.py")],
        test_cases=[
            "pandas/tests/indexes/datetimes/test_setops.py::TestDatetimeIndexSetOps::test_intersection_empty",
            "pandas/tests/indexes/datetimes/test_setops.py::TestBusinessDatetimeIndex::test_intersection_bug",
            "pandas/tests/indexes/datetimes/test_setops.py::TestCustomDatetimeIndex::test_intersection_bug",
        ],
    )
    Pandas(
        bug_id=24,
        buggy_commit_id="91dcc3a",
        fixed_commit_id="6367bd23b935a85f1bcd2ae762c7f08433d0efbd",
        test_file=[
            Path("pandas", "tests", "indexes", "datetimes", "test_timezones.py")
        ],
        test_cases=[
            "pandas/tests/indexes/datetimes/test_timezones.py::test_tz_localize_invalidates_freq"
        ],
    )
    Pandas(
        bug_id=25,
        buggy_commit_id="ecc3b2e",
        fixed_commit_id="73d614403759831814ef7ab83ef1e4aaa645b33a",
        test_file=[Path("pandas", "tests", "indexes", "datetimes", "test_misc.py")],
        test_cases=[
            "pandas/tests/indexes/datetimes/test_misc.py"
            "::test_isocalendar_returns_correct_values_close_to_new_year_with_tz"
        ],
    )
    Pandas(
        bug_id=26,
        buggy_commit_id="13dc13f",
        fixed_commit_id="70ca24680d3e51fa4b957366e8093b3cc755462d",
        test_file=[
            Path("pandas", "tests", "arrays", "categorical", "test_analytics.py")
        ],
        test_cases=[
            "pandas/tests/arrays/categorical/test_analytics.py::TestCategoricalAnalytics::test_min_max_only_nan"
        ],
    )
    Pandas(
        bug_id=27,
        buggy_commit_id="6658d89",
        fixed_commit_id="13dc13f12c0fca943979cde065b7484bb0e40d66",
        test_file=[
            Path("pandas", "tests", "indexes", "datetimes", "test_to_period.py")
        ],
        test_cases=[
            "pandas/tests/indexes/datetimes/test_to_period.py::TestToPeriod::test_to_period_infer"
        ],
    )
    Pandas(
        bug_id=28,
        buggy_commit_id="40fd73a",
        fixed_commit_id="ef9b9387c88cf12b20dd8656dfedfc236e0f3352",
        test_file=[Path("pandas", "tests", "test_strings.py")],
        test_cases=["pandas/tests/test_strings.py::test_cat_different_classes"],
    )
    Pandas(
        bug_id=29,
        buggy_commit_id="6e3537d",
        fixed_commit_id="4334482c348c3adc69683c8332295e22092c1b57",
        test_file=[
            Path("pandas", "tests", "arrays", "interval", "test_interval.py"),
            Path("pandas", "tests", "series", "methods", "test_convert_dtypes.py"),
        ],
        test_cases=[
            "pandas/tests/arrays/interval/test_interval.py::TestSetitem::test_set_na",
            "pandas/tests/series/methods/test_convert_dtypes.py::TestSeriesConvertDtypes::test_convert_dtypes",
        ],
    )
    Pandas(
        bug_id=30,
        buggy_commit_id="60d6f28",
        fixed_commit_id="d857cd12b3ae11be788ba96015383a5b7464ecc9",
        test_file=[Path("pandas", "tests", "io", "json", "test_pandas.py")],
        test_cases=[
            "pandas/tests/io/json/test_pandas.py::TestPandasContainer::test_readjson_bool_series"
        ],
    )
    Pandas(
        bug_id=31,
        buggy_commit_id="45c13a9",
        fixed_commit_id="8267427bfe567eec9a098aa8c071dddcc1d289f9",
        test_file=[Path("pandas", "tests", "groupby", "test_function.py")],
        test_cases=[
            "pandas/tests/groupby/test_function.py::test_groupby_quantile_nullable_array"
        ],
    )
    Pandas(
        bug_id=32,
        buggy_commit_id="467e1c2",
        fixed_commit_id="c82cb179affed1c1136431ce39e4c66f4f3a65c0",
        test_file=[Path("pandas", "tests", "io", "sas", "test_xport.py")],
        test_cases=["pandas/tests/io/sas/test_xport.py::TestXport::test2_binary"],
    )
    Pandas(
        bug_id=33,
        buggy_commit_id="03dacc1",
        fixed_commit_id="89d8aba76a2bb930e520590d145e3d67b2046e39",
        test_file=[Path("pandas", "tests", "arrays", "integer", "test_function.py")],
        test_cases=[
            "pandas/tests/arrays/integer/test_function.py::test_value_counts_empty"
        ],
    )
    Pandas(
        bug_id=34,
        buggy_commit_id="02a134b",
        fixed_commit_id="cf9ec7854ecb80709804178e769425f02ddf8c64",
        test_file=[Path("pandas", "tests", "resample", "test_datetime_index.py")],
        test_cases=[
            "pandas/tests/resample/test_datetime_index.py::test_downsample_dst_at_midnight"
        ],
    )
    Pandas(
        bug_id=35,
        buggy_commit_id="a7dd3ea",
        fixed_commit_id="f10ec595eccaf86a9f52fe9683e1181a51ba675b",
        test_file=[
            Path("pandas", "tests", "indexes", "multi", "test_get_level_values.py")
        ],
        test_cases=[
            "pandas/tests/indexes/multi/test_get_level_values.py::test_get_level_values_when_periods"
        ],
    )
    Pandas(
        bug_id=36,
        buggy_commit_id="cb41651",
        fixed_commit_id="51f114b9882a5cf819efddb8be74524814f437e1",
        test_file=[Path("pandas", "tests", "dtypes", "", "test_missing.py")],
        test_cases=[
            "pandas/tests/dtypes//test_missing.py::TestIsNA::test_isna_old_datetimelike"
        ],
    )
    Pandas(
        bug_id=37,
        buggy_commit_id="c69f7d8",
        fixed_commit_id="845c50c9e2ce611c773422ae9db7097fc3e5fba5",
        test_file=[Path("pandas", "tests", "arrays", "string_", "test_string.py")],
        test_cases=["pandas/tests/arrays/string_/test_string.py::test_astype_int"],
    )
    Pandas(
        bug_id=38,
        buggy_commit_id="c81d90f",
        fixed_commit_id="e7ee418fa7a519225203fef23481c5fa35834dc3",
        test_file=[Path("pandas", "tests", "frame", "test_reshape.py")],
        test_cases=[
            "pandas/tests/frame/test_reshape.py::TestDataFrameReshape::test_unstack_long_index",
            "pandas/tests/frame/test_reshape.py::TestDataFrameReshape::test_unstack_multi_level_cols",
            "pandas/tests/frame/test_reshape.py::TestDataFrameReshape::test_unstack_multi_level_rows_and_cols",
        ],
    )
    Pandas(
        bug_id=39,
        buggy_commit_id="8a5f291",
        fixed_commit_id="a3097b5bd172e76dd3524eb5dbe18b6b4c22df50",
        test_file=[Path("pandas", "tests", "frame", "", "test_axis_select_reindex.py")],
        test_cases=[
            "pandas/tests/frame//test_axis_select_reindex.py::TestDataFrameSelectReindex"
            "::test_inplace_drop_and_operation"
        ],
    )
    Pandas(
        bug_id=40,
        buggy_commit_id="218cc30",
        fixed_commit_id="8a5f2917e163e09e08af880819fdf44144b1a5fe",
        test_file=[Path("pandas", "tests", "reshape", "merge", "test_merge.py")],
        test_cases=[
            "pandas/tests/reshape/merge/test_merge.py::TestMerge::test_merge_preserves_row_order"
        ],
    )
    Pandas(
        bug_id=41,
        buggy_commit_id="1b49f69",
        fixed_commit_id="d4273353bc512e3b4e79c361b879633f33ec7289",
        test_file=[
            Path("pandas", "tests", "indexing", "test_iloc.py"),
            Path("pandas", "tests", "internals", "test_internals.py"),
        ],
        test_cases=[
            "pandas/tests/indexing/test_iloc.py::TestiLoc2::test_iloc_setitem_categorical_updates_inplace",
            "pandas/tests/internals/test_internals.py::TestShouldStore::test_should_store_categorical",
        ],
    )
    Pandas(
        bug_id=42,
        buggy_commit_id="b3a0fe4",
        fixed_commit_id="05780a760400e42ce1b00200dd8204ae4f94044a",
        test_file=[
            Path("pandas", "tests", "util", "test_assert_frame_equal.py"),
            Path("pandas", "tests", "util", "test_assert_series_equal.py"),
        ],
        test_cases=[
            "pandas/tests/util/test_assert_frame_equal.py::test_assert_frame_equal_extension_dtype_mismatch",
            "pandas/tests/util/test_assert_frame_equal.py::test_assert_frame_equal_interval_dtype_mismatch",
            "pandas/tests/util/test_assert_series_equal.py::test_assert_series_equal_extension_dtype_mismatch",
            "pandas/tests/util/test_assert_series_equal.py::test_assert_series_equal_interval_dtype_mismatch",
            "",
        ],
    )
    Pandas(
        bug_id=43,
        buggy_commit_id="81149fb",
        fixed_commit_id="be7bfe6ab7ae2cba056f61dea6c3b0226bf80082",
        test_file=[Path("pandas", "tests", "frame", "test_arithmetic.py")],
        test_cases=["pandas/tests/frame/test_arithmetic.py::test_pow_with_realignment"],
    )
    Pandas(
        bug_id=44,
        buggy_commit_id="96d22d4",
        fixed_commit_id="50817487ce5b1a2c4896495509e2b53e22fa3212",
        test_file=[
            Path("pandas", "tests", "indexes", "test_base.py"),
            Path("pandas", "tests", "indexing", "test_loc.py"),
        ],
        test_cases=[
            "pandas/tests/indexes/test_base.py::test_get_indexer_non_unique_wrong_dtype",
            "pandas/tests/indexing/test_loc.py::test_loc_datetimelike_mismatched_dtypes",
        ],
    )
    Pandas(
        bug_id=45,
        buggy_commit_id="74c5306",
        fixed_commit_id="74f6579941fbe71cf7c033f53977047ac872e469",
        test_file=[Path("pandas", "tests", "frame", "test_constructors.py")],
        test_cases=[
            "pandas/tests/frame/test_constructors.py::TestDataFrameConstructorWithDatetimeTZ"
            "::test_construction_from_set_raises"
        ],
    )
    Pandas(
        bug_id=46,
        buggy_commit_id="e734449",
        fixed_commit_id="0ed6d538c38010bcbd540cd6413ae8e4b749d9e6",
        test_file=[Path("pandas", "tests", "reshape", "test_pivot.py")],
        test_cases=[
            "pandas/tests/reshape/test_pivot.py::TestPivotTable::test_pivot_table_retains_tz"
        ],
    )
    Pandas(
        bug_id=47,
        buggy_commit_id="1a5b11d",
        fixed_commit_id="810a4e5b19616efb503767b4518083c9a59c11e6",
        test_file=[
            Path("pandas", "tests", "frame", "indexing", "test_indexing.py"),
            Path("pandas", "tests", "indexing", "test_loc.py"),
        ],
        test_cases=[
            "pandas/tests/frame/indexing/test_indexing.py::TestDataFrameIndexing::test_setitem_list_missing_columns",
            "pandas/tests/indexing/test_loc.py::TestLoc2::test_loc_setitem_missing_columns",
        ],
    )
    Pandas(
        bug_id=48,
        buggy_commit_id="9bc3ee0",
        fixed_commit_id="9e7cb7c102655d0ba92d2561c178da9254d5cef5",
        test_file=[Path("pandas", "tests", "groupby", "test_function.py")],
        test_cases=[
            "pandas/tests/groupby/test_function.py::test_apply_to_nullable_integer_returns_float"
        ],
    )
    Pandas(
        bug_id=49,
        buggy_commit_id="113c255",
        fixed_commit_id="37659d47a685ecc5f5117aa56526ece0106c6d0f",
        test_file=[Path("pandas", "tests", "test_strings.py")],
        test_cases=[
            "pandas/tests/test_strings.py::TestStringMethods::test_repeat_with_null"
        ],
    )
    Pandas(
        bug_id=50,
        buggy_commit_id="ebf9668",
        fixed_commit_id="821aa25c9039e72da9a7b236cf2f9e7d549cbb7b",
        test_file=[Path("pandas", "tests", "extension", "test_categorical.py")],
        test_cases=[
            "pandas/tests/extension/test_categorical.py::TestComparisonOps::test_not_equal_with_na"
        ],
    )
    Pandas(
        bug_id=51,
        buggy_commit_id="4800ab4",
        fixed_commit_id="ea1d8fadb95fbc7cafe036274006228400817fd4",
        test_file=[Path("pandas", "tests", "reshape", "merge", "test_merge.py")],
        test_cases=[
            "pandas/tests/reshape/merge/test_merge.py::test_categorical_non_unique_monotonic",
            "",
        ],
    )
    Pandas(
        bug_id=52,
        buggy_commit_id="20a84a5",
        fixed_commit_id="7017599821e02ba95282848c12f7d3b5f2ce670a",
        test_file=[Path("pandas", "tests", "groupby", "test_function.py")],
        test_cases=[
            "pandas/tests/groupby/test_function.py::test_series_groupby_nunique"
        ],
    )
    Pandas(
        bug_id=53,
        buggy_commit_id="f9b49c8",
        fixed_commit_id="020dcce17e3bd0983fca5b02556bd431140ab371",
        test_file=[
            Path("pandas", "tests", "indexing", "test_categorical.py"),
            Path("pandas", "tests", "indexing", "test_loc.py"),
        ],
        test_cases=[
            "pandas/tests/indexing/test_categorical.py::TestCategoricalIndex::test_loc_scalar",
            "pandas/tests/indexing/test_loc.py::TestLoc::test_loc_getitem_int",
            "pandas/tests/indexing/test_loc.py::test_loc_mixed_int_float",
        ],
    )
    Pandas(
        bug_id=54,
        buggy_commit_id="25443f0",
        fixed_commit_id="00e8e4ab0c5e4c7bfb3e356e660d9f088d4a82a4",
        test_file=[Path("pandas", "tests", "dtypes", "test_dtypes.py")],
        test_cases=[
            "pandas/tests/dtypes/test_dtypes.py::TestCategoricalDtype::test_from_values_or_dtype_invalid_dtype"
        ],
    )
    Pandas(
        bug_id=55,
        buggy_commit_id="6ab00bc",
        fixed_commit_id="628dfba239865adc09c94108b288bcb60c619950",
        test_file=[Path("pandas", "tests", "indexing", "test_iloc.py")],
        test_cases=[
            "pandas/tests/indexing/test_iloc.py::TestiLoc2::test_is_scalar_access"
        ],
    )
    Pandas(
        bug_id=56,
        buggy_commit_id="9e69040",
        fixed_commit_id="dafec63f2e138d0451dae5b37edea2e83f9adc8a",
        test_file=[Path("pandas", "tests", "indexing", "test_scalar.py")],
        test_cases=[
            "pandas/tests/indexing/test_scalar.py::test_iat_dont_wrap_object_datetimelike"
        ],
    )
    Pandas(
        bug_id=57,
        buggy_commit_id="267d2d8",
        fixed_commit_id="84444538a88721c5ee74de8836b716d3c1adc4b8",
        test_file=[Path("pandas", "tests", "arrays", "categorical", "test_replace.py")],
        test_cases=["pandas/tests/arrays/categorical/test_replace.py::test_replace"],
    )
    Pandas(
        bug_id=58,
        buggy_commit_id="634a41f",
        fixed_commit_id="16684f2affaf901b42a12e50f9c29e7c034ad7ea",
        test_file=[
            Path("pandas", "tests", "arrays", "categorical", "test_constructors.py")
        ],
        test_cases=[
            "pandas/tests/arrays/categorical/test_constructors.py::TestCategoricalConstructors"
            "::test_from_codes_with_nullable_int",
            "pandas/tests/arrays/categorical/test_constructors.py::TestCategoricalConstructors"
            "::test_from_codes_with_nullable_int_na_raises",
        ],
    )
    Pandas(
        bug_id=59,
        buggy_commit_id="292a993",
        fixed_commit_id="8dd9fabd2ad9104e747084437b9ad436d5be087a",
        test_file=[Path("pandas", "tests", "window", "test_pairwise.py")],
        test_cases=[
            "pandas/tests/window/test_pairwise.py::TestPairwise::test_corr_freq_memory_error"
        ],
    )
    Pandas(
        bug_id=60,
        buggy_commit_id="6bc2dca",
        fixed_commit_id="fcf7258c19b0a6a712f33fb0bcefdae426be7e7f",
        test_file=[Path("pandas", "tests", "window", "test_grouper.py")],
        test_cases=[
            "pandas/tests/window/test_grouper.py::TestGrouperGrouping::test_groupby_rolling"
        ],
    )
    Pandas(
        bug_id=61,
        buggy_commit_id="74dad82",
        fixed_commit_id="f7e2b74f1bcc1d1cbebbc42481e33f0abb2843dc",
        test_file=[Path("pandas", "tests", "indexing", "test_indexing.py")],
        test_cases=[
            "pandas/tests/indexing/test_indexing.py::TestFancy::test_getitem_ndarray_3d"
        ],
    )
    Pandas(
        bug_id=62,
        buggy_commit_id="46a77f6",
        fixed_commit_id="74dad82827e9b13552df2d6d3fbbeb901821b53f",
        test_file=[Path("pandas", "tests", "indexing", "test_indexing.py")],
        test_cases=[
            "pandas/tests/indexing/test_indexing.py::TestFancy::test_setitem_ndarray_3d"
        ],
    )
    Pandas(
        bug_id=63,
        buggy_commit_id="e5c65bf",
        fixed_commit_id="e1ca66bae38b8026079dfcbe0edad5f278546608",
        test_file=[Path("pandas", "tests", "indexing", "test_scalar.py")],
        test_cases=[
            "pandas/tests/indexing/test_scalar.py::TestScalar2::test_series_at_raises_type_error"
        ],
    )
    Pandas(
        bug_id=64,
        buggy_commit_id="31c1856",
        fixed_commit_id="d0c84ce57d23a409169daf7232ec7681e42363fe",
        test_file=[Path("pandas", "tests", "io", "excel", "test_writers.py")],
        test_cases=[
            "pandas/tests/io/excel/test_writers.py::TestExcelWriter::test_write_subset_columns"
        ],
    )
    Pandas(
        bug_id=65,
        buggy_commit_id="2f70e41",
        fixed_commit_id="2f9a44635bd8d468cf008f2855ce2dcfb9e90586",
        test_file=[Path("pandas", "tests", "io", "parser", "test_encoding.py")],
        test_cases=[
            "pandas/tests/io/parser/test_encoding.py::test_binary_mode_file_buffers"
        ],
    )
    Pandas(
        bug_id=66,
        buggy_commit_id="f5409cb",
        fixed_commit_id="d84f9eb32aea33a8f790e8e365cf226eddd5c7a7",
        test_file=[Path("pandas", "tests", "series", "indexing", "test_xs.py")],
        test_cases=[
            "pandas/tests/series/indexing/test_xs.py::test_xs_datetimelike_wrapping"
        ],
    )
    Pandas(
        bug_id=67,
        buggy_commit_id="c3e32d7",
        fixed_commit_id="1996b17599731b889895b0e1edf758588c068fbb",
        test_file=[Path("pandas", "tests", "frame", "indexing", "test_indexing.py")],
        test_cases=[
            "pandas/tests/frame/indexing/test_indexing.py::test_object_casting_indexing_wraps_datetimelike"
        ],
    )
    Pandas(
        bug_id=68,
        buggy_commit_id="01582c4",
        fixed_commit_id="d28db65bdba16e9400a16469ba2707f94ae63483",
        test_file=[Path("pandas", "tests", "arrays", "interval", "test_interval.py")],
        test_cases=[
            "pandas/tests/arrays/interval/test_interval.py::TestMethods::test_shift"
        ],
    )
    Pandas(
        bug_id=69,
        buggy_commit_id="426d445",
        fixed_commit_id="948f95756c79543bb089a94a85e73011a3730b2d",
        test_file=[Path("pandas", "tests", "indexes", "test_numeric.py")],
        test_cases=[
            "pandas/tests/indexes/test_numeric.py::TestFloat64Index::test_lookups_datetimelike_values"
        ],
    )
    Pandas(
        bug_id=70,
        buggy_commit_id="a05e6c9",
        fixed_commit_id="06ef193a5c1957c0a76e3e88bc7b834b38972c39",
        test_file=[Path("pandas", "tests", "groupby", "test_categorical.py")],
        test_cases=[
            "pandas/tests/groupby/test_categorical.py::test_groupby_agg_categorical_columns"
        ],
    )
    Pandas(
        bug_id=71,
        buggy_commit_id="74a5edc",
        fixed_commit_id="a5daff22e6e37af4946c614f85b110905e063be3",
        test_file=[Path("pandas", "tests", "arrays", "test_integer.py")],
        test_cases=["pandas/tests/arrays/test_integer.py::test_cut"],
    )
    Pandas(
        bug_id=72,
        buggy_commit_id="a9b61a9",
        fixed_commit_id="0c50950f2a7e32887eff6be5979f09772091e1de",
        test_file=[Path("pandas", "tests", "frame", "indexing", "test_categorical.py")],
        test_cases=[
            "pandas/tests/frame/indexing/test_categorical.py::TestDataFrameIndexingCategorical"
            "::test_setitem_single_row_categorical"
        ],
    )
    Pandas(
        bug_id=73,
        buggy_commit_id="f1d7ac6",
        fixed_commit_id="6f93898d32c0f1fdb382d1e9dee434c158998374",
        test_file=[Path("pandas", "tests", "frame", "test_arithmetic.py")],
        test_cases=[
            "pandas/tests/frame/test_arithmetic.py::TestFrameFlexArithmetic::test_floordiv_axis0"
        ],
    )
    Pandas(
        bug_id=74,
        buggy_commit_id="9a211aa",
        fixed_commit_id="839e7f1416148caff518a5b75327a2480a2bbbb4",
        test_file=[
            Path("pandas", "tests", "indexes", "timedeltas", "test_constructors.py")
        ],
        test_cases=[
            "pandas/tests/indexes/timedeltas/test_constructors.py::TestTimedeltaIndex::test_infer_from_tdi_mismatch"
        ],
    )
    Pandas(
        bug_id=75,
        buggy_commit_id="2038d7a",
        fixed_commit_id="9a211aae9f710db23c9113aea0251e2758904755",
        test_file=[Path("pandas", "tests", "indexes", "period", "test_indexing.py")],
        test_cases=[
            "pandas/tests/indexes/period/test_indexing.py::TestIndexing::test_contains"
        ],
    )
    Pandas(
        bug_id=76,
        buggy_commit_id="4da554f",
        fixed_commit_id="47922d3b00edfc264f73b1484589734bbd077c11",
        test_file=[Path("pandas", "tests", "io", "json", "test_pandas.py")],
        test_cases=[
            "pandas/tests/io/json/test_pandas.py::TestPandasContainer::test_frame_int_overflow"
        ],
    )
    Pandas(
        bug_id=77,
        buggy_commit_id="667bb37",
        fixed_commit_id="daef69c1366e31c3c49aea6f2e55f577d0c832fd",
        test_file=[Path("pandas", "tests", "arithmetic", "test_array_ops.py")],
        test_cases=["pandas/tests/arithmetic/test_array_ops.py::test_na_logical_op_2d"],
    )
    Pandas(
        bug_id=78,
        buggy_commit_id="f5aa542",
        fixed_commit_id="bd6b395a1e8fb7d099fa17a0e24f8fe3b628822c",
        test_file=[Path("pandas", "tests", "frame", "test_subclass.py")],
        test_cases=[
            "pandas/tests/frame/test_subclass.py::TestDataFrameSubclassing::test_subclassed_boolean_reductions"
        ],
    )
    Pandas(
        bug_id=79,
        buggy_commit_id="38ea154",
        fixed_commit_id="0b0cd08524e4472eb15835c2b91621dc0a6eeeb0",
        test_file=[Path("pandas", "tests", "indexes", "datetimes", "test_indexing.py")],
        test_cases=[
            "pandas/tests/indexes/datetimes/test_indexing.py::TestDatetimeIndex::test_get_loc"
        ],
    )
    Pandas(
        bug_id=80,
        buggy_commit_id="d0d93db",
        fixed_commit_id="351760c0655b6c383e449cf857b9a718e3545229",
        test_file=[Path("pandas", "tests", "arrays", "sparse", "test_arithmetics.py")],
        test_cases=["pandas/tests/arrays/sparse/test_arithmetics.py::test_invert"],
    )
    Pandas(
        bug_id=81,
        buggy_commit_id="b529857",
        fixed_commit_id="339edcdb7ecc6edc6fde1b7d1413dbb746d2bcca",
        test_file=[Path("pandas", "tests", "arrays", "test_integer.py")],
        test_cases=[
            "pandas/tests/arrays/test_integer.py::TestCasting::test_astype_boolean"
        ],
    )
    Pandas(
        bug_id=82,
        buggy_commit_id="6f395ad",
        fixed_commit_id="e83a6bddac8c89b144dfe0783594dd332c5b3030",
        test_file=[Path("pandas", "tests", "reshape", "merge", "test_merge.py")],
        test_cases=[
            "pandas/tests/reshape/merge/test_merge.py::test_merge_datetime_upcast_dtype"
        ],
    )
    Pandas(
        bug_id=83,
        buggy_commit_id="964400d",
        fixed_commit_id="7ffcf9d6753e7de2c5318e8e0ecdc63586d502f3",
        test_file=[Path("pandas", "tests", "reshape", "test_concat.py")],
        test_cases=["pandas/tests/reshape/test_concat.py::test_concat_copy_index"],
    )
    Pandas(
        bug_id=84,
        buggy_commit_id="469b4b7",
        fixed_commit_id="24d7c06130f9c2aeebedc26971b244ce076f7d0a",
        test_file=[Path("pandas", "tests", "frame", "test_reshape.py")],
        test_cases=[
            "pandas/tests/frame/test_reshape.py::TestDataFrameReshape::test_unstack_tuplename_in_multiindex",
            "pandas/tests/frame/test_reshape.py::TestDataFrameReshape::test_unstack_mixed_type_name_in_multiindex",
        ],
    )
    Pandas(
        bug_id=85,
        buggy_commit_id="f1aaf62",
        fixed_commit_id="29edd119d31a9ee7d4f89e8c1dc8af96f0c19dce",
        test_file=[Path("pandas", "tests", "groupby", "test_apply.py")],
        test_cases=["pandas/tests/groupby/test_apply.py::test_apply_multi_level_name"],
    )
    Pandas(
        bug_id=86,
        buggy_commit_id="55cfabb",
        fixed_commit_id="f792d8c50ee456aa8aa2ae406d8e6b8843f45614",
        test_file=[Path("pandas", "tests", "reshape", "test_pivot.py")],
        test_cases=[
            "pandas/tests/reshape/test_pivot.py::TestPivotTable::test_pivot_columns_none_raise_error"
        ],
    )
    Pandas(
        bug_id=87,
        buggy_commit_id="641346c",
        fixed_commit_id="a890239b7020dec714d9819b718d83f786bfda34",
        test_file=[Path("pandas", "tests", "reshape", "test_pivot.py")],
        test_cases=[
            "pandas/tests/reshape/test_pivot.py::TestCrosstab::test_crosstab_both_tuple_names"
        ],
    )
    Pandas(
        bug_id=88,
        buggy_commit_id="698920f",
        fixed_commit_id="586bcb16023ae870b0ad7769f6d9077903705486",
        test_file=[Path("pandas", "tests", "reshape", "test_pivot.py")],
        test_cases=[
            "pandas/tests/reshape/test_pivot.py::TestPivotTable::test_pivot_table_multiindex_only"
        ],
    )
    Pandas(
        bug_id=89,
        buggy_commit_id="0dc317f",
        fixed_commit_id="feaa5033b7810f7775fd4806c27b2f9f1e9b5051",
        test_file=[Path("pandas", "tests", "frame", "test_reshape.py")],
        test_cases=[
            "pandas/tests/frame/test_reshape.py::test_unstacking_multi_index_df"
        ],
    )
    Pandas(
        bug_id=90,
        buggy_commit_id="a474a01",
        fixed_commit_id="1c3d64bae7c07b5ae1be337e0ebd751385b7ce27",
        test_file=[Path("pandas", "tests", "io", "test_pickle.py")],
        test_cases=[
            "pandas/tests/io/test_pickle.py::test_pickle_buffer_roundtrip",
            "pandas/tests/io/test_pickle.py::test_pickle_generalurl_read",
        ],
    )
    Pandas(
        bug_id=91,
        buggy_commit_id="5c12d4f",
        fixed_commit_id="cb9a1c7d0319c34a97247973ca96af53ead8033a",
        test_file=[Path("pandas", "tests", "arrays", "test_timedeltas.py")],
        test_cases=[
            "pandas/tests/arrays/test_timedeltas.py::TestTimedeltaArray::test_searchsorted_invalid_types"
        ],
    )
    Pandas(
        bug_id=92,
        buggy_commit_id="f2b213c",
        fixed_commit_id="511a2847f4330c54d079d04b3cac4febe0fe9915",
        test_file=[Path("pandas", "tests", "frame", "methods", "test_asof.py")],
        test_cases=[
            "pandas/tests/frame/methods/test_asof.py::TestFrameAsof::test_missing"
        ],
    )
    Pandas(
        bug_id=93,
        buggy_commit_id="425c2fb",
        fixed_commit_id="bde25278ccf4fb2d751c5e99e24b2270e0d62ef7",
        test_file=[
            Path("pandas", "tests", "indexes", "period", "test_indexing.py"),
            Path(""),
        ],
        test_cases=[
            "pandas/tests/indexes/period/test_indexing.py::TestWhere::test_where_invalid_dtypes"
        ],
    )
    Pandas(
        bug_id=94,
        buggy_commit_id="8803056",
        fixed_commit_id="613df15047887957f5964d2a6ce59ea20b0c4c91",
        test_file=[
            Path("pandas", "tests", "indexes", "datetimes", "test_constructors.py")
        ],
        test_cases=[
            "pandas/tests/indexes/datetimes/test_constructors.py::TestDatetimeIndex"
            "::test_shallow_copy_inherits_array_freq"
        ],
    )
    Pandas(
        bug_id=95,
        buggy_commit_id="036dc88",
        fixed_commit_id="c99dfea33612f44e97c2365f78c0ca6d5754a1bc",
        test_file=[Path("pandas", "tests", "arithmetic", "test_period.py")],
        test_cases=[
            "pandas/tests/arithmetic/test_period.py::TestPeriodIndexComparisons::test_eq_integer_disallowed"
        ],
    )
    Pandas(
        bug_id=96,
        buggy_commit_id="5e488a0",
        fixed_commit_id="6d67cf9f02dd22cc870fd407f569197512700203",
        test_file=[
            Path("pandas", "tests", "indexes", "datetimes", "test_date_range.py")
        ],
        test_cases=[
            "pandas/tests/indexes/datetimes/test_date_range.py::test_date_range_with_custom_holidays"
        ],
    )
    Pandas(
        bug_id=97,
        buggy_commit_id="f9e524c",
        fixed_commit_id="6f690b088190581552e04c53288819472fdb2dbe",
        test_file=[Path("pandas", "tests", "indexes", "timedeltas", "test_setops.py")],
        test_cases=[
            "pandas/tests/indexes/timedeltas/test_setops.py::TestTimedeltaIndex::test_union_sort_false"
        ],
    )
    Pandas(
        bug_id=98,
        buggy_commit_id="8105a7e",
        fixed_commit_id="09e4b780f09c5aa72bb2a6ae2832612f81dc047f",
        test_file=[
            Path("pandas", "tests", "indexes", "period", "test_constructors.py")
        ],
        test_cases=[
            "pandas/tests/indexes/period/test_constructors.py::TestPeriodIndex::test_base_constructor_with_period_dtype"
        ],
    )
    Pandas(
        bug_id=99,
        buggy_commit_id="2b1b3da",
        fixed_commit_id="b8043724c48890e86fda0265ad5b6ac3d31f1940",
        test_file=[Path("pandas", "tests", "indexes", "datetimes", "test_tools.py")],
        test_cases=[
            "pandas/tests/indexes/datetimes/test_tools.py::test_nullable_integer_to_datetime"
        ],
    )
    Pandas(
        bug_id=100,
        buggy_commit_id="8806ed7",
        fixed_commit_id="2b1b3da4c68fdaf9637d12706c5ba3de1a9b20de",
        test_file=[Path("pandas", "tests", "frame", "methods", "test_pct_change.py")],
        test_cases=[
            "pandas/tests/frame/methods/test_pct_change.py::test_pct_change_with_duplicated_indices"
        ],
    )
    Pandas(
        bug_id=101,
        buggy_commit_id="765d8db",
        fixed_commit_id="27b713ba677869893552cbeff6bc98a5dd231950",
        test_file=[Path("pandas", "tests", "dtypes", "test_common.py")],
        test_cases=["pandas/tests/dtypes/test_common.py::test_astype_nansafe"],
    )
    Pandas(
        bug_id=102,
        buggy_commit_id="efaadd5",
        fixed_commit_id="765d8db7eef1befef33f4c99d3e206d26e8444c8",
        test_file=[Path("pandas", "tests", "frame", "test_constructors.py")],
        test_cases=[
            "pandas/tests/frame/test_constructors.py::TestDataFrameConstructorWithDatetimeTZ"
            "::test_from_2d_ndarray_with_dtype"
        ],
    )
    Pandas(
        bug_id=103,
        buggy_commit_id="d1f82f7",
        fixed_commit_id="19578e364fb47ce10dd14174cffc3ecfea1a58cd",
        test_file=[Path("pandas", "tests", "groupby", "test_transform.py")],
        test_cases=["pandas/tests/groupby/test_transform.py::test_pct_change"],
    )
    Pandas(
        bug_id=104,
        buggy_commit_id="f738581",
        fixed_commit_id="8e9b3eee812b70197341c26c40200d8a1a77ed9c",
        test_file=[Path("pandas", "tests", "groupby", "test_function.py")],
        test_cases=[
            "pandas/tests/groupby/test_function.py::test_groupby_quantile_with_arraylike_q_and_int_columns"
        ],
    )
    Pandas(
        bug_id=105,
        buggy_commit_id="7e6125a",
        fixed_commit_id="cb5f9d1ff407f5ccef7c717e0c23bbd6ed96cf5f",
        test_file=[Path("pandas", "tests", "arithmetic", "test_period.py")],
        test_cases=[
            "pandas/tests/arithmetic/test_period.py::TestPeriodIndexArithmetic::test_pi_add_offset_n_gt1",
            "pandas/tests/arithmetic/test_period.py::TestPeriodIndexArithmetic::test_parr_add_sub_td64_nat",
            "pandas/tests/arithmetic/test_period.py::TestPeriodIndexArithmetic::test_parr_add_sub_tdt64_nat_array",
        ],
    )
    Pandas(
        bug_id=106,
        buggy_commit_id="114d552",
        fixed_commit_id="e46026ff4669a30192b91e362ce8cdcbc9693870",
        test_file=[Path("pandas", "tests", "indexes", "multi", "test_drop.py")],
        test_cases=[
            "pandas/tests/indexes/multi/test_drop.py::test_drop_with_non_unique_datetime_index_and_invalid_keys"
        ],
    )
    Pandas(
        bug_id=107,
        buggy_commit_id="47ac4b3",
        fixed_commit_id="fa4949f27ccfbc255bb8dbcd5ec5464b8663f1d2",
        test_file=[Path("pandas", "tests", "frame", "test_combine_concat.py")],
        test_cases=[
            "pandas/tests/frame/test_combine_concat.py::TestDataFrameConcatCommon"
            "::test_append_timestamps_aware_or_naive"
        ],
    )
    Pandas(
        bug_id=108,
        buggy_commit_id="20e4c18",
        fixed_commit_id="53a0dfd41a65a33dd7b0963734b24c749212e625",
        test_file=[Path("pandas", "tests", "dtypes", "cast", "test_infer_dtype.py")],
        test_cases=[
            "pandas/tests/dtypes/cast/test_infer_dtype.py::test_infer_from_interval"
        ],
    )
    Pandas(
        bug_id=109,
        buggy_commit_id="8b39de1",
        fixed_commit_id="68b3eb4f5a7fbc223accbbeddbf03ec8ea31af00",
        test_file=[
            Path("pandas", "tests", "arrays", "categorical", "test_analytics.py")
        ],
        test_cases=[
            "pandas/tests/arrays/categorical/test_analytics.py::TestCategoricalAnalytics::test_min_max_ordered_empty"
        ],
    )
    Pandas(
        bug_id=110,
        buggy_commit_id="cceef8e",
        fixed_commit_id="96bb151fe1a5b812ecab400adcd297d14fd0e0e4",
        test_file=[Path("pandas", "tests", "indexing", "test_categorical.py")],
        test_cases=[
            "pandas/tests/indexing/test_categorical.py::TestCategoricalIndex::test_loc_with_non_string_categories",
            "pandas/tests/indexing/test_categorical.py::TestCategoricalIndex::test_loc_slice",
        ],
    )
    Pandas(
        bug_id=111,
        buggy_commit_id="28715a7",
        fixed_commit_id="27836e93dc3c9d55c60282ccb15c88c42a340d87",
        test_file=[
            Path("pandas", "tests", "indexing", "test_categorical.py"),
            Path("pandas", "tests", "indexing", "test_floats.py"),
        ],
        test_cases=[
            "pandas/tests/indexing/test_categorical.py::TestCategoricalIndex::test_loc_with_non_string_categories",
            "pandas/tests/indexing/test_floats.py::TestFloatIndexers::test_scalar_non_numeric",
        ],
    )
    Pandas(
        bug_id=112,
        buggy_commit_id="ebbe2a2",
        fixed_commit_id="8a354b7630f74739212725c38cbaa9b069191a88",
        test_file=[Path("pandas", "tests", "frame", "test_analytics.py")],
        test_cases=[
            "pandas/tests/frame/test_analytics.py::TestDataFrameAnalytics::test_round_interval_category_columns"
        ],
    )
    Pandas(
        bug_id=113,
        buggy_commit_id="b164624",
        fixed_commit_id="8705aad961dd227d38ff93a39697547b98109c9d",
        test_file=[Path("pandas", "tests", "extension", "test_integer.py")],
        test_cases=[
            "pandas/tests/extension/test_integer.py::TestComparisonOps::test_compare_to_string",
            "pandas/tests/extension/test_integer.py::TestComparisonOps::test_compare_to_int",
        ],
    )
    Pandas(
        bug_id=114,
        buggy_commit_id="8f0310a",
        fixed_commit_id="9a222ea0300053ff46da984e3b3f68622ccba9c3",
        test_file=[Path("pandas", "tests", "extension", "decimal", "test_decimal.py")],
        test_cases=[
            "pandas/tests/extension/decimal/test_decimal.py::test_indexing_no_materialize"
        ],
    )
    Pandas(
        bug_id=115,
        buggy_commit_id="ed20822",
        fixed_commit_id="386494d0dc851be9e86b1576f30fa8705df4d47b",
        test_file=[Path("pandas", "tests", "series", "test_missing.py")],
        test_cases=[
            "pandas/tests/series/test_missing.py::TestSeriesInterpolateData::test_interpolate_unsorted_index"
        ],
    )
    Pandas(
        bug_id=116,
        buggy_commit_id="9333e3d",
        fixed_commit_id="c4fa6a52f7737aecda08f6b0f2d6c27476298ae1",
        test_file=[Path("pandas", "tests", "reshape", "merge", "test_merge_asof.py")],
        test_cases=[
            "pandas/tests/reshape/merge/test_merge_asof.py::TestAsOfMerge::test_merge_index_column_tz"
        ],
    )
    Pandas(
        bug_id=117,
        buggy_commit_id="fc100fe",
        fixed_commit_id="f98d2b6587b74c9a640b062d94911b199d962119",
        test_file=[Path("pandas", "tests", "series", "test_analytics.py")],
        test_cases=[
            "pandas/tests/series/test_analytics.py::TestSeriesAnalytics::test_count"
        ],
    )
    Pandas(
        bug_id=118,
        buggy_commit_id="6f1accd",
        fixed_commit_id="76e39ebcf584042fab4f224a6bd2c903bb0c8aff",
        test_file=[Path("pandas", "tests", "reshape", "test_melt.py")],
        test_cases=[
            "pandas/tests/reshape/test_melt.py::TestMelt::test_melt_mixed_int_str_id_vars",
            "pandas/tests/reshape/test_melt.py::TestMelt::test_melt_mixed_int_str_value_vars",
        ],
    )
    Pandas(
        bug_id=119,
        buggy_commit_id="3f69d62",
        fixed_commit_id="e0bd4d5dd07cc481cb52de3cf3c7bf199cb2df07",
        test_file=[Path("pandas", "tests", "reshape", "test_pivot.py")],
        test_cases=[
            "pandas/tests/reshape/test_pivot.py::TestPivotTable::test_margins_casted_to_float"
        ],
    )
    Pandas(
        bug_id=120,
        buggy_commit_id="2b0cac7",
        fixed_commit_id="c5a1f9e2c373ced9ef2f02ab64d11eaa7b4248f2",
        test_file=[Path("pandas", "tests", "groupby", "test_categorical.py")],
        test_cases=[
            "pandas/tests/groupby/test_categorical.py::test_series_groupby_on_2_categoricals_unobserved",
            "pandas/tests/groupby/test_categorical.py::test_series_groupby_on_2_categoricals_unobserved_zeroes_or_nans",
        ],
    )
    Pandas(
        bug_id=121,
        buggy_commit_id="ad4c4d5",
        fixed_commit_id="958756af5cb40658e975a70d29089b68aea93040",
        test_file=[Path("pandas", "tests", "frame", "test_replace.py")],
        test_cases=[
            "pandas/tests/frame/test_replace.py::TestDataFrameReplace::test_replace_replacer_dtype"
        ],
    )
    Pandas(
        bug_id=122,
        buggy_commit_id="07e6b9d",
        fixed_commit_id="30059081e946a2020d08d49bf4fa7b771d10089a",
        test_file=[Path("pandas", "tests", "internals", "test_internals.py")],
        test_cases=[
            "pandas/tests/internals/test_internals.py::test_dataframe_not_equal"
        ],
    )
    Pandas(
        bug_id=123,
        buggy_commit_id="b6d64d2",
        fixed_commit_id="17fe9a467581ca39f44c89876ebd0d38b9ca77ea",
        test_file=[
            Path("pandas", "tests", "indexes", "test_numeric.py"),
            Path("pandas", "tests", "indexes", "test_range.py"),
        ],
        test_cases=[
            "pandas/tests/indexes/test_numeric.py::TestFloat64Index::test_invalid_dtype",
            "pandas/tests/indexes/test_range.py::TestRangeIndex::test_constructor_same",
            "pandas/tests/indexes/test_range.py::TestRangeIndex::test_constructor_range",
            "pandas/tests/indexes/test_range.py::TestRangeIndex::test_constructor_corner",
        ],
    )
    Pandas(
        bug_id=124,
        buggy_commit_id="deceebe",
        fixed_commit_id="5a0f7e9e03976020ba52a7473f90cb1c8a4354c0",
        test_file=[Path("pandas", "tests", "test_strings.py")],
        test_cases=[
            "pandas/tests/test_strings.py::TestStringMethods::test_empty_str_methods"
        ],
    )
    Pandas(
        bug_id=125,
        buggy_commit_id="e639af2",
        fixed_commit_id="fb08ceeeeba2ba62f92b47d424b3ae83c20ed9db",
        test_file=[
            Path("pandas", "tests", "arrays", "categorical", "test_algos.py"),
            Path("pandas", "tests", "frame", "test_replace.py"),
        ],
        test_cases=[
            "pandas/tests/arrays/categorical/test_algos.py::test_replace",
            "pandas/tests/frame/test_replace.py::TestDataFrameReplace::test_categorical_replace_with_dict",
        ],
    )
    Pandas(
        bug_id=126,
        buggy_commit_id="29be383",
        fixed_commit_id="e639af2afd18b90ab9063df9c1927ae1f357a418",
        test_file=[Path("pandas", "tests", "frame", "test_combine_concat.py")],
        test_cases=[
            "pandas/tests/frame/test_combine_concat.py::TestDataFrameConcatCommon::test_append_empty_list"
        ],
    )
    Pandas(
        bug_id=127,
        buggy_commit_id="f7d6b58",
        fixed_commit_id="710d82c0d393c9031e469ec0371660d8187b7dc3",
        test_file=[Path("pandas", "tests", "series", "test_timeseries.py")],
        test_cases=[
            "pandas/tests/series/test_timeseries.py::TestTimeSeries::test_pct_change_with_duplicate_axis"
        ],
    )
    Pandas(
        bug_id=128,
        buggy_commit_id="794a1c2",
        fixed_commit_id="112e6b8d054f9adc1303138533ed6506975f94db",
        test_file=[Path("pandas", "tests", "io", "json", "test_readlines.py")],
        test_cases=["pandas/tests/io/json/test_readlines.py::test_readjson_unicode"],
    )
    Pandas(
        bug_id=129,
        buggy_commit_id="5b580fb",
        fixed_commit_id="82c9547ddcaf2fd70e00f1368731f14a03bbac88",
        test_file=[Path("pandas", "tests", "arithmetic", "test_timedelta64.py")],
        test_cases=[
            "pandas/tests/arithmetic/test_timedelta64.py::TestTimedeltaArraylikeAddSubOps"
            "::test_td64arr_add_sub_datetimelike_scalar"
        ],
    )
    Pandas(
        bug_id=130,
        buggy_commit_id="7adc14a",
        fixed_commit_id="8efc717e4652e1e4bfbc4455da1d40eb676eed91",
        test_file=[Path("pandas", "tests", "groupby", "test_value_counts.py")],
        test_cases=[
            "pandas/tests/groupby/test_value_counts.py::test_series_groupby_value_counts_with_grouper"
        ],
    )
    Pandas(
        bug_id=131,
        buggy_commit_id="73745be",
        fixed_commit_id="bf5848f111c92fc5c6c11a93a3bc2480f138f1b1",
        test_file=[Path("pandas", "tests", "series", "test_datetime_values.py")],
        test_cases=[
            "pandas/tests/series/test_datetime_values.py::TestSeriesDatetimeValues::test_dt_tz_localize_categorical",
            "pandas/tests/series/test_datetime_values.py::TestSeriesDatetimeValues::test_dt_tz_convert_categorical",
        ],
    )
    Pandas(
        bug_id=132,
        buggy_commit_id="221c8a7",
        fixed_commit_id="bd8f07fb29d2ac819f4c8e8e1b8e6d40f8b0f40c",
        test_file=[Path("pandas", "tests", "reductions", "test_reductions.py")],
        test_cases=[
            "pandas/tests/reductions/test_reductions.py::TestIndexReductions::test_timedelta_ops",
            "pandas/tests/reductions/test_reductions.py::TestSeriesReductions::test_ops_consistency_on_empty",
        ],
    )
    Pandas(
        bug_id=133,
        buggy_commit_id="343544d",
        fixed_commit_id="c983d52e3a3a8a191359814417f375b1dc8b04c1",
        test_file=[Path("pandas", "tests", "frame", "test_missing.py")],
        test_cases=[
            "pandas/tests/frame/test_missing.py::TestDataFrameInterpolate::test_interp_axis_names"
        ],
    )
    Pandas(
        bug_id=134,
        buggy_commit_id="da1401b",
        fixed_commit_id="b1eb97bdfe17f477600eef19e82d65480457bbf5",
        test_file=[Path("pandas", "tests", "tseries", "holiday", "test_calendar.py")],
        test_cases=[
            "pandas/tests/tseries/holiday/test_calendar.py::test_calendar_2031"
        ],
    )
    Pandas(
        bug_id=135,
        buggy_commit_id="0df22b6",
        fixed_commit_id="f41219179de69fed5c2a4b7df821394af1aa6559",
        test_file=[Path("pandas", "tests", "extension", "decimal", "test_decimal.py")],
        test_cases=[
            "pandas/tests/extension/decimal/test_decimal.py::test_groupby_agg",
            "pandas/tests/extension/decimal/test_decimal.py::test_groupby_agg_ea_method",
        ],
    )
    Pandas(
        bug_id=136,
        buggy_commit_id="3954fa7",
        fixed_commit_id="6241b9d3b3b8fd688cf32e45539719f1b9ec25c1",
        test_file=[Path("pandas", "tests", "reshape", "merge", "test_merge_asof.py")],
        test_cases=[
            "pandas/tests/reshape/merge/test_merge_asof.py::TestAsOfMerge::test_int_type_tolerance"
        ],
    )
    Pandas(
        bug_id=137,
        buggy_commit_id="a1b2c4b",
        fixed_commit_id="48f1a67469c91c38e78ebb2648061fe73dd79e6b",
        test_file=[
            Path("pandas", "tests", "extension", "test_categorical.py"),
            Path("pandas", "tests", "reshape", "merge", "test_merge.py"),
        ],
        test_cases=[
            "pandas/tests/extension/test_categorical.py::TestCasting::test_cast_category_to_extension_dtype",
            "pandas/tests/reshape/merge/test_merge.py::test_merge_on_cat_and_ext_array",
        ],
    )
    Pandas(
        bug_id=138,
        buggy_commit_id="3dcbec5",
        fixed_commit_id="c59c2df94e5563819a824f49fa6f55636bdb4445",
        test_file=[Path("pandas", "tests", "reshape", "test_qcut.py")],
        test_cases=[
            "pandas/tests/reshape/test_qcut.py::test_qcut_bool_coercion_to_int"
        ],
    )
    Pandas(
        bug_id=139,
        buggy_commit_id="7705cd2",
        fixed_commit_id="0ffdbe36f0df732f2700cda4a84be758084ff901",
        test_file=[Path("pandas", "tests", "groupby", "test_categorical.py")],
        test_cases=[
            "pandas/tests/groupby/test_categorical.py::test_preserve_categories"
        ],
    )
    Pandas(
        bug_id=140,
        buggy_commit_id="3b19e1d",
        fixed_commit_id="4375daffeed16531bae3fdaf85324b590d1dcb59",
        test_file=[Path("pandas", "tests", "groupby", "test_apply.py")],
        test_cases=["pandas/tests/groupby/test_apply.py::test_apply_datetime_issue"],
    )
    Pandas(
        bug_id=141,
        buggy_commit_id="b298696",
        fixed_commit_id="411dd249e755d7e281603fe3e0ab9e0e48383df9",
        test_file=[Path("pandas", "tests", "indexes", "test_range.py")],
        test_cases=[
            "pandas/tests/indexes/test_range.py::TestRangeIndex::test_get_indexer_decreasing"
        ],
    )
    Pandas(
        bug_id=142,
        buggy_commit_id="7721f31",
        fixed_commit_id="65815e6f33e25991e3d40a53c581ffb3c7daf70f",
        test_file=[Path("pandas", "tests", "series", "test_analytics.py")],
        test_cases=[
            "pandas/tests/series/test_analytics.py::TestSeriesAnalytics::test_bool_diff"
        ],
    )
    Pandas(
        bug_id=143,
        buggy_commit_id="c13c13b",
        fixed_commit_id="df918becf698741861da0e9b7e810d477b0eb194",
        test_file=[
            Path("pandas", "tests", "frame", "test_indexing.py"),
            Path("pandas", "tests", "indexes", "test_range.py"),
        ],
        test_cases=[
            "pandas/tests/frame/test_indexing.py::TestDataFrameIndexing::test_reindex_limit",
            "pandas/tests/indexes/test_range.py::TestRangeIndex::test_get_indexer_limit",
        ],
    )
    Pandas(
        bug_id=144,
        buggy_commit_id="b106108",
        fixed_commit_id="ffe6cfdbf82d663c3f77567bde11f1666de1df38",
        test_file=[Path("pandas", "tests", "plotting", "test_series.py")],
        test_cases=[
            "pandas/tests/plotting/test_series.py::TestSeriesPlots::test_xtick_barPlot"
        ],
    )
    Pandas(
        bug_id=145,
        buggy_commit_id="3bd222d",
        fixed_commit_id="f08a1e62e31fc11e7e5bd7bec72b7e6d86473423",
        test_file=[Path("pandas", "tests", "frame", "test_arithmetic.py")],
        test_cases=[
            "pandas/tests/frame/test_arithmetic.py::TestFrameArithmetic::test_td64_op_nat_casting"
        ],
    )
    Pandas(
        bug_id=146,
        buggy_commit_id="5ebb1e4",
        fixed_commit_id="74cba561ece511e24abb5145225bf98a929ca6c9",
        test_file=[Path("pandas", "tests", "dtypes", "test_missing.py")],
        test_cases=[
            "pandas/tests/dtypes/test_missing.py::test_array_equivalent_tzawareness"
        ],
    )
    Pandas(
        bug_id=147,
        buggy_commit_id="6acfc75",
        fixed_commit_id="773f341c8cc5a481a5a222508718034457ed1ebc",
        test_file=[Path("pandas", "tests", "dtypes", "test_dtypes.py")],
        test_cases=[
            "pandas/tests/dtypes/test_dtypes.py::TestDatetimeTZDtype::test_construct_from_string_raises"
        ],
    )
    Pandas(
        bug_id=148,
        buggy_commit_id="4ac7f9d",
        fixed_commit_id="95edcf1cbee630e42daca0404c44d8128ea156fb",
        test_file=[Path("pandas", "tests", "frame", "test_apply.py")],
        test_cases=[
            "pandas/tests/frame/test_apply.py::TestDataFrameApply::test_apply_funcs_over_empty",
            "pandas/tests/frame/test_apply.py::TestDataFrameApply::test_nunique_empty",
        ],
    )
    Pandas(
        bug_id=149,
        buggy_commit_id="0d69d91",
        fixed_commit_id="fa1364d1299a53093bc704f9c34c595b602a568b",
        test_file=[Path("pandas", "tests", "io", "test_gcs.py")],
        test_cases=["pandas/tests/io/test_gcs.py::test_to_parquet_gcs_new_file"],
    )
    Pandas(
        bug_id=150,
        buggy_commit_id="54e9b75",
        fixed_commit_id="d38627b5889db3f663cad339fe8f995af823b76b",
        test_file=[Path("pandas", "tests", "dtypes", "test_missing.py")],
        test_cases=[
            "pandas/tests/dtypes/test_missing.py::test_array_equivalent_nested"
        ],
    )
    Pandas(
        bug_id=151,
        buggy_commit_id="6110608",
        fixed_commit_id="5a227a410c520ceec2d94369a44e2ab774a40dc3",
        test_file=[Path("pandas", "tests", "arrays", "test_numpy.py")],
        test_cases=[
            "pandas/tests/arrays/test_numpy.py::test_setitem_object_typecode",
            "pandas/tests/arrays/test_numpy.py::test_setitem_no_coercion",
        ],
    )
    Pandas(
        bug_id=152,
        buggy_commit_id="eb8cce0",
        fixed_commit_id="f61deb962ac0853595a43ad024c482b018d1792b",
        test_file=[Path("pandas", "tests", "series", "test_combine_concat.py")],
        test_cases=[
            "pandas/tests/series/test_combine_concat.py::TestSeriesCombine::test_append_tuples"
        ],
    )
    Pandas(
        bug_id=153,
        buggy_commit_id="ae22b80",
        fixed_commit_id="0c0a0cfbadcf01864d499599712edc9022eea12e",
        test_file=[Path("pandas", "tests", "io", "formats", "test_to_csv.py")],
        test_cases=[
            "pandas/tests/io/formats/test_to_csv.py::TestToCSV::test_to_csv_na_rep_long_string"
        ],
    )
    Pandas(
        bug_id=154,
        buggy_commit_id="3f5b5c4",
        fixed_commit_id="e0c63b4cfaa821dfe310f4a8a1f84929ced5f5bd",
        test_file=[Path("pandas", "tests", "groupby", "test_groupby.py")],
        test_cases=["pandas/tests/groupby/test_groupby.py::test_shift_bfill_ffill_tz"],
    )
    Pandas(
        bug_id=155,
        buggy_commit_id="4252ab7",
        fixed_commit_id="0bde7cedf46209a9fd4fa8c7f9fbce8b49aa78cd",
        test_file=[Path("pandas", "tests", "window", "test_rolling.py")],
        test_cases=[
            "pandas/tests/window/test_rolling.py::TestRolling::test_rolling_datetime"
        ],
    )
    Pandas(
        bug_id=156,
        buggy_commit_id="42d6ee7",
        fixed_commit_id="05cc95971e56b503d4df9911a44cd60a7b74cc79",
        test_file=[Path("pandas", "tests", "sparse", "frame", "test_frame.py")],
        test_cases=[
            "pandas/tests/sparse/frame/test_frame.py::TestSparseDataFrameArithmetic::test_add_series_retains_dtype"
        ],
    )
    Pandas(
        bug_id=157,
        buggy_commit_id="b1c871c",
        fixed_commit_id="def01cf7bbb5ef8c9bf2e19737ea918e6a76a143",
        test_file=[Path("pandas", "tests", "reshape", "merge", "test_merge_asof.py")],
        test_cases=[
            "pandas/tests/reshape/merge/test_merge_asof.py::TestAsOfMerge::test_timedelta_tolerance_nearest"
        ],
    )
    Pandas(
        bug_id=158,
        buggy_commit_id="a76df79",
        fixed_commit_id="b1c871ce4b5e76b3cffe1ebd4216d36379872352",
        test_file=[Path("pandas", "tests", "series", "test_alter_axes.py")],
        test_cases=[
            "pandas/tests/series/test_alter_axes.py::TestSeriesAlterAxes::test_rename_with_custom_indexer",
            "pandas/tests/series/test_alter_axes.py::TestSeriesAlterAxes::test_rename_with_custom_indexer_inplace",
        ],
    )
    Pandas(
        bug_id=159,
        buggy_commit_id="e55b698",
        fixed_commit_id="62ab439b168d972546e06d329916c6be7ddd1288",
        test_file=[Path("pandas", "tests", "arithmetic", "test_numeric.py")],
        test_cases=[
            "pandas/tests/arithmetic/test_numeric.py::test_fill_value_inf_masking",
            "pandas/tests/arithmetic/test_numeric.py::test_dataframe_div_silenced",
        ],
    )
    Pandas(
        bug_id=160,
        buggy_commit_id="489d1ff",
        fixed_commit_id="fb62fcf91c874e9c24fa83693c4e6e613f35f864",
        test_file=[Path("pandas", "tests", "test_expressions.py")],
        test_cases=[
            "pandas/tests/test_expressions.py::TestExpressions::test_frame_series_axis"
        ],
    )
    Pandas(
        bug_id=161,
        buggy_commit_id="a818281",
        fixed_commit_id="ca5198a6daa7757e398112a17ccadc9e7d078d96",
        test_file=[Path("pandas", "tests", "series", "test_missing.py")],
        test_cases=[
            "pandas/tests/series/test_missing.py::TestSeriesMissingData::test_fillna_categorical_with_new_categories"
        ],
    )
    Pandas(
        bug_id=162,
        buggy_commit_id="341043d",
        fixed_commit_id="640d9e1f5fe8ab64d1f6496b8216c28185e53225",
        test_file=[Path("pandas", "tests", "reshape", "test_pivot.py")],
        test_cases=[
            "pandas/tests/reshape/test_pivot.py::TestCrosstab::test_margin_normalize"
        ],
    )
    Pandas(
        bug_id=163,
        buggy_commit_id="61819ab",
        fixed_commit_id="f669f94a186ea444cc771985a915e90eecf218a9",
        test_file=[Path("pandas", "tests", "window", "test_rolling.py")],
        test_cases=[
            "pandas/tests/window/test_rolling.py::TestRolling::test_readonly_array"
        ],
    )
    Pandas(
        bug_id=164,
        buggy_commit_id="ac69333",
        fixed_commit_id="61819aba14dd7b3996336aaed84d07cd936d92b5",
        test_file=[Path("pandas", "tests", "indexes", "datetimes", "test_tools.py")],
        test_cases=[
            "pandas/tests/indexes/datetimes/test_tools.py::TestToDatetimeMisc::test_to_datetime_dta_tz"
        ],
    )
    Pandas(
        bug_id=165,
        buggy_commit_id="9fe8a0f",
        fixed_commit_id="9b1c005142fed227081dd454eab1a414168d458e",
        test_file=[Path("pandas", "tests", "arithmetic", "test_datetime64.py")],
        test_cases=[
            "pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexArithmetic::test_dta_add_sub_index"
        ],
    )
    Pandas(
        bug_id=166,
        buggy_commit_id="4056ded",
        fixed_commit_id="d44fb07063e9a8bd8a209ddce35b40d8a56c8d02",
        test_file=[Path("pandas", "tests", "frame", "test_join.py")],
        test_cases=[
            "pandas/tests/frame/test_join.py::test_suppress_future_warning_with_sort_kw"
        ],
    )
    Pandas(
        bug_id=167,
        buggy_commit_id="6af6d51",
        fixed_commit_id="226398224d260d908a1f3d0f23c16fa9ffc8f9b0",
        test_file=[
            Path("pandas", "tests", "indexes", "datetimes", "test_partial_slicing.py")
        ],
        test_cases=[
            "pandas/tests/indexes/datetimes/test_partial_slicing.py::TestSlicing::test_slice_reduce_to_series"
        ],
    )
    Pandas(
        bug_id=168,
        buggy_commit_id="2de4fbb",
        fixed_commit_id="1fa1ad91b29c5474cbb86cbcbcdcd50537cad0ae",
        test_file=[Path("pandas", "tests", "groupby", "test_groupby.py")],
        test_cases=["pandas/tests/groupby/test_groupby.py::test_groupby_axis_1"],
    )
    Pandas(
        bug_id=169,
        buggy_commit_id="4d9016e",
        fixed_commit_id="01babb590cb15ef5c6e9ad890ea580a5112e6999",
        test_file=[Path("pandas", "tests", "frame", "test_quantile.py")],
        test_cases=[
            "pandas/tests/frame/test_quantile.py::TestDataFrameQuantile::test_quantile_empty_no_columns"
        ],
    )


class PandasAPI(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> TestResult:
        return TestResult.UNDEFINED

    def execute(self, system_test_path: PathLike, environ: Environment) -> Any:
        pass

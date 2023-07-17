import abc
from os import PathLike
from pathlib import Path
from typing import List, Optional, Any

from tests4py.constants import Environment
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult


class Ansible(Project):
    def __init__(
        self,
        bug_id: int,
        python_version: str,
        python_path: str,
        buggy_commit_id: str,
        fixed_commit_id: str,
        test_file: List[Path],
        test_cases: List[str],
        darwin_python_version: Optional[str] = None,
        test_status_fixed: TestStatus = TestStatus.PASSING,
        test_status_buggy: TestStatus = TestStatus.FAILING,
        unittests: Optional[UnittestGenerator] = None,
        systemtests: Optional[SystemtestGenerator] = None,
        api: Optional[API] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name="ansible",
            github_url="https://github.com/ansible/ansible",
            status=Status.OK,
            cause="N.A.",
            python_version=python_version,
            python_path=python_path,
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_file=test_file,
            test_cases=test_cases,
            darwin_python_version=darwin_python_version,
            python_fallback_version=darwin_python_version,
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
        )  # TODO adjust parameters


# REGISTER BUGS


def register():
    Ansible(
        bug_id=1,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="25c5388fdec9e56517a93feb5e8d485680946c25",
        fixed_commit_id="343ffaa18b63c92e182b16c3ad84b8d81ca4df69",
        test_file=[Path("test", "units", "galaxy", "test_collection.py")],
        test_cases=[
            "test/units/galaxy/test_collection.py::test_verify_collections_no_version"
        ],
        test_status_buggy=TestStatus.PASSING,
    )
    Ansible(
        bug_id=2,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="de59b17c7f69d5cfb72479b71776cc8b97e29a6b",
        fixed_commit_id="5b9418c06ca6d51507468124250bb58046886be6",
        test_file=[Path("test", "units", "utils", "test_version.py")],
        test_cases=[
            "test/units/utils/test_version.py::test_alpha",
            "test/units/utils/test_version.py::test_numeric",
        ],
        test_status_buggy=TestStatus.PASSING,
    )
    Ansible(
        bug_id=3,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="70219df9056ffb1e2766f572fbe71f7a1800c9f5",
        fixed_commit_id="9d48884e36fb4fd9551f000b87d264383de74e75",
        test_file=[
            Path("test", "units", "module_utils", "test_distribution_version.py")
        ],
        test_cases=[
            "test/units/module_utils/test_distribution_version.py::test_distribution_version",
        ],
    )
    Ansible(
        bug_id=4,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="d91658ec0c8434c82c3ef98bfe9eb4e1027a43a3",
        fixed_commit_id="18a66e291dad71128a32d662aa808213acefe0e9",
        test_file=[Path("test", "units", "playbook", "test_collectionsearch.py")],
        test_cases=[
            "test/units/playbook/test_collectionsearch.py::test_collection_static_warning",
        ],
    )
    Ansible(
        bug_id=5,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="2af76f16be8cf2239daaec4c2f31c3dcb4e3469e",
        fixed_commit_id="3c3ffc09c203d1b2262f6a319cceadd727749761",
        test_file=[
            Path(
                "test",
                "units",
                "module_utils",
                "common",
                "validation",
                "test_check_required_arguments.py",
            )
        ],
        test_cases=[
            "test/units/module_utils/common/validation/"
            "test_check_required_arguments.py::test_check_required_arguments_missing_multiple",
        ],
    )
    Ansible(
        bug_id=6,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="90898132e456ee1993db99a1531379f1b98ee915",
        fixed_commit_id="4881af2e7e0506ada0225fd764e874e20569d5b2",
        test_file=[Path("test", "units", "galaxy", "test_collection_install.py")],
        test_cases=[
            "test/units/galaxy/test_collection_install.py::test_build_requirement_from_path_with_manifest",
            "test/units/galaxy/test_collection_install.py::test_build_requirement_from_path_no_version",
            "test/units/galaxy/test_collection_install.py::test_add_collection_requirement_to_unknown_installed_version",
        ],
    )
    Ansible(
        bug_id=7,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="cd146b836e032df785ecd9eb711c6ef23c2228b8",
        fixed_commit_id="cd146b836e032df785ecd9eb711c6ef23c2228b8",
        test_file=[
            Path("test", "units", "modules", "network", "eos", "test_eos_vlans.py")
        ],
        test_cases=[
            "test/units/modules/network/eos/test_eos_vlans.py::TestEosVlansModule::test_eos_vlan_replaced",
        ],
    )
    Ansible(
        bug_id=8,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="81378b3e744cd0d13b33d18a4f8a38aeb8a6e97a",
        fixed_commit_id="fc7980af9a42676913b4054163570ee438b82e9c",
        test_file=[Path("test", "units", "plugins", "shell", "test_powershell.py")],
        test_cases=[
            "test/units/plugins/shell/test_powershell.py::test_join_path_unc",
        ],
    )
    Ansible(
        bug_id=9,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="9276dd2007a73172ed99ab5a56cded4298d3cd2b",
        fixed_commit_id="6f1bb37feb81acd99157f5ba0933fecd747015a2",
        test_file=[
            Path(
                "test",
                "units",
                "modules",
                "packaging",
                "os",
                "test_redhat_subscription.py",
            )
        ],
        test_cases=[
            "test/units/modules/packaging/os/test_redhat_subscription.py::test_redhat_subscribtion",
        ],
    )
    Ansible(
        bug_id=10,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="e368f788f71c338cd3f049d5d6bdc643a51c0514",
        fixed_commit_id="a4b59d021368285490f7cda50c11ac4f7a8030b5",
        test_file=[Path("test", "units", "modules", "system", "test_pamd.py")],
        test_cases=[
            "test/units/modules/system/test_pamd.py::PamdServiceTestCase::test_remove_first_rule",
            "test/units/modules/system/test_pamd.py::PamdServiceTestCase::test_remove_last_rule",
        ],
    )
    Ansible(
        bug_id=11,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="da07b98b7a433493728ddb7ac7efbd20b8988776",
        fixed_commit_id="52f3ce8a808f943561803bd664e695fed1841fe8",
        test_file=[
            Path("test", "units", "modules", "network", "ios", "test_ios_banner.py")
        ],
        test_cases=[
            "test/units/modules/network/ios/test_ios_banner.py::TestIosBannerModule::test_ios_banner_nochange",
            "test/units/modules/network/ios/test_ios_banner.py::TestIosBannerIos12Module::test_ios_banner_nochange",
        ],
    )
    Ansible(
        bug_id=12,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="05e2e1806162393d76542a75c2520c7d61c2d855",
        fixed_commit_id="2fa8f9cfd80daf32c7d222190edf7cfc7234582a",
        test_file=[Path("test", "units", "plugins", "lookup", "test_env.py")],
        test_cases=[
            "test/units/plugins/lookup/test_env.py",
        ],
    )
    Ansible(
        bug_id=13,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="41472ee3878be215af8b933b2b04b4a72b9165ca",
        fixed_commit_id="694ef5660d45fcb97c9beea5b2750f6eadcf5e93",
        test_file=[Path("test", "units", "cli", "test_galaxy.py")],
        test_cases=[
            "test/units/cli/test_galaxy.py::test_collection_install_with_url",
        ],
    )
    Ansible(
        bug_id=14,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="a1ab093ddbd32f1002cbf6d6f184c7d0041d890d",
        fixed_commit_id="7acae62fa849481b2a5e2e2d56961c5e1dcea96c",
        test_file=[Path("test", "units", "galaxy", "test_api.py")],
        test_cases=[
            "test/units/galaxy/test_api.py::test_get_role_versions_pagination",
        ],
    )
    Ansible(
        bug_id=15,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="b1e8a6c1cbd2a668b462995487b819ef7dd8ba4b",
        fixed_commit_id="68de182555b185737353e780882159a3d213908c",
        test_file=[
            Path("test", "units", "modules", "network", "eos", "test_eos_eapi.py")
        ],
        test_cases=[
            "test/units/modules/network/eos/test_eos_eapi.py::TestEosEapiModule::test_eos_eapi_vrf",
        ],
    )
    Ansible(
        bug_id=16,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="2a9964ede8b2b77a62a005f6f5abc964b2819b0e",
        fixed_commit_id="93d9d640380252084855885ad27873b4377898ec",
        test_file=[
            Path(
                "test",
                "units",
                "module_utils",
                "facts",
                "hardware",
                "test_linux_get_cpu_info.py",
            )
        ],
        test_cases=[
            "test/units/module_utils/facts/hardware/test_linux_get_cpu_info.py::test_get_cpu_info_missing_arch",
        ],
    )
    Ansible(
        bug_id=17,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="9cb47832d15c61884b30d70f9d4e0f816b064b05",
        fixed_commit_id="b38cb37728df76e0529243bdce694b18ca0e1163",
        test_file=[Path("test", "units", "module_utils", "facts", "test_facts.py")],
        test_cases=[
            "test/units/module_utils/facts/test_facts.py::TestFactsLinuxHardwareGetMountFacts::test_get_mount_facts",
        ],
    )
    Ansible(
        bug_id=18,
        python_version="3.6.9",
        darwin_python_version="3.6.15",
        python_path="ansible/build/lib/",
        buggy_commit_id="70219df9056ffb1e2766f572fbe71f7a1800c9f5",
        fixed_commit_id="9d48884e36fb4fd9551f000b87d264383de74e75",
        test_file=[
            Path("test", "units", "module_utils", "test_distribution_version.py")
        ],
        test_cases=[
            "test/units/module_utils/test_distribution_version.py::test_distribution_version",
        ],
    )


class AnsibleAPI(API, abc.ABC):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> TestResult:
        return TestResult.UNDEFINED

    def execute(self, system_test_path: PathLike, environ: Environment) -> Any:
        return

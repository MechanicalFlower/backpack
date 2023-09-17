import filecmp
from datetime import datetime
from pathlib import Path

from packaging.version import Version
from py.path import local
from pytest_mock import MockerFixture

from backpack.bump_version import replace_version


class TestBumpVersion:

    def test_0001_bump_version(self, tmpdir: local, mocker: MockerFixture,
                               script_loc: Path) -> None:
        mocker.patch('backpack.bump_version.get_today',
                     return_value=datetime(2014, 6, 2))

        input_cfg_file = script_loc.joinpath(
            "resources/bump_version/input_presets.cfg")
        output_cfg_file = tmpdir.mkdir("results").join("presets.cfg")
        excepted_output_cfg_file = script_loc.joinpath(
            "resources/bump_version/excepted_presets.cfg")

        replace_version(Version("1.2.3"), input_cfg_file, output_cfg_file)
        assert filecmp.cmp(output_cfg_file, excepted_output_cfg_file)

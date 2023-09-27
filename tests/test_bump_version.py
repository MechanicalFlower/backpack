import filecmp
from datetime import datetime

from packaging.version import Version

from magic_combo.scripts.bump_version import replace_version


class TestBumpVersion:

    def test_0001_bump_version(self, tmpdir, mocker, script_loc):
        mocker.patch(
            'magic_combo.scripts.bump_version.get_today',
            return_value=datetime(2014, 6, 2)
        )

        input_cfg_file = script_loc.joinpath("resources/bump_version/input_presets.cfg")
        output_cfg_file = tmpdir.mkdir("results").join("presets.cfg")
        excepted_output_cfg_file = script_loc.joinpath(
            "resources/bump_version/excepted_presets.cfg"
        )

        replace_version(Version("1.2.3"), input_cfg_file, output_cfg_file)
        assert filecmp.cmp(output_cfg_file, excepted_output_cfg_file)

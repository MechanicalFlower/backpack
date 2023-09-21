import filecmp

from magic_combo.generate_credits import generate_credits_file, parse_dep5_file


class TestGenerateCredits:

    def test_0001_generate_credits(self, tmpdir, script_loc):
        input_dep5 = script_loc.joinpath(
            "resources/generate_credits/input_dep5")
        output_credits_file = tmpdir.mkdir("results").join("CREDITS.md")
        excepted_output_credits_file = script_loc.joinpath(
            "resources/generate_credits/excepted_credits.md")

        deps = parse_dep5_file(input_dep5)
        for section in ("addons", "models", "textures", "sounds", "fonts",
                        "shaders"):
            assert section in deps

        generate_credits_file(deps, output_credits_file)
        assert filecmp.cmp(output_credits_file, excepted_output_credits_file)

from invoke.context import Context

from .constants import GODOT_URL


class ConfigWrapper:
    @staticmethod
    def godot_version(c: Context) -> str:
        return str(c["godot"]["version"])

    @staticmethod
    def godot_release(c: Context) -> str:
        return str(c["godot"]["release"])

    @staticmethod
    def godot_subdir(c: Context) -> str:
        return str(c["godot"]["subdir"])

    @staticmethod
    def godot_platform(c: Context) -> str:
        return str(c["godot"]["platform"])

    @staticmethod
    def godot_filename(c: Context) -> str:
        return (
            f"Godot_v{ConfigWrapper.godot_version(c)}"
            f"-{ConfigWrapper.godot_release(c)}_{ConfigWrapper.godot_platform(c)}"
        )

    @staticmethod
    def godot_filename_url(c: Context) -> str:
        return (
            f"{GODOT_URL}/"
            f"{ConfigWrapper.godot_version(c)}{ConfigWrapper.godot_subdir(c)}/"
            f"{ConfigWrapper.godot_filename(c)}.zip"
        )

    @staticmethod
    def godot_template(c: Context) -> str:
        return (
            f"Godot_v{ConfigWrapper.godot_version(c)}"
            f"-{ConfigWrapper.godot_release(c)}_export_templates.tpz"
        )

    @staticmethod
    def godot_template_url(c: Context) -> str:
        return (
            f"{GODOT_URL}/"
            f"{ConfigWrapper.godot_version(c)}{ConfigWrapper.godot_subdir(c)}/"
            f"{ConfigWrapper.godot_template(c)}"
        )

    @staticmethod
    def game_name(c: Context) -> str:
        return str(c["game"]["name"])

    @staticmethod
    def game_version(c: Context) -> str:
        return str(c["game"]["version"])

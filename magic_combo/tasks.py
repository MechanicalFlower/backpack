from pathlib import Path

from invoke.collection import Collection
from invoke.context import Context
from invoke.tasks import task

from .scripts.bump_version import read_version_file

GODOT_VERSION = read_version_file(Path('.godot_version'))
RELEASE_NAME = "stable"
SUBDIR = ""
GODOT_PLATFORM = "linux.x86_64"
GODOT_FILENAME = f"Godot_v{GODOT_VERSION}-{RELEASE_NAME}_{GODOT_PLATFORM}"
GODOT_TEMPLATE = f"Godot_v{GODOT_VERSION}-{RELEASE_NAME}_export_templates.tpz"

GAME_NAME = "Greeter"
GAME_VERSION = read_version_file(Path('.version'))


@task()
def makedirs(c: Context) -> None:
    c.run("mkdir -p .combo")
    c.run("mkdir -p .combo/build")
    c.run("mkdir -p .combo/bin")
    c.run("mkdir -p .combo/cache")

    c.run("touch .combo/.gitignore")
    c.run("echo '*' >> .combo/.gitignore")

    c.run("touch .combo/.gdignore")


@task()
def install_godot(c: Context) -> None:
    c.run((
        f"curl -X GET 'https://downloads.tuxfamily.org/godotengine/{GODOT_VERSION}{SUBDIR}/{GODOT_FILENAME}.zip'"
        f" --output .combo/cache/{GODOT_FILENAME}.zip"
    ))
    c.run(f"unzip .combo/cache/{GODOT_FILENAME}.zip -d .combo/cache/")
    c.run("fcp .combo/cache/{GODOT_FILENAME} .combo/bin/{GODOT_FILENAME}")


@task()
def install_templates(c: Context) -> None:
    c.run((
        f"curl -X GET 'https://downloads.tuxfamily.org/godotengine/{GODOT_VERSION}{SUBDIR}/{GODOT_TEMPLATE}'"
        f" --output .combo/cache/{GODOT_TEMPLATE}"
    ))
    c.runf("unzip .combo/cache/{GODOT_TEMPLATE} -d .combo/cache/")
    c.run((
        "mkdir -p ~/.local/share/godot/export_templates"
        f"/{GODOT_VERSION}.{RELEASE_NAME}"
    ))
    c.run((
        "cp .combo/cache/templates/*"
        f" ~/.local/share/godot/export_templates/{GODOT_VERSION}.{RELEASE_NAME}"
    ))


@task(pre=[makedirs])
def install_addons(c: Context) -> None:
    c.run(f".combo/bin/{GODOT_FILENAME} --headless --script plug.gd install || true")


@task(pre=[makedirs])
def import_resources(c: Context) -> None:
    c.run(f".combo/bin/{GODOT_FILENAME} --headless --export-pack null /dev/null")


@task()
def export_release_linux(c: Context) -> None:
    c.run("mkdir -p .combo/build/linux")
    c.run((
        f".combo/bin/{GODOT_FILENAME}"
        " --export-release 'Linux/X11'"
        f" --headless .combo/build/linux/{GAME_NAME}.x86_64"
    ))
    c.run((
        "(cd .combo/build/linux"
        f" && zip {GAME_NAME}-linux-v{GAME_VERSION}.zip -r .)"
    ))
    c.run((
        f"mv .combo/build/linux/{GAME_NAME}-linux-v{GAME_VERSION}.zip"
        f" .combo/build/{GAME_NAME}-linux-v{GAME_VERSION}.zip"
    ))


@task()
def export_release_windows(c: Context) -> None:
    c.run("mkdir -p .combo/build/windows")
    c.run((
        f".combo/bin/{GODOT_FILENAME}"
        " --export-release 'Windows Desktop'"
        f" --headless .combo/build/windows/{GAME_NAME}.exe"
    ))
    c.run((
        "(cd .combo/build/windows"
        f" && zip {GAME_NAME}-windows-v{GAME_VERSION}.zip -r .)"
    ))
    c.run((
        f"mv .combo/build/windows/{GAME_NAME}-windows-v{GAME_VERSION}.zip"
        f" .combo/build/{GAME_NAME}-windows-v{GAME_VERSION}.zip"
    ))


@task()
def export_release_mac(c: Context) -> None:
    c.run((
        f".combo/bin/{GODOT_FILENAME}"
        " --export-release 'macOS'"
        f" --headless .combo/build/{GAME_NAME}-mac-v{GAME_VERSION}.zip"
    ))


@task()
def editor(c: Context) -> None:
    c.run(f".combo/bin/{GODOT_FILENAME} --editor")


@task()
def godot(c: Context) -> None:
    c.run(f".combo/bin/{GODOT_FILENAME} $(ARGS)")


@task()
def run_release(c: Context) -> None:
    c.run(f".combo/build/linux/{GAME_NAME}.x86_64")


@task()
def clean_combo(c: Context) -> None:
    c.run("rm -rf .combo")


@task()
def clean_godot(c: Context) -> None:
    c.run("rm -rf .godot")


@task()
def clean_plug(c: Context) -> None:
    c.run("rm -rf .plugged")
    c.run((
        "find addons/"
        " -type d"
        " -not -name 'addons' -not -name 'gd-plug'"
        " -exec rm -rf {} \; || true"
    ))


task_ns = Collection('task')
task_ns.add_task(clean_godot)
task_ns.add_task(clean_combo)
task_ns.add_task(clean_plug)
task_ns.add_task(godot)
task_ns.add_task(editor)
task_ns.add_task(export_release_linux)
task_ns.add_task(export_release_mac)
task_ns.add_task(export_release_windows)
task_ns.add_task(import_resources)
task_ns.add_task(install_addons)
task_ns.add_task(install_godot)
task_ns.add_task(install_templates)
task_ns.add_task(run_release)
task_ns.add_task(makedirs)

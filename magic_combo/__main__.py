import sys

from invoke.collection import Collection
from invoke.program import Program

from .playbooks import playbook_ns
from .scripts import script_ns
from .tasks import task_ns

ns = Collection(playbook_ns, task_ns, script_ns)


def main() -> None:
    program = Program(version='0.2.0', namespace=ns)
    program.run()
    sys.exit(1)


main()

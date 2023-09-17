from pathlib import Path

import pytest


@pytest.fixture(scope="module")
def script_loc(request):
    """Return the directory of the currently running test script"""

    return Path(request.fspath).parent

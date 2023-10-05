import nox


@nox.session
def lint(session: nox.Session) -> None:
    session.install("poetry")
    session.run("poetry", "install")
    session.run("pre-commit", "run", "-a")


@nox.session(python=["3.10", "3.11", "3.12"])
def test(session: nox.Session) -> None:
    session.install("poetry")
    session.run("poetry", "install")
    session.run("pytest")

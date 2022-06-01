import os

from tomlkit import load, TOMLDocument


def test_locate():
    with open(os.path.join(os.path.dirname(__file__), "examples", "example" + ".toml"),
        encoding="utf-8",) as fp:
        document = load(fp)
        assert isinstance(document, TOMLDocument)

# See the documenteer.toml for overrides of the Rubin user guide presets

from documenteer.conf.guide import *

html_theme = "pydata_sphinx_theme"

exclude_patterns = [
    r"_build",
    r"README.rst",
    r"README.md",
    r".venv",
    r"venv",
    r"requirements.txt",
    r".github",
    r".tox",
    r"project/templates/template-folder",
]

# See the documenteer.toml for overrides of the Rubin user guide presets

from documenteer.conf.guide import *  # noqa: F403

exclude_patterns.append(  # noqa: F405
    r"project/templates/template-folder",
)

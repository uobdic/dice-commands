# DICE Command Line Interface (CLI)

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]
[![Gitter][gitter-badge]][gitter-link]


[actions-badge]:            https://github.com/uobdic/dice-cli/workflows/CI/badge.svg
[actions-link]:             https://github.com/uobdic/dice-cli/actions
[black-badge]:              https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]:               https://github.com/psf/black
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/uobdic/dice-cli/discussions
[gitter-badge]:             https://badges.gitter.im/https://github.com/uobdic/dice-cli/community.svg
[gitter-link]:              https://gitter.im/https://github.com/uobdic/dice-cli/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
[pypi-link]:                https://pypi.org/project/dice-cli/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/dice-cli
[pypi-version]:             https://badge.fury.io/py/dice-cli.svg
[rtd-badge]:                https://readthedocs.org/projects/dice-cli/badge/?version=latest
[rtd-link]:                 https://dice-cli.readthedocs.io/en/latest/?badge=latest

## Installation

The best way to install `dice-cli` is via `pipx`.
This will setup a separate `virtualenv` for `dice-cli` preventing interference with your normal Python setup.

```bash
pipx install dice-cli
```

For tab-completion of the DICE CLI, you can run

```bash
dice --install-completion
```

which will install the completion for your shell.

Should you be using a "non-standard" shell, you can check what will be installed through

```bash
dice --show-completion
```

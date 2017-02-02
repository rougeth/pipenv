import os

# Shell compatibility mode, for mis-configured shells.
PIPENV_SHELL_COMPAT = os.environ.get('PIPENV_SHELL_COMPAT')

# No color mode, for unfun people.
PIPENV_COLORBLIND = os.environ.get('PIPENV_COLORBLIND')

# User-configuraable max-depth for Pipfile searching.
PIPENV_MAX_DEPTH = int(os.environ.get('PIPENV_MAX_DEPTH', '3'))
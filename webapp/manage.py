#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Redirect the stdout and stderr streams to sys.__stdout__ and sys.__stderr__
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

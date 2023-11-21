#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geeks_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

import logging
import os
from datetime import datetime


year, month, day = datetime.now().year, datetime.now().month, datetime.now().day
module_name = os.path.splitext(os.path.basename(__file__))[0]
logger_path = f"logs/{year}/{month}/{day}/"
if not os.path.exists(logger_path):
    os.makedirs(logger_path)
logger2 = logging.getLogger(module_name)
logger2.setLevel(logging.INFO)
# настройка обработчика и форматировщика для logger2
handler2 = logging.FileHandler(f"{logger_path}/{module_name}.log", mode='a')
formatter2 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
# добавление форматировщика к обработчику
handler2.setFormatter(formatter2)
# добавление обработчика к логгеру
logger2.addHandler(handler2)
logger2.info(f"Running module {module_name}...")

errors = (AssertionError,AttributeError,EOFError,FloatingPointError,
    GeneratorExit,ImportError,IndexError,KeyError,MemoryError,
    NotImplementedError,OSError,OverflowError,ReferenceError,StopIteration,
    IndentationError,TabError,SystemError,SystemExit,TypeError,UnboundLocalError,UnicodeError,UnicodeEncodeError,
    UnicodeDecodeError,UnicodeTranslateError,ValueError,ZeroDivisionError,RuntimeError, TypeError, NameError,
    SyntaxError,Exception,ValueError,KeyboardInterrupt)

try:
    #your actual code
    x = int(input("Please enter a number: "))
    logger2.info("Successful run")
except errors as err:
    logger2.exception("Some kind of error, check log file")
if __name__ == '__main__':
    main()

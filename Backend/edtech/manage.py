#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import multiprocessing
import time
from model import scrape_the_news

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edtech.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def init_scrape():
    print('do this once')

def start_scrape():
    while True:
        scrape_the_news()
        time.sleep(300)



if __name__ == '__main__':
    # main()
    #p = multiprocessing.Pool(2)
    p1 = multiprocessing.Process(target=main, args=())
    p2 = multiprocessing.Process(target=start_scrape, args=())

    p1.start()
    p2.start()

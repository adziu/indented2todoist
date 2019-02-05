#!/usr/bin/env python3
# coding: utf-8

import click

# input
INITIAL_INDENT = ' ' * 5
INDENT = ' ' * 4


@click.command(
    help='Indented text file paths to convert to CSV',
)
@click.argument(
    'indented_text',
    nargs=-1,
    type=click.File(),
)
def indented(indented_text):
    """Convert indented *.txt files into *.csv for Todoist."""
    for f in indented_text:
        print(f, f.name)


# output
HEADER = (
    'TYPE,CONTENT,PRIORITY,INDENT,AUTHOR,RESPONSIBLE,DATE,DATE_LANG,TIMEZONE'
)
USER = 'Adrian (21609785)'
DEFAULTS = 'task,{content},4,1,{USER},,,en,Europe/Warsaw'


# click entry point
if __name__ == '__main__':
    indented()

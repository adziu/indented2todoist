#!/usr/bin/env python3
# coding: utf-8

import click

@click.command(
    help='Convert indented text files to CSV',
)
@click.argument(
    'indented',
    nargs=-1,
    type=click.File(),
)
def indented_command(indented):
    """Convert indented *.txt files into *.csv for Todoist."""
    for indented_file in indented:
        tasks = _indented_tasks(indented_file)


# input
INITIAL_INDENT = ' ' * 5
INDENT = ' ' * 4


def _indented_tasks(lines):
    yield from _strip_header_and_initial_indent(lines)


def _strip_header_and_initial_indent(lines):
    lines_iter = iter(lines)
    next(lines_iter, None)
    for line in lines_iter:
        without_initial = line[len(INITIAL_INDENT):]
        yield without_initial


# output
HEADER = (
    'TYPE,CONTENT,PRIORITY,INDENT,AUTHOR,RESPONSIBLE,DATE,DATE_LANG,TIMEZONE'
)
USER = 'Adrian (21609785)'
DEFAULTS = 'task,{content},4,1,{USER},,,en,Europe/Warsaw'


# click entry point
if __name__ == '__main__':
    indented_command()

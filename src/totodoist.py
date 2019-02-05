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
        print(list(tasks))


# input
INITIAL_INDENT = ' ' * 5
INDENT = ' ' * 4


def _indented_tasks(lines):
    for task_line in _strip_noise(lines):
        yield _indent_content(task_line)


def _strip_noise(lines):
    lines_iter = iter(lines)
    next(lines_iter, None)
    for line in lines_iter:
        without_initial = line[len(INITIAL_INDENT):]
        without_newline = without_initial.rstrip('\n')
        yield without_newline


def _indent_content(task_line):
    stripped = task_line.lstrip()
    indent_depth = (len(task_line) - len(stripped)) // len(INDENT) + 1
    return indent_depth, stripped

# output
HEADER = (
    'TYPE,CONTENT,PRIORITY,INDENT,AUTHOR,RESPONSIBLE,DATE,DATE_LANG,TIMEZONE'
)
USER = 'Adrian (21609785)'
DEFAULTS = 'task,{content},4,{indent_depth},{USER},,,en,Europe/Warsaw'


# click entry point
if __name__ == '__main__':
    indented_command()

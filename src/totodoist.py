#!/usr/bin/env python3
# coding: utf-8
import os

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
        csv_file_path = os.path.splitext(indented_file.name)[0] + '.csv'
        with open(csv_file_path, mode='w') as csv_file:
            csv_file.writelines(_csv_output(tasks))


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
        line = line[len(INITIAL_INDENT):]
        line = line.rstrip('\n')
        yield line


def _indent_content(task_line):
    stripped = task_line.lstrip()
    indent_depth = (len(task_line) - len(stripped)) // len(INDENT) + 1
    return indent_depth, stripped

# output
HEADER = (
    'TYPE,CONTENT,PRIORITY,INDENT,AUTHOR,RESPONSIBLE,DATE,DATE_LANG,TIMEZONE'
)
USER = 'Adrian (21609785)'
DEFAULTS = 'task,{content},4,{indent},{user},,,en,Europe/Warsaw'


def _csv_output(tasks):
    yield HEADER + '\n'
    for indent, content in tasks:
        yield DEFAULTS.format(
            indent=indent,
            content=content,
            user=USER
        ) + '\n'


# click entry point
if __name__ == '__main__':
    indented_command()

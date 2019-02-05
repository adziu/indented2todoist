#!/usr/bin/env python3
# coding: utf-8

import totodoist


def test_strip_noise():
    input_lines = '''\
task_list_name
     task_not_indented
         task_indented'''.split('\n')
    expected = '''\
task_not_indented
    task_indented'''.split('\n')
    result = list(totodoist._strip_noise(input_lines))
    assert result == expected


def test_indent_content():
    input_line = ' ' * 8 + 'task_proper'
    expected = 3, 'task_proper'  # no indentation is 1
    assert totodoist._indent_content(input_line) == expected

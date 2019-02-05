#!/usr/bin/env python3
# coding: utf-8

import totodoist


def test_strip_header_and_initial_indent():
    input_lines = '''\
task_list_name
     task_not_indented
         task_indented'''.split('\n')
    expected = '''\
task_not_indented
    task_indented'''.split('\n')
    result = list(totodoist._strip_header_and_initial_indent(input_lines))
    assert result == expected

# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest

from dotable import DotableDict, DotableList, parse


class TestCore(unittest.TestCase):

    def setUp(self):
        self.dictionary = {
            'first_key': {
                'nested_dict': {
                    'val1': 'val1',
                    'int1': 1,
                },
                'nested_list': [1, 2, 3],
            },
            'second_key': {
                'nested_dict': {
                    'val1': 'val1',
                    'int1': 1,
                },
                'nested_list': [1, 2, 3],
            }
        }

        self.list = [
            [
                {
                    'nested_dict': {
                        'val1': 'val1',
                        'int1': 1,
                    },
                    'nested_list': [1, 2, 3],
                }
            ],
            {
                'nested_dict': {
                    'val1': 'val1',
                    'int1': 1,
                },
                'nested_list': [1, 2, 3],
            }, {
                'nested_dict': {},
                'nested_list': [1, 2, 3],
            }
        ]

    def test_dict(self):
        d = DotableDict(self.dictionary)

        self.assertEqual(d.first_key.nested_dict.val1, 'val1')

    def test_list(self):
        l = DotableList(self.list)

        self.assertEqual(l[1].nested_dict.int1, 1)
        self.assertEqual(l[0][0].nested_list[2], 3)

    def test_parse(self):
        item_d = parse(self.dictionary)
        self.assertEqual(item_d.first_key.nested_dict.val1, 'val1')

        item_l = parse(self.list)

        self.assertEqual(item_l[1].nested_dict.int1, 1)
        self.assertEqual(item_l[0][0].nested_list[2], 3)

    def test_parse_invalid(self):
        with self.assertRaises(ValueError):
            item_invalid = parse(5)

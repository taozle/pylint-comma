# -*- coding: utf-8 -*-
import astroid

from pylint.interfaces import IAstroidChecker
from pylint.checkers import BaseChecker


class TrailingCommaChecker(BaseChecker):
    """Detect trailing comma, prevent typo caused trouble.
    """

    __implements__ = IAstroidChecker

    name = 'custom'
    msgs = {
        'W0001': ('Making a tuple in implicit format',
                  'trailing-comma',
                  'You should always make a tuple like this `(xxx,)` but not `xxx,`')
    }
    options = ()
    # this is important so that your checker is executed before others
    priority = -1

    def visit_assign(self, node):
        if isinstance(node.value, astroid.Tuple):
            self.add_message('W0001', node=node)


def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(TrailingCommaChecker(linter))

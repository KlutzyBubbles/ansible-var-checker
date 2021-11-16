import pytest
import logging
from avc.logger import IndentedLoggerAdapter

def test_adjust():
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    adapter = IndentedLoggerAdapter(logger)
    assert adapter.indent == 0
    adapter.adjust(1)
    assert adapter.indent == 1
    adapter.adjust(0)
    assert adapter.indent == 1
    adapter.adjust(-4)
    assert adapter.indent == 0

def test_add():
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    adapter = IndentedLoggerAdapter(logger)
    assert adapter.indent == 0
    adapter.add(1)
    assert adapter.indent == 1
    adapter.add(0)
    assert adapter.indent == 1
    adapter.add(-4)
    assert adapter.indent == 0

def test_sub():
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    adapter = IndentedLoggerAdapter(logger)
    adapter.add(4)
    assert adapter.indent == 4
    adapter.sub(1)
    assert adapter.indent == 3
    adapter.sub(0)
    assert adapter.indent == 3
    adapter.sub(-4)
    assert adapter.indent == 7
    adapter.sub(8)
    assert adapter.indent == 0

def test_push_pop():
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    adapter = IndentedLoggerAdapter(logger)
    adapter.push().push(1).push(2)
    adapter.pop()
    assert adapter.indent == 2
    adapter.add(1)
    adapter.push().push(4)
    adapter.pop()
    assert adapter.indent == 4
    adapter.pop()
    assert adapter.indent == 3
    adapter.pop()
    assert adapter.indent == 1
    adapter.pop()
    assert adapter.indent == 0
    adapter.pop()
    assert adapter.indent == 0

def test_calc_indent():
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    adapter = IndentedLoggerAdapter(logger)
    assert adapter.calc_indent() == ''
    adapter.add(1)
    assert adapter.calc_indent() == '  '
    adapter.char = '-'
    assert adapter.calc_indent() == '--'
    adapter.sub(4)
    assert adapter.calc_indent() == ''
    adapter.num_per_indent = 1
    adapter.add(1)
    assert adapter.calc_indent() == '-'
    adapter.num_per_indent = 3
    adapter.add(1)
    assert adapter.calc_indent() == '------'

def test_process():
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    adapter = IndentedLoggerAdapter(logger)
    assert adapter.process('test', {}) == ('test', {})
    adapter.add(1)
    assert adapter.process('test', {}) == ('  test', {})
    adapter.char = '-'
    assert adapter.process('test', {}) == ('--test', {})
    adapter.sub(4)
    assert adapter.process('test', {}) == ('test', {})
    adapter.num_per_indent = 1
    adapter.add(1)
    assert adapter.process('test', {}) == ('-test', {})
    adapter.num_per_indent = 3
    adapter.add(1)
    assert adapter.process('test', {}) == ('------test', {})

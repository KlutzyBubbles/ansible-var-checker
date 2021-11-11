#!/usr/bin/env python
import re

from setuptools import setup, find_packages

__version__ = ''
with open('avc/__init__.py', 'r') as fd:
    reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
    for line in fd:
        m = reg.match(line)
        if m:
            __version__ = m.group(1)
            break

if not __version__:
    raise RuntimeError('Cannot find version information')

setup(
    name='ansible-var-checker',
    version=__version__,
    description='Variable checker for ansible playbooks',
    long_description=open('README.md').read(),
    author='KlutzyBubbles',
    author_email='LTzilantois@gmail.com',
    url='https://ansible_var_checker.readthedocs.io',
    packages=find_packages(exclude=['tests', 'test_ansible_project']),
    install_requires=['Jinja2>=2.2'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    entry_points={
        'console_scripts': ['avc = avc:main']
    }
)

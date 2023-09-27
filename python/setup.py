from setuptools import setup, find_packages

setup(
    name='gitWiz',
    version='0.1',
    packages=['wizard'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'squash = wizard.wand:main',
        ],
    },
)
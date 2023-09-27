from setuptools import setup

setup(
    name='gitWiz',
    version='0.1',
    packages=['wizard'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'gwiz = wizard.wand:main',
        ],
    },
    author='Dompeh Kofi Bright',
    author_email='kekelidompeh@gmail.com',
    description='An automation script to ease version control with a lot of files',
    license='MIT',
    url='https://github.com/db-keli/gitWiz',
)

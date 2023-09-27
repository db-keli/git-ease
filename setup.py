from setuptools import setup, find_packages

setup(
    name='gitWiz',
    version='0.1',
    packages=['wizard'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'wiz = wizard.wand:main',
        ],
    },
    author='Dompeh Kofi Bright',
    author_email='kekelidompeh@gmail.com',
    description='A brief description of your project',
    license='Your License (e.g., MIT)',
    url='https://github.com/db-keli/gitWiz',
)
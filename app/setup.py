from setuptools import setup

setup(
    name='buckets',
    version='0.1.0',
    py_modules=['buckets'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'buckets = buckets:buckets',
        ],
    },
)
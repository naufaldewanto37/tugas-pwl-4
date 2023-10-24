from setuptools import setup, find_packages

setup(
    name='tugaspwl4',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyramid',
        # Tambahkan dependencies lainnya di sini
    ],
    entry_points={
    'paste.app_factory': [
        'main = tugaspwl4:main'
        ],
    },
)

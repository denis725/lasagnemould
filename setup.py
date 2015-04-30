from setuptools import setup, find_packages


setup(
    name='lasagnemould',
    version='0.1',
    description='Wrapper for Lasagne',
    author='Benjamin Bossan',
    install_requires=['Lasagne', 'nolearn>=0.5'],
    packages=find_packages(),
)

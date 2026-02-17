from setuptools import setup, find_packages

def get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
        if "-e ." in requirements:
            requirements.remove("-e .")
        return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Anshul',
    author_email='anshulsingh250406@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)

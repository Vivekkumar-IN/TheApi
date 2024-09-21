from setuptools import find_packages, setup


def read_requirements():
    try:
        with open("requirements.txt") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


setup(
    name="TheApi",
    version="0.1",
    packages=find_packages(),
    install_requires=read_requirements(),
)

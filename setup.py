from setuptools import setup, find_packages


def read_requirements():
    try:
        with open("requirements.txt") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


setup(
    name="TheApi",
    version="1.2",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=read_requirements(),
)

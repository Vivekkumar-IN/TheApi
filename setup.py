from setuptools import setup, find_packages


def read_requirements():
    try:
        with open("requirements.txt") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def version():
    version_file = "src/TheApi/__init__.py"
    with open(version_file, "r") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"')
    raise ValueError("Version not found in src/TheApi/__init__.py")


setup(
    name="TheApix",
    version=version(),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=read_requirements(),
    author="VivekKumar",
    description="TheApix is a Python library for asynchronous interactions with various public APIs, enabling diverse functionalities and data retrieval.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Vivekkumar-IN/TheApi",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    project_urls={
        "Issue Tracker": "https://github.com/Vivekkumar-IN/TheApi/issues",
        "Community": "https://t.me/TheTeamVivek",
        "Source": "https://github.com/Vivekkumar-IN/TheApi",
    },
    python_requires=">=3.9",
)

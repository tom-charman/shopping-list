import os

from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    LICENSE = f.read()

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

with open("requirements-dev.txt") as f:
    tests_require = [
        line for line in f.read().splitlines() if line != "-r requirements.txt"
    ]


def get_version() -> str:
    return os.environ.get("APP_VERSION", "0.1.dev0")


setup(
    name="shopping-list",
    version=get_version(),
    long_description=readme,
    author="Thomas Charman",
    author_email="thomas.charman@physics.org",
    license=LICENSE,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "data": ["*.json"],
    },
    install_requires=install_requires,
    tests_require=tests_require,
    dependency_links=[],
    zip_safe=True,
    keywords="",
    python_requires=">=3.7",
)

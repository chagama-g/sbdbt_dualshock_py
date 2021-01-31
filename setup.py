from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="sbdbt_dualshock_py",
    version="0.0.0",
    licence="licence",
    description="description of package",
    author="chagama",

    packages=find_packages(where="src"),
    package_dir={'': 'src'},
)

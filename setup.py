from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="sbdbt_dualshock_py",
    version="0.0.0",
    licence="licence",
    description="Obtain data from Dualshock via SBDBT.",
    author="chagama-g",

    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=_requires_from_file('requirements.txt'),
)

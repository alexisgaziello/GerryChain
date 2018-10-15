from setuptools import find_packages, setup

import versioneer

requirements = [
    # package requirements go here
    "pandas",
    "networkx",
    "geopandas",
    "pysal",
]

setup(
    name="GerryChain",
    description="Short description",
    author="Metric Geometry and Gerrymandering Group",
    author_email="gerrymandr@gmail.com",
    url="https://github.com/mggg/GerryChain",
    packages=find_packages(exclude=("tests",)),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    entry_points={"console_scripts": ["gerrychain=gerrychain.__main__:main"]},
    install_requires=requirements,
    keywords="GerryChain",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
    ],
)

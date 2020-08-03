from setuptools import setup, find_packages

from dryml.version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dryml",
    version=__version__,
    author="Valentin Grigoryevskiy",
    author_email="v.grigoryevskiy@gmail.com",
    license="MIT",
    description="Converts a DRYML Document to the JSON Document.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dryml/dryml",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 2 - Pre-Alfa",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.6",
    keywords="modeling modelling modelling-tool uml uml-diagram uml-diagrams uml-class-diagram uml-state-machine uml-sequence-diagram uml-model plantuml software-architecture software-design diagram-generator dryml use-case-diagram activity-diagram activity-diagrams business-analysis software-architecture-and-design",
    project_urls={
        "Source": "https://github.com/dryml/dryml",
        "Tracker": "https://github.com/dryml/dryml/issues",
    },
)

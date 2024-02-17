from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="keycove",
    version="0.3.1",
    description="An API key authorization library",
    packages=find_packages(),
    install_requires=[
        "cryptography>=42.0.3",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaz-alli/keycove",
    author="Jaz Allibhai",
    author_email="jaz.allibhai@gmail.com",
    license="MIT",
)

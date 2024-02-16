from setuptools import setup, find_packages

setup(
    name="keycove",
    version="0.3.0",
    description="An API key authorization library",
    packages=find_packages(),
    install_requires=[
        "cryptography>=42.0.3",
    ],
)

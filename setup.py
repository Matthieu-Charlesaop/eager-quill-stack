from setuptools import setup, find_packages

setup(
    name="eager-quill-stack",
    version="1.4.2",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.1.0",
        "numpy>=1.26.0",
        "matplotlib>=3.8.0",
    ],
)

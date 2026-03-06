from setuptools import setup, find_packages

setup(
    name="automation",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "python-dotenv",
    ],
)

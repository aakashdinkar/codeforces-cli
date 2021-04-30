import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="saral-square",
    version="1.0.0",
    description="Command line interface for Codeforces",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/uditvashisht/saral-square",
    author="Udit Vashisht",
    author_email="admin@saralgyaan.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["codeforces"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "codeforeces=codeforeces.__main__:codeforces",
        ]
    },
)
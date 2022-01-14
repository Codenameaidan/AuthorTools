import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name='authortools',
    version="0.0.2",
    description="A collection of useful functions for writers to analyze text/stories.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Codenameaidan/AuthorTools",
    author="Codenameaidan",
    author_email="codenameaidan@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['authortools'],
    include_package_data=True,
    py_modules=['writing_analysis']
    
    
)

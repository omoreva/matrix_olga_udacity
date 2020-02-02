# TODO: Fill out this file with information about your package

# HINT: Go back to the object-oriented programming lesson "Putting Code on PyPi" and "Exercise: Upload to PyPi"

# HINT: Here is an example of a setup.py file
# https://packaging.python.org/tutorials/packaging-projects/

import setuptools

with open("matrix_olga_udacity/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matrix_olga_udacity", 
    version="0.0.1",
    author="Olga Moreva",
    description="The first assignment for machine learning engineer nanodegree udacity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omoreva/matrix_olga_udacity",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
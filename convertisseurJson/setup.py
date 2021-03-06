import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yamltojsoncreator",
    version="0.0.1",
    author="Eric",
    author_email="travers.eric@gmail.com",
    description="Yaml convertisseur for files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoHn3r/python-py/tree/master/convertisseurJson",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

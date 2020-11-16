import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bibtex2rfc",
    version="2.0.0",
    author="Yaron Sheffer",
    author_email="yaronf.ietf@gmail.com",
    description="Convert BibTeX references to the xml2rfc format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaronf/bibtex2rfc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    install_requires=['bibtexparser'],
    python_requires='>=3.6',
    scripts=['bin/bibtex2rfc'],
)

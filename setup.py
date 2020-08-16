import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-yugioh",
    version="0.0.1",
    author="James Rocker",
    author_email="jamesrocker@hotmail.co.uk",
    description="A package dedicated to being a helper for yuigioh players",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheRockerfly/py-yugioh",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="growx-core-groworx",
    version="0.0.1",
    author="Jerric Calosor",
    author_email="jerric.calosor@groworx.com.au",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/groworxph/gwx-core",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.7'
)

import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data_analysis",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example data analysis package",
    install_requires=("numpy", "requests"),
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/opengeophysics/2018-agu-oss-example-repo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

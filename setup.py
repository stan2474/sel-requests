import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sel-requests",
    #version="0.0.1",
    author="h0nda",
    author_email="1@1.com",
    description="Send requests using selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h0nde/sel-requests",
    packages=setuptools.find_packages(),
    classifiers=[
    ],
    install_requires=[
        "requests",
        "selenium"
    ],
    include_package_data=True,
    python_requires='>=3.6',
)

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='amongus_codec',
    version='1',
    author="Omicron166",
    author_email="omicron166@protonmail.com",
    description="An amongus code encryption / decryption library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Omicron166/amongus-codec",
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

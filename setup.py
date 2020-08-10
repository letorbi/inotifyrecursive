import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="inotifyrecursive",
    version="0.3.3",
    author="Torben Haase",
    author_email="git@letorbi.com",
    description="Recursive inotify watches based on inotify_simple.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/letorbi/inotifyrecursive",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    install_requires=["inotify-simple>=1.3.5"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*"
)

import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

if sys.version_info.major < 3:
    install_requires = ["enum", "inotify_simple"]
else:
    install_requires = ["inotify_simple"]

setuptools.setup(
    name="inotifyrecursive",
    version="0.2.2",
    author="Torben Haase",
    author_email="torben@pixelsvsbytes.com",
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
    install_requires=install_requires,
)

# Inotify Recursive - Recursive inotify watches for Python

Inotify Recursive is a Python package that offers a simple way to watch a directory-tree recursively for file changes
via the inotify functionality of the Linux kernel. It uses [the inotify_simple package](https://github.com/chrisjbillington/inotify_simple)
to set and remove the inotify watches and also incorporates its whole functionality. The package is written in
Python and licensed as open-source under the GPL version 3.

At the moment the main purpose of Inotify Recursive is to provide the file watching functionality for [Synoindex Watcher](https://github.com/letorbi/synoindexwatcher), a small tool that automatically updates the media index of Synology DiskStations.

*This Python package is still an alpha! Its core functionality has been tested and is working, but there could still be undiscovered bugs. Also breaking interface changes are likely to happen, so it is not recommended to use it in
production projects, yet.*

## Features

* **Small** About 150 lines of code (including comments)
* **Powerfull** All features of inotify-simple plus recursive watching
* **Agnostic** Python 2 and Python 3 compatible (minimum tested version is 2.7)

## Installation

The recommended installation method is via pip:

`pip install inotifyrecursive`

You could also simply clone the repository or copy the code directly into your project, but don't forget to install the
dependency [inotify-simple](https://pypi.org/project/inotify_simple/), if you choose this way.

## Documentation

Please [read the docs for inotify_simple](http://inotify_simple.readthedocs.org) first, since the basic usage is the
same.

The `INotify` class of Inotify Recursive provides three additional methods, which are useful, if a directory shall be
watched recursively:

#### `inotify.add_watch_recursive(path, mask, filter = None)`

  * **path** The path to watch
  * **mask** The mask of events to watch for
  * **filter** A function to ignore certain sub-directories

Returns the descriptor for the newly created watch of the directory where the given path points to. Unlike `add_watch()`
this function also creates watches for all sub-directories below it. The descriptors of the sub-watches are not
returned.

The filter function is optional. It takes the name of the file or directory and the descriptor of the watcher of the parent directory. The filter returns a boolean value, which describes whether the directory shall be watched (`True`) or ignored (`False`). If no filter is set, all files and sub-directories will be watched.

####  `inotify.rm_watch_recursive(wd)`

  * **wd** The watch descriptor to remove

Removes the watch with the given descriptor and all associated sub-watches. Should be used for any watch that has been
created by `add_watch_recursive()`.

####  `inotify.get_path(wd)`

  * **wd** The watch descriptor the path is fetched for

Returns the absolute path of the directory associated to the watch with given descriptor.

----

Copyright 2019 Torben Haase \<[https://pixelsvsbytes.com](https://pixelsvsbytes.com)>

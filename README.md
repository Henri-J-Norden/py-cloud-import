Import Python modules straight from the cloud (e.g. GitHub) at runtime!

## Installation
* pip: `pip install cloud_import`
* no pip: copy [cloud_import.py](cloud_import/could_import.py) into your project

## Usage
See [examples/example1.py](examples/example1.py)

## Why?
This can be used to entirely skip the "deployment" step for internal tooling, that's not meant for distribution or public usage.

Originally by [James Murphy](https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/133_cloud_imports/cloud_imports.py) - check out his video "[You won't believe it! Import from the Cloud](https://www.youtube.com/watch?v=2f7YKoOU6_g)"  

## Limitations
* No dependency handling
* Fixed URL structure: the source code for module `foo.bar` must be accessible at `<url>/foo/bar/*.py`
* Bad things will happen if the cloud source code changes while a package (with multiple modules) is being imported 

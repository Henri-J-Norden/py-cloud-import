from distutils.core import setup

setup(
    name='cloud_import',
    packages=['cloud_import'],
    version='0.4',
    license='MIT',
    description='Import Python modules straight from the cloud (e.g. GitHub) at runtime!',
    author='Henri J. Norden (originally by James Murphy)',
    #author_email='your.email@domain.com',
    url='https://github.com/Henri-J-Norden/py-cloud-import',
    download_url='https://github.com/Henri-J-Norden/py-cloud-import.git',
    keywords=['CLOUD', 'IMPORT', 'ARBITRARY CODE EXECUTION'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.4',
        #'Programming Language :: Python :: 3.5',
        #'Programming Language :: Python :: 3.6',
    ],
    long_description_content_type='text/markdown',
    long_description="""
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

    """,
)

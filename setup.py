from distutils.core import setup

setup(
    name='cloud_import',
    packages=['cloud_import'],
    version='0.1',
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
)

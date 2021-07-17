from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Netman, a network status checker'
LONG_DESCRIPTION = 'Netman verifies the status of your internet connection and of the sites you wish'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="netman", 
        version=VERSION,
        author="Diogo Lopes",
        author_email="diogolopes18@ieee.org",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        license = "MIT",
        install_requires=['speedtest-cli', 'numpy', 'pandas'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'network', 'ping', 'socket'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: Linux :: Ubuntu",
            "Operating System :: Microsoft :: Windows",
            "Topic :: Networking"
        ],

        python_requires = '>3'
)
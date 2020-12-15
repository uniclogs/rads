import setuptools
import rads

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name=rads.APP_NAME,
    version=rads.APP_VERSION,
    author=rads.APP_AUTHOR,
    license=rads.APP_LICENSE,
    description=rads.APP_DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=rads.APP_URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Environment :: Console :: Curses",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking :: Monitoring :: Hardware Watchdog"
    ],
    install_requires=[
        "loguru",
        "sqlalchemy",
        "reverse_geocoder",
        "pass-calculator",
        "ballcosmos",
    ],
    extras_require={
        "dev": [
            "setuptools",
            "wheel",
            "pytest",
            "flake8",
            "twine",
            "sphinx",
            "sphinx_rtd_theme",
        ]
    },
    python_requires='>=3.8.5',
    entry_points={
        "console_scripts": [
            "rads = rads.ui.main_menu:main"
        ]
    }
)

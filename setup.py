import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="edlstrip",
    version="1.0.6",
    author="Scott C.",
    author_email="shuaiscott@gmail.com",
    description="Strips commercials off Channels DVR recordings using outputted EDL files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tresby/edlstrip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    entry_points = {
        'console_scripts': ['edlstrip=edlstrip:main'],
    }
)
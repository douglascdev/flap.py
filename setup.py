import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flappy",
    version="0.0.1",
    author="Douglas Carvalho",
    author_email="douglasc.dev@gmail.com",
    description="A not very well done flappy bird clone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/douglas-cpp/flap.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        'assets': ['*']
    },
    install_requires=['pygame'],
    python_requires='>=3.6',
)

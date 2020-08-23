import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="flappy",
    version="0.0.1",
    author="Douglas Carvalho",
    author_email="douglasc.dev@gmail.com",
    description="A not very well coded flappy bird clone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/douglas-cpp/flap.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.7',
)

from setuptools import find_packages, setup


with open('README.md') as f:
    long_description = f.read()


setup(
    name="nestedaccess",
    packages=find_packages(),
    version="0.1.1",
    description="Get nested data of dictionary or list.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Potato-OvO",
    author_email="wkl1224141267@gmail.com",
    license="MIT",
    url="https://github.com/Potato-OvO/nestedaccess",
    python_requires=">=3.6"
)

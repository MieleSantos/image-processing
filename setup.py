from setuptools import setup, find_packages


with open("README.md", "r") as f:
    page_descritption = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setup(
    name="package_name",
    version="0.0.1",
    author="my_email",
    description="My short description",
    long_description=page_descritption,
    long_description_content_type="text/markdown",
    url="mygithub",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.6"
)

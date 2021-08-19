from setuptools import setup, find_packages


with open("README.md", "r") as f:
    page_descritption = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-diolab-test",
    version="0.0.1",
    author="mielesnts@gmail.com",
    description="Projeto da DigitalInnovationOne",
    long_description=page_descritption,
    long_description_content_type="text/markdown",
    url="https://github.com/MieleSantos/image-processing-dio-lab",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8"
)

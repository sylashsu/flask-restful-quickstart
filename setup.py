from setuptools import find_packages
from setuptools import setup

setup(
    name="flask-restful-quickstart",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask", "flask_restful"],
)

"""Setup for the code kata collection."""

from setuptools import setup


setup(
    name="code-katas",
    description="A work through of Python Katas",
    version=0.1,
    author="Claire Gatenby",
    author_email="clairejgatenby@gmail.com",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=[""],
    extras_require={
        "test": ["pytest", "pytest-watch", "pytest-cov", "tox"]
    },
)

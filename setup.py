from setuptools import setup, find_packages
from Cython.Build import cythonize
import glob

setup(
    name="n4tazac",
    version="0.1.7",

    package_dir={"": "src"},
    packages=find_packages(where="src"),

    ext_modules=cythonize(
        glob.glob("src/n4tazac/*.py"),
        compiler_directives={
            "language_level": "3"
        }
    ),

    zip_safe=False,
)

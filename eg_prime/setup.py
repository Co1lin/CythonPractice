from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(
        [
            'primes_cython.pyx',
            'primes_python_compiled.py',
            'primes_vec.pyx',
        ],
        annotate=True,
    ),
)
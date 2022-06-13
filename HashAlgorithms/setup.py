from setuptools import find_packages, setup

setup(
    name='hash_lib',
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.*",
    version='0.0.1',
    description='Python library for implementing hash algorithms such as Keccak and SHA1',
    author='InterNosTC',
    license='MIT',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)

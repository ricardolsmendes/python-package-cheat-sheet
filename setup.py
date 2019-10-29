from setuptools import find_packages, setup

setup(
    name='python-package-cheat-sheet',
    version='1.0.0',
    author='Your Name',
    author_email='you@yourdomain.com',
    description='Python package developer\'s cheat sheet',
    platforms='Posix; MacOS X; Windows',
    packages=find_packages(where='./src'),
    package_dir={
        '': 'src'
    },
    include_package_data=True,
    install_requires=(
        'stringcase',
    ),
    setup_requires=(
        'pytest-runner',
    ),
    tests_require=(
        'pytest-cov',
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

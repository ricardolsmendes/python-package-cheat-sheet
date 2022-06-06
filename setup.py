import setuptools

setuptools.setup(
    name='python-package-cheat-sheet',
    version='1.0.0',
    author='Your Name',
    author_email='you@yourdomain.com',
    description='Python package developer\'s cheat sheet',
    platforms='Posix; MacOS X; Windows',
    packages=setuptools.find_packages(where='./src'),
    package_dir={
        '': 'src'
    },
    include_package_data=True,
    install_requires=(
        'stringcase ~=1.2.0',
    ),
    setup_requires=(
        'pytest-runner ~=5.3.2',
    ),
    tests_require=(
        'coverage ==6.2',
        'pytest ~=7.0.1',
        'pytest-cov ~=2.12.1',
        'typing-extensions ==4.1.1',
        'tomli ~=1.2.3',
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

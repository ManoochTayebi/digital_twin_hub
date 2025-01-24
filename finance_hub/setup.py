from setuptools import setup, find_packages

setup(
    name='financial_twin',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for financial data processing and trading workflows',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
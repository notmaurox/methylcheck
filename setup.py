# Lib
from setuptools import setup, find_packages

setup(
    name='methQC',
    version='0.2.3',
    description="""Quality Control (QC), Visualization/plotting, and postprocessing software for Illumina methylation array data.
See https://life-epigenetics-methqc.readthedocs-hosted.com/en/latest/ for full documentation and examples.""",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Framework :: Jupyter',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
      ],
    keywords='methylation dna data processing epigenetics illumina',
    url='https://github.com/LifeEGX/methQC',
    license='MIT',
    author='Life Epigenetics',
    author_email='info@lifeegx.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'seaborn',
        'matplotlib',
        'tqdm',
        'scikit-learn',
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-pep8',
            'pytest-cov',
            'flake8',
            'pytest',
            'coverage',
            'coveralls-python',
            'sphinxcontrib-apidoc',
            'm2r',
            'nbsphinx',
            'sphinx',
            'ipykernel'
        ]
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'methQC-cli = methQC.cli:cli_parser',
            ],
    }
)
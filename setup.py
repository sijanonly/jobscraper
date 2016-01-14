from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='jobscraper',
    version='0.2',
    description='Grab all the matching jobs from job portals',
    long_description=readme(),
    url='https://github.com/sijanonly/jobscraper',
    download_url='https://github.com/sijanonly/jobscraper/tarball/0.2',
    author='Sijan Bhandari',
    author_email='sijanonly@gmail.com',
    license='MIT',
    packages=['jobscraper'],
    keywords=['jobs', 'freelance'],
    install_requires=[
        'xmltodict==0.9.2',
        'requests==2.9.1'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)

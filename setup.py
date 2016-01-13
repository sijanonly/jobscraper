from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='jobscraper',
    version='0.1',
    description='Grab all the matching jobs from job portals',
    long_description=readme(),
    url='https://github.com/sijanonly/jobscraper',
    author='Sijan Bhandari',
    author_email='sijanonly@gmail.com',
    license='MIT',
    packages=['jobscraper'],
    keywords=['jobs', 'freelance'],
    install_requires=[
        'beautifulsoup4==4.4.1',
        'requests==2.9.1'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Jobs :: Freelancing',
    ],
    zip_safe=False
)

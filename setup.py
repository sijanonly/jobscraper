from setuptools import setup

setup(
    name='jobscraper',
    version='0.1',
    description='Grab all the matching jobs from job portals',
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

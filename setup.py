from setuptools import setup, find_packages


setup(
    name='flask-bootstrap',
    version='0.1.0',
    url='https://github.com/kevinxuv/flask-bootstrap',
    description='bootstrap flask project',
    author='kevin.xu.v',
    license='BSD',
    packages=find_packages(exclude=('tests', 'tests.*')),
    package_data={'flask_bootstrap': ['templates/*']},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['flask-boot = flask_bootstrap.cli:cli']
    },
    classifiers=[
        'Framework :: flask',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    install_requires=[
        'click',
        'jinja2',
        'gitpython',
        'virtualenv'
    ],
)

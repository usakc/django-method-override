from setuptools import find_packages, setup

from method_override import __version__


setup(
    name='django-method-override',
    version=__version__,
    description='Django Middleware for HTTP Method Override Form Params & Header',
    author='LocalMed',
    author_email='pete.browne@localmed.com',
    url='https://bitbucket.org/localmed/django-method-override',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
    ],
)

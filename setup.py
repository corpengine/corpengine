from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='corpengine2',
    version='2.0',
    description='Fast, Organized, Object-Oriented Python Game Development',
    long_description='github repository: https://github.com/corpengine/corpengine',
    url='https://corpengine.github.io/',
    author='CORPEngine Organization + Contributors',
    license='MIT',
    classifiers=classifiers,
    keywords='corpengine',
    install_requires=['easygui', 'raylib']
)

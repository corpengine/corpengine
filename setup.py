from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

changelog = 'v1.2\n\n*Some object & service naming fixes\n*Added back the version module\n*new colors methods: all, onlyFill, onlyEmpty\n*Fixed color range checking in colors.mix()\n*Optional Rectangle support for isCollidingWithMouse()\n*'

setup(
    name='corpengine1',
    version='1.2',
    description='Fast, Organized, Object-Oriented Python Game Development',
    long_description='github repository: https://github.com/corpengine/corpengine' + '\n\nChangelog:\n'+changelog,
    url='https://corpengine.github.io/',
    author='CORPEngine Organization + Contributors',
    license='MIT',
    classifiers=classifiers,
    keywords='corpengine',
    packages=find_packages(),
    install_requires=['easygui', 'pygame']
)
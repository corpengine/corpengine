from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

changelog = 'v1.3.dev1\n\n- '

setup(
    name='corpengine1',
    version='1.3.dev1',
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
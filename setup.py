from setuptools import setup, find_packages

setup(
    name='injectinput',
    version='0.0.0',
    url='https://github.com/meeuw/injectinput.git',
    author='Dick Marinus',
    author_email='dick@mrns.nl',
    description='Inject input',
    packages=find_packages(),    
    install_requires=['evdev'],
    entry_points={
        'console_scripts': ['injectinput = injectinput.injectinput:main'],
    },
)

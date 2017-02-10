from setuptools import setup, find_packages

setup(
    name='benzaiten',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'regex'
    ],
    entry_points='''
        [console_scripts]
        bsum=benzaiten.benzaiten:bensum
    '''
)
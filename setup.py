import setuptools

setuptools.setup(
    include_package_data=True,
    name='comutils',
    version='0.0.1',
    description='Package for common python utilities.',
    url='git@github.com:BennyC31/com_utils.git',
    author='Benjamin Calderaio, Jr.',
    author_email='bencalderaio@gmail.com',
    packages=setuptools.find_packages(exclude=['tests']),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
)
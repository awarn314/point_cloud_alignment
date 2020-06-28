from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='pycpd',
      version='2.0.0',
      description='Pure Numpy Implementation of the Coherent Point Drift Algorithm',
      long_description=readme(),
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering',
      ],
      keywords='image processing, point cloud, registration, mesh, surface',
      author='Alex Warning',
      author_email='alex.d.warning@gmail.com',
      license='MIT',
      install_requires=['numpy', 'future'],
      zip_safe=False)

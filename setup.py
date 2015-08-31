from setuptools import setup

setup(
    name='IVisual-alt',
    version='0.2.01',
    author='John Coady <johncoady@shaw.ca>, Nathan Whitehead <nwhitehe@gmail.com>',
    author_email='johncoady@shaw.ca, nwhitehe@gmail.com',
    packages=['ivisual'],
    package_data={'ivisual': ['data/*.js']},
    url='https://github.com/nwhitehead/IVisual',
    license='Unknown',
    description='VPython visual inline for IPython Notebook',
    long_description=open('README.md').read(),
    keywords=['VPython', 'IPython', 'IVisual', 'jupyter', 'notebook',
              'Graphics', '3D', 'visualization', 'rendering', 'animation'],
    classifiers=[
          'Framework :: IPython',
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Natural Language :: English',
          'Programming Language :: Python :: 2.7',
          'Topic :: Multimedia :: Graphics :: 3D Modeling',
          'Topic :: Multimedia :: Graphics :: 3D Rendering',
          'Topic :: Scientific/Engineering :: Visualization',
    ],
    install_requires=[
        'ipykernel',
    ],
    zip_safe=False,
)

from distutils.core import setup

setup(name='dnet',
      version='0.1.0',
      description='Distribution Network Evaluation Tool',
      author='Takeru Inoue',
      author_email='takeru.inoue@gmail.com',
      url='http://www-erato.ist.hokudai.ac.jp/?language=en',
      license='MIT License',
      packages=['dnet'],
      scripts=['script/dnet-converter', 'script/dnet-enumerator', 'script/dnet-optimizer'],
      requires=['networkx', 'yaml'],

#      py_modules=['foo'],
#      package_dir={'mypkg': 'src/mypkg'},
#      package_data={'mypkg': ['data/*.dat']},
#      data_files=[('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),
#                  ('config', ['cfg/data.cfg']),
#                  ('/etc/init.d', ['init-script'])]
#      classifiers=[
#          'Development Status :: 4 - Beta',
#          'Environment :: Console',
#          'Environment :: Web Environment',
#          'Intended Audience :: End Users/Desktop',
#          'Intended Audience :: Developers',
#          'Intended Audience :: System Administrators',
#          'License :: OSI Approved :: Python Software Foundation License',
#          'Operating System :: MacOS :: MacOS X',
#          'Operating System :: Microsoft :: Windows',
#          'Operating System :: POSIX',
#          'Programming Language :: Python',
#          'Topic :: Communications :: Email',
#          'Topic :: Office/Business',
#          'Topic :: Software Development :: Bug Tracking',
#          ],
      )

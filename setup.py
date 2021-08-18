from distutils.core import setup
setup(
  name = 'HBTile',         
  packages = ['hbtile'],   
  version = '1.0.0',      
  license='MIT',        
  description = 'A library for simulating tile based games with separate attacking and directional movement',   
  author = 'Nicholas Gray',
  author_email = 'nicholascgray@knights.ucf.edu', 
  url = 'https://github.com/NicholasCG/HBTile',
  download_url = 'https://github.com/NicholasCG/HBTile/archive/1.0.0.tar.gz',
  keywords = ['python', 'hexagon', 'game', 'hbtile', 'hexy'],
  install_requires=[            
          'hexy',
          'pickle',
          'numpy',
          'yaml'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Moduless',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
)
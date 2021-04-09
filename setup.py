from distutils.core import setup
setup(
  name = 'koronavirus',
  packages = ['koronavirus'],
  version = '0.1',
  license='MIT',
  description = 'Koronavirüs (Covid-19) verilerine erişmenizi sağlayan bir Python modülü.',
  author = 'Dorukyum',
  author_email = 'no.email@not.now.com',
  url = 'https://github.com/user/reponame',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['API', 'TÜRKÇE', 'COVID', 'KORONA'],
  install_requires=["requests", "aiohttp"]
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
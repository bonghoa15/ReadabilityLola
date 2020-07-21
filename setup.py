from distutils.core import setup
setup(
  name = 'readability',         # How you named your package folder (MyLib)
  packages = ['readability'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'readability score of local languages',   # Give a short description about your library
  author = 'bonghoa',                   # Type in your name
  author_email = 'nguyendieuhoa15@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/bonghoa15',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/bonghoa15/readability/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['READABILITY', 'LANGUAGES', 'HINDI','BAHASA'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Data Science',      # Define that your audience are developers
    'Topic :: Data Science :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7'    #Specify which pyhton versions that you want to support
  ],
)
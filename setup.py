import setuptools

setuptools.setup(name="elorating",
      version="0.2",
      description="A Python module for scoring a set of elements using Elo Rating System",
      author="Luxin Tian",
      author_email="luxintian@uchicago.edu",
#      url="https://luxintian.com",
      classifiers=["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                  ],
      packages=setuptools.find_packages(), 
      python_requires='>=3.6'
#      scripts=['scripts/baidu_map, scripts/pp2']
      )
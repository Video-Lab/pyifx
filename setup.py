import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name='pyifx',
  version='0.3.0',
  description="An image handling, processing, & editing library for Python.",
  long_description=long_description,
  author='Jad Khalili',
  author_email='jad.khalili123@gmail.com',
  packages=setuptools.find_packages(),
  long_description_content_type="text/markdown",
  url="https://github.com/Video-Lab/pyifx/",
  zip_safe=False,
  install_requires=[
      'numpy',
      'imageio'
      ],
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='jinja_gcs_loader',  
     version='0.0.16',
     author="Pedro Pinho",
     author_email="ptfpinho@hotmail.com",
     install_requires=['google-cloud','Jinja2','google'],
     description="Simple Jinja2 GCS Template Loader",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/ptfpinho23/jinja2-gcs-loader",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
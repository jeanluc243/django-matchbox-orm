import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "django-matchbox-orm",
    version = "0.1",
    scripts = ['django-matchbox-orm'],
    author = "Jean-Luc Kabulu",
    author_email = "jeanluc.kabulu@gmail.com",
    description = "django-matchbox-orm is orm package for Google Cloud firestore with Django",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/jeanluc243/django-matchbox-orm",
    zip_safe=False,
    keywords='firebase orm firestore django',
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    install_requires = ['matchbox-orm>=0.2'],
)
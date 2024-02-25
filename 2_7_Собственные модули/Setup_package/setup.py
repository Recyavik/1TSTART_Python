from setuptools import setup, find_packages

setup(
    name="Viktor_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Здесь перечислите зависимости вашего пакета, например:
        # "requests", "numpy"
    ],
    author="Your Name",
    author_email="you@example.com",
    description="My cool Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)

# python setup.py sdist
# pip install twine
# pip install auto-py-to-exe
# auto-py-to-exe

from setuptools import setup, find_packages


setup(
    name="vadvergasov_serialization",
    version="1.0.0",
    description="Serialization library",
    url="https://github.com/VadVergasov/SCCS",
    author="VadVergasov",
    author_email="vadim.vergasov2003@gmail.com",
    license="GNU GPLv3",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU GPLv3",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
)

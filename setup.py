from setuptools import setup, find_packages
setup(
    name="costo-economico-salud-mental-global-latam-2020-2024",
    version="1.0.0",
    description="Costo económico de los trastornos mentales: datos globales y América Latina 2020-2024. Pérdida PIB, ",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/costo-economico-salud-mental-global-latam-2020-2024",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="america-latina, avad, dataset, economia, open-data, pib, productividad, salud-mental, zenodo, open-data",
)
from setuptools import find_packages, setup
setup(
    name='ELF_Winddows',
    packages=find_packages(include=['ELF_Windows']),
    version='0.1.0',
    description='This library is made for developing malware in Python',
    author='ELF',
    license='MIT',
    install_requires=[],
    setup_requires=['pywin32' ,'_winreg'],
)

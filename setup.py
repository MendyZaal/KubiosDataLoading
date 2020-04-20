from distutils.core import setup

setup(
    name='KubiosDataLoader',
    packages=['KubiosDataLoader'],
    version='0.1',
    license='gpl-3.0',
    description='Importing text files from Kubios ECG data analysis',
    author='Mendy Zaal',
    author_email='mendyzaal@hotmail.com',
    url='https://github.com/MendyZaal/KubiosDataLoading',
    download_url='',  # I explain this later on
    keywords=['Kubios', 'dataloader', 'data-analysis'],
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

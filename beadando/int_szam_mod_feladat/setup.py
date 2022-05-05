from glob import glob
import os

from setuptools import setup

package_name = 'int_szam_mod_feladat'

setup(
    name=package_name,
    version='0.3.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'rviz'),
            glob(os.path.join('rviz', '*.rviz'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Balazs Megyeri',
    author_email='megbalaa@gmail.com',
    maintainer='Balazs Megyeri',
    maintainer_email='megbalaa@gmail.com',
    description=(
        'int_szam_mod beadando'
    ),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'static_int_szam_mod_feladat_broadcaster = int_szam_mod_feladat.static_int_szam_mod_feladat_broadcaster:main',
            'int_szam_mod_feladat_broadcaster = int_szam_mod_feladat.int_szam_mod_feladat_broadcaster:main',
            'int_szam_mod_feladat_listener = int_szam_mod_feladat.int_szam_mod_feladat_listener:main',
            'fixed_frame_tf2_broadcaster = int_szam_mod_feladat.fixed_frame_tf2_broadcaster:main',
            'dynamic_frame_tf2_broadcaster = int_szam_mod_feladat.dynamic_frame_tf2_broadcaster:main',
            'int_szam_mod_feladat_message_broadcaster = int_szam_mod_feladat.int_szam_mod_feladat_message_broadcaster:main',
        ],
    },
)

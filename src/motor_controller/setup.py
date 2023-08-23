from setuptools import setup
import os
from glob import glob

package_name = 'motor_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools', 'canopen'],
    zip_safe=True,
    maintainer='Mads Rossen',
    maintainer_email='mrma19@student.aau.dk',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor = motor_controller.motor:main',
            'calibration = motor_controller.calibration:main'
        ],
    },
)

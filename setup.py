from setuptools import setup

package_name = 'lidar_filter'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    # py_modules=[
    #     'lidar_filter.lidar_scan_filter'
    # ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='josue-meran',
    maintainer_email='pavoro30@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'laser_scan_filter = lidar_filter.laser_scan_filter:main',
        ],
    },
)

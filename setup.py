from setuptools import find_packages, setup

package_name = 'obstacle_detector'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pl',
    maintainer_email='pierluigi1009@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'obstacle_detector_node = obstacle_detector.obstacle_detector_node:main',
        'obstacle_clusters_node = obstacle_detector.obstacle_clusters_node:main',
    ],
},

)

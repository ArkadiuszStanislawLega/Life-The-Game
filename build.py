from pybuilder.core import use_plugin, init

use_plugin('python.core')
use_plugin('python.install_dependencies')
use_plugin('python.distutils')
use_plugin("python.unittest")
use_plugin('python.pydev')
use_plugin('python.pycharm')

default_task = ['analyze']

@init
def initialize(project):
    
    #Set source directory
    project.set_property('dir_source_main_python', 'project_name')
    project.set_property('dir_source_unittest_python', 'unittests')
    
    #install dependencies
    project.depends_on_requirements("requirements.txt")
   




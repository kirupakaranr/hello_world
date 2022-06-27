from conans import ConanFile, CMake, tools

import json
import os


class helloworld(ConanFile):


    scm = {
            "type": "git",
            "url": "auto",
            "revisions": "auto"
    }
    name = "helloworld"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared":[True, False]}
    requires = [ ("fmt/6.1.2")]
    generators = "cmake", "cmake_find_package", "cmake_paths", "virtualrunenv"

    default_options = {"shared" : False}


    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()


    def package (self):
        cmake = self._configure_cmake()
        cmake.install()


    def package_info (self):
        pass

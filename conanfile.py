#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Conan recipe package for libstyxe
"""
from conans import ConanFile, CMake, tools


class LibstyxeConan(ConanFile):
    name = "libstyxe"
    license = "Apache-2.0"
    author = "Ivan Ryabov <abbyssoul@gmail.com>"
    url = "https://github.com/abbyssoul/conan-%s.git" % name
    homepage = "https://github.com/abbyssoul/%s" % name
    description = "9P2000 file protocol parser implementation"
    topics = ("9P", "9P2000", "plan9", "styx", "protocol", "parser", "distributed", "distributed-file-system", "9pfs", "Modern C++")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    generators = "cmake"

    version = "0.4"
    requires = "libsolace/0.3.3@abbyssoul/stable"


    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
#        git = tools.Git()
#        git.clone(self.homepage)
        self.run("git clone --branch {} --depth 1 --recurse-submodules {}".format(self.version, self.homepage))

    def build(self):
        cmake = CMake(self, parallel=True)
        cmake.configure(source_folder=self.name)
        cmake.build()
        # cmake.test()
        cmake.install()

    def package(self):
        self.copy("*.hpp", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["styxe"]

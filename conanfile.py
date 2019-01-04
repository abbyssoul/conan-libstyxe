#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Conan recipe package for libsolace
"""
from conans import ConanFile, CMake, tools


class LibstyxeConan(ConanFile):
    name = "libstyxe"
    version = "0.1"
    license = "A"
    license = "Apache-2.0"
    author = "Ivan Ryabov <abbyssoul@gmail.com>"
    url = "https://github.com/abbyssoul/conan-%s" % name
    homepage = "https://github.com/abbyssoul/%s" % name
    description = "9P2000 file protocol implementation"
    topics = ("9P", "9P2000", "Modern C++")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    generators = "cmake"
    # exports_sources = "src/*"

    _src_url = "https://github.com/abbyssoul/%s" % name

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
#        git = tools.Git()
#        git.clone(self._src_url)
        # TODO: Only clone tagged vesion: tags/self.version
        self.run("git clone --depth 1 --recurse-submodules {}".format(self._src_url))

    def build(self):
        cmake = CMake(self, parallel=True)
        cmake.configure(source_folder=self.name)
        cmake.build()
        cmake.test()
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

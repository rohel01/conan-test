from conans import ConanFile, CMake, tools

class Lib2Conan(ConanFile):
    name = "lib2"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    url = "www.melchiore.com"
    licence = "MIT"
    description = "Lol2"
    generators = "cmake"
    requires = ["lib1/0.1@demo/testing"]

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.a", dst="lib")

    def build(self):
        cmake = CMake(self) 
        cmake.configure(defs={
            "CMAKE_VERBOSE_MAKEFILE": True,
            "CPPAST_BUILD_TEST": False,
            "CPPAST_BUILD_EXAMPLE": False,
            "CPPAST_BUILD_TOOL": False
            })
        cmake.build()


    def package_info(self):
        self.cpp_info.libs = tools.collect_libs()
from conans import ConanFile, CMake, tools

class AppConan(ConanFile):
    name = "app"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    url = "www.melchiore.com"
    license = "MIT"
    description = "Lol2"
    generators = "cmake"
    requires = ["lib2/0.1@demo/testing"]

    def build(self):
        cmake = CMake(self) 
        cmake.configure(defs={
            "CMAKE_VERBOSE_MAKEFILE": True,
            "CPPAST_BUILD_TEST": False,
            "CPPAST_BUILD_EXAMPLE": False,
            "CPPAST_BUILD_TOOL": False
            })
        cmake.build()
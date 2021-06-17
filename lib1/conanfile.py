from conans import ConanFile

class Lib1Conan(ConanFile):
    name = "lib1"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    url = "www.melchiore.com"
    licence = "MIT"
    description = "Lol"

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.a", dst="lib")


    def package_info(self):
        self.cpp_info.libs = ["lib1"]
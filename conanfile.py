from conans import ConanFile, CMake

class Sg14Conan(ConanFile):
    name = "sg14"
    version = "0.1"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    exports_sources = "CMakeLists.txt", "SG14/*"

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

cmake_minimum_required(VERSION 3.10)
project(app)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(app main.c)
target_link_libraries(app PUBLIC CONAN_PKG::lib2)
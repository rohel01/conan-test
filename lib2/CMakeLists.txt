cmake_minimum_required(VERSION 3.10)
project(lib2)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_library(lib2 lib2.c)
#target_include_directories(lib2 PUBLIC ${CONAN_INCLUDE_DIRS})
cmake_minimum_required(VERSION 3.1)
project(TimSdk CXX)

set(CMAKE_SYSTEM_PROCESSOR arm64)
set(CMAKE_OSX_ARCHITECTURES arm64)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()



add_library(TimSdk TimSdk.cpp)

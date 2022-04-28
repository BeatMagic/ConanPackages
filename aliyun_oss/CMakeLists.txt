cmake_minimum_required(VERSION 3.15)
project(AliyunOss CXX)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(CMAKE_OSX_DEPLOYMENT_TARGET "10.14.0")

# 引用第三方库
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_subdirectory(src)

#add_library(AliyunOss src/AliyunOss.cpp)
#
#set_target_properties(AliyunOss PROPERTIES PUBLIC_HEADER "src/AliyunOss.h")
#install(TARGETS AliyunOss DESTINATION "."
#        PUBLIC_HEADER DESTINATION include
#        RUNTIME DESTINATION bin
#        ARCHIVE DESTINATION lib
#        LIBRARY DESTINATION lib
#        )

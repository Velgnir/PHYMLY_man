cmake_minimum_required(VERSION 3.17)
enable_language(CXX)
project(phymly_man)
find_package(SFML 2.5.1 COMPONENTS graphics audio)
set(CMAKE_CXX_STANDARD 17)

include_directories(inc)

add_executable(phymly_man main.cpp inc/visualization.hpp src/visualization.cpp)

target_link_libraries(phymly_man sfml-graphics sfml-audio)
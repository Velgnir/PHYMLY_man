cmake_minimum_required(VERSION 3.15)

set(PROJECT_NAME thermal_conductivity)
project(${PROJECT_NAME} CXX)

set(CMAKE_CXX_STANDARD 17)

# Options
set(WARNINGS_AS_ERRORS ON)
set(ENABLE_PVS_STUDIO OFF)
set(ENABLE_SANITIZERS ON) # Option for the test builds. Do not use it in the production builds.

if (NOT CMAKE_BUILD_TYPE)
	set(CMAKE_BUILD_TYPE Release)
endif()

# Set output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/../bin)

# Include headers
include_directories(include)

# Project source compilation
add_executable(${PROJECT_NAME} src/main.cpp src/formula.cpp src/files/config_file.cpp src/visualization.cpp)

# Add external packages
find_package(Boost 1.71.0 COMPONENTS program_options REQUIRED)
include_directories(${Boost_INCLUDE_DIR})
target_link_libraries(${PROJECT_NAME} Boost::program_options)

# set output directory (bin)
set_target_properties(${PROJECT_NAME}
						PROPERTIES
						RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)

set(YOU_NEED_X11 1)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread")
set(YOU_NEED_PNG 1)

find_package(X11 REQUIRED)
include_directories(${X11_INCLUDE_DIR})
target_link_libraries(${PROJECT_NAME} ${X11_LIBRARIES})
find_package(PNG REQUIRED)
include_directories(${PNG_INCLUDE_DIR})
target_link_libraries (${PROJECT_NAME} ${PNG_LIBRARY})
target_compile_definitions(${PROJECT_NAME} PRIVATE cimg_use_png=1)

# Include fixed CMake configuration
set (ALL_TARGETS ${PROJECT_NAME})

include(cmake/config.cmake)



# Project Dependences Configuration

# Find OpenCV
set(OpenCV_STATIC OFF CACHE BOOL "Using OpenCV static linking library")
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

# Find YORO C++ API
find_package(yoro_api REQUIRED)
include_directories(${yoro_api_INCLUDE_DIRS})

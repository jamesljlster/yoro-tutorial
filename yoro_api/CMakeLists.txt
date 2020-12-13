cmake_minimum_required(VERSION 3.10)

# Disable in-source builds to prevent source tree corruption.
if(" ${CMAKE_SOURCE_DIR}" STREQUAL " ${CMAKE_BINARY_DIR}")
    message(FATAL_ERROR "\nFATAL: In-source builds are not allowed.\n"
        "You should create a separate directory for build files."
        )
endif()

# Default installation path
set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}/install" CACHE PATH "Installation directory")

# Initialize RPATH settings for shared library loading
set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

# Set project
project(yoro_tutorial CXX)

# Find OpenCV
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

# Find YORO C++ API
find_package(yoro_api REQUIRED)
include_directories(${yoro_api_INCLUDE_DIRS})

# Build C++ examples
file(GLOB PROJECT_SRCS "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp")
foreach(FILE_PATH ${PROJECT_SRCS})

    # Get each file name
    get_filename_component(FILE_NAME ${FILE_PATH} NAME_WE)

    # Build executable
    add_executable(${FILE_NAME} ${FILE_PATH})
    set_target_properties(${FILE_NAME} PROPERTIES
        CXX_STANDARD 11
        OUTPUT_NAME ${FILE_NAME}
        )

    # Link libraries
    target_link_libraries(${FILE_NAME} yoro_api ${OpenCV_LIBS})

    # Install
    install(TARGETS ${FILE_NAME} DESTINATION "${CMAKE_INSTALL_PREFIX}")

endforeach()

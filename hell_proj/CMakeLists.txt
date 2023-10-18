cmake_minimum_required(VERSION 3.16)
project(hell_proj)
set(CMAKE_CXX_STANDARD 20)

option(BUILD_TESTS "Build hell_proj tests" ON)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

add_subdirectory(src)
if (BUILD_TESTS)
    add_subdirectory(tests)
endif()

if(MSVC)
    add_compile_options(/W4 /WX)
else()
    add_compile_options(-Wall -Wextra -Wpedantic -Werror)
endif()

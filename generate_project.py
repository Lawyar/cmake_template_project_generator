#!/bin/python3

import argparse
import os

cmake_min_version = 3.16
cpp_standard = 20
msvc_compile_options = "/W4 /WX"
gnu_compile_options = "-Wall -Wextra -Wpedantic -Werror"
gtest_url = "https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip"

def generate_main_cmake(project_name):
    cmake_string = f"cmake_minimum_required(VERSION {cmake_min_version})\n"
    cmake_string += f"project({project_name})\n"
    cmake_string += f"set(CMAKE_CXX_STANDARD {cpp_standard})\n\n"
    cmake_string += f"option(BUILD_TESTS \"Build {project_name} tests\" ON)\n\n"

    cmake_string += ("set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)\n" +
                     "set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)\n" +
                     "set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)\n\n")

    cmake_string += ("add_subdirectory(src)\n" +
                     "if (BUILD_TESTS)\n"+
                     "    add_subdirectory(tests)\n" +
                     "endif()\n\n")
    
    cmake_string += ("if(MSVC)\n"+
                      f"    add_compile_options({msvc_compile_options})\n" +
                      "else()\n"
                      f"    add_compile_options({gnu_compile_options})\n" +
                      "endif()\n")
    
    cmake_lists = open("CMakeLists.txt", "w")
    cmake_lists.write(cmake_string)


def generate_gitignore():
    gigignore_string = ("build/\n" +
                        ".vscode/\n" +
                        ".idea/\n")
    gitignore = open(".gitignore", "w")
    gitignore.write(gigignore_string)


def generate_applications(application_names):
    applications_main_cmake_string = ""
    for application_name in application_names:
        applications_main_cmake_string += f"add_subdirectory({application_name})\n"

    main_tests_cmake = open("CMakeLists.txt", "w")
    main_tests_cmake.write(applications_main_cmake_string)

    for application_name in application_names:
        os.mkdir(application_name)
        os.chdir(application_name)
        cmake_string = ("file(GLOB INCS *.cpp)\n" + 
                        "file(GLOB SRCS *.cpp)\n" +
                         f"add_executable({application_name} ${{INCS}} ${{SRCS}})\n")
        tests_cmake = open("CMakeLists.txt", "w")
        tests_cmake.write(cmake_string)
        generate_main_cpp()
        os.chdir("..")


def generate_main_cpp():
    main_cpp_string = ("#include <iostream>\n\n"
                       "using namespace std;\n\n"
                       "int main(int argc, char** argv)\n"
                       "{\n"
                       "    cout << \"Hello\\n\";\n"
                       "}\n\n")
    main_cpp = open("main.cpp", "w")
    main_cpp.write(main_cpp_string)
    

def generate_cmake_for_sources(library_names):
    src_cmake_string = ""
    for library_name in library_names:
        src_cmake_string += f"add_subdirectory({library_name})\n"

    src_cmake = open("CMakeLists.txt", "w")
    src_cmake.write(src_cmake_string)
    generate_cmake_for_libraries(library_names)


def generate_cmake_for_libraries(library_names):
        for library_name in library_names:
            os.mkdir(library_name)
            os.chdir(library_name)
            cmake_string = ("file(GLOB INCS *.cpp)\n" + 
                            "file(GLOB SRCS *.cpp)\n" +
                            f"add_library({library_name} ${{INCS}} ${{SRCS}})\n")
            tests_cmake = open("CMakeLists.txt", "w")
            tests_cmake.write(cmake_string)
            os.chdir("..")


def generate_cmake_for_tests(library_names):
    tests_main_cmake_string = "enable_testing()\n"
    for library_name in library_names:
        tests_main_cmake_string += f"add_subdirectory({library_name})\n"
    tests_main_cmake_string += "\n"

    tests_main_cmake_string += ("include(FetchContent)\n"+
                                "FetchContent_Declare(\n" +
                                 "    googletest\n" +
                                 "    URL {gtest_url}\n" +
                                 ")\n")
    main_tests_cmake = open("CMakeLists.txt", "w")
    main_tests_cmake.write(tests_main_cmake_string)
    generate_cmake_for_library_tests(library_names)


def generate_cmake_for_library_tests(library_names):
    for library_name in library_names:
        tests_name = f"{library_name}_tests" 
        os.mkdir(tests_name)
        os.chdir(tests_name)
        cmake_string = ("file(GLOB SRCS *.cpp)\n" +
                        f"add_executable({tests_name} ${{SRCS}})\n" +
                        f"target_link_libraries({tests_name} PRIVATE {library_name} gtest_main)\n" +
                        f"target_include_directories(${{CMAKE_SOURCE_DIR}}/src/{library_name})\n")
        
        tests_cmake = open("CMakeLists.txt", "w")
        tests_cmake.write(cmake_string)
        os.chdir("..")


def generate_project(project_name, library_names, application_names):
    os.mkdir(project_name)
    os.chdir(project_name)
    
    generate_main_cmake(project_name)
    generate_gitignore()

    os.mkdir("applications")
    os.chdir("applications")
    generate_applications(application_names)
    os.chdir("..")

    os.mkdir("src")
    os.chdir("src")
    generate_cmake_for_sources(library_names)
    os.chdir("..")

    os.mkdir("tests")
    os.chdir("tests")
    generate_cmake_for_tests(library_names)
    os.chdir("..")
    

parser = argparse.ArgumentParser(description='Generate template CMake project')
parser.add_argument('-p', '--project_name', type=str, help="project name")
parser.add_argument('-l', '--libraries', action="extend", nargs="+", type=str, help="libraries list")
parser.add_argument('-a', '--applications', action="extend", nargs="+", type=str, help="applications list")

args = parser.parse_args()
generate_project(args.project_name, args.libraries, args.applications)

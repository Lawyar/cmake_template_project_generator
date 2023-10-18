file(GLOB SRCS *.cpp)
add_executable(dell_tests ${SRCS})
target_link_libraries(dell_tests PRIVATE dell gtest_main)
target_include_directories(${CMAKE_SOURCE_DIR}/src/dell)

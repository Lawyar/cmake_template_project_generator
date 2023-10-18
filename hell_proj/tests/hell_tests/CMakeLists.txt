file(GLOB SRCS *.cpp)
add_executable(hell_tests ${SRCS})
target_link_libraries(hell_tests PRIVATE hell gtest_main)
target_include_directories(hell_tests PRIVATE ${CMAKE_SOURCE_DIR}/src/hell)

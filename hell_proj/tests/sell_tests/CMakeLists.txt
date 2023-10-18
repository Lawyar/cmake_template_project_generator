file(GLOB SRCS *.cpp)
add_executable(sell_tests ${SRCS})
target_link_libraries(sell_tests PRIVATE sell gtest_main)
target_include_directories(sell_tests PRIVATE ${CMAKE_SOURCE_DIR}/src/sell)

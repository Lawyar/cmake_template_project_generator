enable_testing()

add_subdirectory(dell_tests)
add_subdirectory(hell_tests)
add_subdirectory(sell_tests)

include(FetchContent)
FetchContent_Declare(
    googletest
    URL {gtest_url}
)

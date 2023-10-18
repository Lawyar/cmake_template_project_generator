enable_testing()
add_subdirectory(hell)
add_subdirectory(dell)
add_subdirectory(sell)

include(FetchContent)
FetchContent_Declare(
    googletest
    URL {gtest_url}
)

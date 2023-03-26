#
# gpt-j-online

set(TEST_TARGET gpt-j-online)
add_executable(${TEST_TARGET} main.cpp)
target_link_libraries(${TEST_TARGET} PRIVATE ggml ggml_utils)

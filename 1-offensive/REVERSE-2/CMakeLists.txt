cmake_minimum_required(VERSION 3.14)
project(task1)

# GoogleTest requires at least C++14
set(CMAKE_CXX_STANDARD 17)

add_executable(
    old_times
    ./src/main.cpp
    ./src/interpreter.cpp
    ./src/smth.cpp
)
add_executable(
    test
    ./src/test.cpp
)
target_link_libraries(
  old_times 
  ${CMAKE_SOURCE_DIR}/uni/unicorn/build/libunicorn.a
  ${CMAKE_SOURCE_DIR}/uni/unicorn/build/libunicorn-common.a
  ${CMAKE_SOURCE_DIR}/uni/unicorn/build/libmipsel-softmmu.a
  ${CMAKE_SOURCE_DIR}/uni/unicorn/build/libmips-softmmu.a
  )
  target_link_libraries(
    test
    ${CMAKE_SOURCE_DIR}/uni/unicorn/build/libunicorn.a
    ${CMAKE_SOURCE_DIR}/uni/unicorn/build/libunicorn-common.a
    ${CMAKE_SOURCE_DIR}/uni/unicorn/build/libmipsel-softmmu.a
    ${CMAKE_SOURCE_DIR}/uni/unicorn/build/libmips-softmmu.a
    )
target_link_libraries(
  old_times -s -static -OFast
)
target_link_libraries(
  test -s -static -OFast
)




# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.25

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build

# Include any dependencies generated for this target.
include CMakeFiles/test_mips.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/test_mips.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/test_mips.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/test_mips.dir/flags.make

CMakeFiles/test_mips.dir/tests/unit/test_mips.c.o: CMakeFiles/test_mips.dir/flags.make
CMakeFiles/test_mips.dir/tests/unit/test_mips.c.o: /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/tests/unit/test_mips.c
CMakeFiles/test_mips.dir/tests/unit/test_mips.c.o: CMakeFiles/test_mips.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/test_mips.dir/tests/unit/test_mips.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/test_mips.dir/tests/unit/test_mips.c.o -MF CMakeFiles/test_mips.dir/tests/unit/test_mips.c.o.d -o CMakeFiles/test_mips.dir/tests/unit/test_mips.c.o -c /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/tests/unit/test_mips.c

CMakeFiles/test_mips.dir/tests/unit/test_mips.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test_mips.dir/tests/unit/test_mips.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/tests/unit/test_mips.c > CMakeFiles/test_mips.dir/tests/unit/test_mips.c.i

CMakeFiles/test_mips.dir/tests/unit/test_mips.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test_mips.dir/tests/unit/test_mips.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/tests/unit/test_mips.c -o CMakeFiles/test_mips.dir/tests/unit/test_mips.c.s

# Object files for target test_mips
test_mips_OBJECTS = \
"CMakeFiles/test_mips.dir/tests/unit/test_mips.c.o"

# External object files for target test_mips
test_mips_EXTERNAL_OBJECTS =

test_mips: CMakeFiles/test_mips.dir/tests/unit/test_mips.c.o
test_mips: CMakeFiles/test_mips.dir/build.make
test_mips: libunicorn.so.2
test_mips: CMakeFiles/test_mips.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable test_mips"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_mips.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/test_mips.dir/build: test_mips
.PHONY : CMakeFiles/test_mips.dir/build

CMakeFiles/test_mips.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/test_mips.dir/cmake_clean.cmake
.PHONY : CMakeFiles/test_mips.dir/clean

CMakeFiles/test_mips.dir/depend:
	cd /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles/test_mips.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test_mips.dir/depend


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
include CMakeFiles/sample_ppc.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/sample_ppc.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/sample_ppc.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/sample_ppc.dir/flags.make

CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.o: CMakeFiles/sample_ppc.dir/flags.make
CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.o: /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/samples/sample_ppc.c
CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.o: CMakeFiles/sample_ppc.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.o -MF CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.o.d -o CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.o -c /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/samples/sample_ppc.c

CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/samples/sample_ppc.c > CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.i

CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/samples/sample_ppc.c -o CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.s

# Object files for target sample_ppc
sample_ppc_OBJECTS = \
"CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.o"

# External object files for target sample_ppc
sample_ppc_EXTERNAL_OBJECTS =

sample_ppc: CMakeFiles/sample_ppc.dir/samples/sample_ppc.c.o
sample_ppc: CMakeFiles/sample_ppc.dir/build.make
sample_ppc: libunicorn.so.2
sample_ppc: CMakeFiles/sample_ppc.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable sample_ppc"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sample_ppc.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/sample_ppc.dir/build: sample_ppc
.PHONY : CMakeFiles/sample_ppc.dir/build

CMakeFiles/sample_ppc.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/sample_ppc.dir/cmake_clean.cmake
.PHONY : CMakeFiles/sample_ppc.dir/clean

CMakeFiles/sample_ppc.dir/depend:
	cd /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles/sample_ppc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/sample_ppc.dir/depend


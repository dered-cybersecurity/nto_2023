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
include CMakeFiles/sample_sparc.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/sample_sparc.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/sample_sparc.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/sample_sparc.dir/flags.make

CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.o: CMakeFiles/sample_sparc.dir/flags.make
CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.o: /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/samples/sample_sparc.c
CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.o: CMakeFiles/sample_sparc.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.o -MF CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.o.d -o CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.o -c /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/samples/sample_sparc.c

CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/samples/sample_sparc.c > CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.i

CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/samples/sample_sparc.c -o CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.s

# Object files for target sample_sparc
sample_sparc_OBJECTS = \
"CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.o"

# External object files for target sample_sparc
sample_sparc_EXTERNAL_OBJECTS =

sample_sparc: CMakeFiles/sample_sparc.dir/samples/sample_sparc.c.o
sample_sparc: CMakeFiles/sample_sparc.dir/build.make
sample_sparc: libunicorn.so.2
sample_sparc: CMakeFiles/sample_sparc.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable sample_sparc"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sample_sparc.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/sample_sparc.dir/build: sample_sparc
.PHONY : CMakeFiles/sample_sparc.dir/build

CMakeFiles/sample_sparc.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/sample_sparc.dir/cmake_clean.cmake
.PHONY : CMakeFiles/sample_sparc.dir/clean

CMakeFiles/sample_sparc.dir/depend:
	cd /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles/sample_sparc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/sample_sparc.dir/depend


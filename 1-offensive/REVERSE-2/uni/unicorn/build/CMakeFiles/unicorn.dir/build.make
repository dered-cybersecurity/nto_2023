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
include CMakeFiles/unicorn.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/unicorn.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/unicorn.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/unicorn.dir/flags.make

CMakeFiles/unicorn.dir/uc.c.o: CMakeFiles/unicorn.dir/flags.make
CMakeFiles/unicorn.dir/uc.c.o: /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/uc.c
CMakeFiles/unicorn.dir/uc.c.o: CMakeFiles/unicorn.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/unicorn.dir/uc.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/unicorn.dir/uc.c.o -MF CMakeFiles/unicorn.dir/uc.c.o.d -o CMakeFiles/unicorn.dir/uc.c.o -c /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/uc.c

CMakeFiles/unicorn.dir/uc.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/unicorn.dir/uc.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/uc.c > CMakeFiles/unicorn.dir/uc.c.i

CMakeFiles/unicorn.dir/uc.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/unicorn.dir/uc.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/uc.c -o CMakeFiles/unicorn.dir/uc.c.s

CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.o: CMakeFiles/unicorn.dir/flags.make
CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.o: /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/qemu/softmmu/vl.c
CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.o: CMakeFiles/unicorn.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.o -MF CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.o.d -o CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.o -c /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/qemu/softmmu/vl.c

CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/qemu/softmmu/vl.c > CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.i

CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/qemu/softmmu/vl.c -o CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.s

CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.o: CMakeFiles/unicorn.dir/flags.make
CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.o: /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/qemu/hw/core/cpu.c
CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.o: CMakeFiles/unicorn.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.o -MF CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.o.d -o CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.o -c /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/qemu/hw/core/cpu.c

CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/qemu/hw/core/cpu.c > CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.i

CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/qemu/hw/core/cpu.c -o CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.s

# Object files for target unicorn
unicorn_OBJECTS = \
"CMakeFiles/unicorn.dir/uc.c.o" \
"CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.o" \
"CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.o"

# External object files for target unicorn
unicorn_EXTERNAL_OBJECTS =

libunicorn.so.2: CMakeFiles/unicorn.dir/uc.c.o
libunicorn.so.2: CMakeFiles/unicorn.dir/qemu/softmmu/vl.c.o
libunicorn.so.2: CMakeFiles/unicorn.dir/qemu/hw/core/cpu.c.o
libunicorn.so.2: CMakeFiles/unicorn.dir/build.make
libunicorn.so.2: libunicorn-common.a
libunicorn.so.2: libx86_64-softmmu.a
libunicorn.so.2: libarm-softmmu.a
libunicorn.so.2: libaarch64-softmmu.a
libunicorn.so.2: libm68k-softmmu.a
libunicorn.so.2: libmips-softmmu.a
libunicorn.so.2: libmipsel-softmmu.a
libunicorn.so.2: libmips64-softmmu.a
libunicorn.so.2: libmips64el-softmmu.a
libunicorn.so.2: libsparc-softmmu.a
libunicorn.so.2: libsparc64-softmmu.a
libunicorn.so.2: libppc-softmmu.a
libunicorn.so.2: libppc64-softmmu.a
libunicorn.so.2: libriscv32-softmmu.a
libunicorn.so.2: libriscv64-softmmu.a
libunicorn.so.2: libs390x-softmmu.a
libunicorn.so.2: libtricore-softmmu.a
libunicorn.so.2: libunicorn-common.a
libunicorn.so.2: CMakeFiles/unicorn.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking C shared library libunicorn.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/unicorn.dir/link.txt --verbose=$(VERBOSE)
	$(CMAKE_COMMAND) -E cmake_symlink_library libunicorn.so.2 libunicorn.so.2 libunicorn.so

libunicorn.so: libunicorn.so.2
	@$(CMAKE_COMMAND) -E touch_nocreate libunicorn.so

# Rule to build all files generated by this target.
CMakeFiles/unicorn.dir/build: libunicorn.so
.PHONY : CMakeFiles/unicorn.dir/build

CMakeFiles/unicorn.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/unicorn.dir/cmake_clean.cmake
.PHONY : CMakeFiles/unicorn.dir/clean

CMakeFiles/unicorn.dir/depend:
	cd /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build /home/c3nt/Projects/Olymp_tasks/Old_Times/uni/unicorn/build/CMakeFiles/unicorn.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/unicorn.dir/depend

# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2019.3.5\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2019.3.5\bin\cmake\win\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "C:\Users\pyw08\Desktop\BOJ step-by-step problem solving"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "C:\Users\pyw08\Desktop\BOJ step-by-step problem solving\cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/BOJ__.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/BOJ__.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/BOJ__.dir/flags.make

CMakeFiles/BOJ__.dir/Step2_-_if_statement/BOJ2884.cpp.obj: CMakeFiles/BOJ__.dir/flags.make
CMakeFiles/BOJ__.dir/Step2_-_if_statement/BOJ2884.cpp.obj: ../Step2\ -\ if\ statement/BOJ2884.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="C:\Users\pyw08\Desktop\BOJ step-by-step problem solving\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/BOJ__.dir/Step2_-_if_statement/BOJ2884.cpp.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\BOJ__.dir\Step2_-_if_statement\BOJ2884.cpp.obj -c "C:\Users\pyw08\Desktop\BOJ step-by-step problem solving\Step2 - if statement\BOJ2884.cpp"

CMakeFiles/BOJ__.dir/Step2_-_if_statement/BOJ2884.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/BOJ__.dir/Step2_-_if_statement/BOJ2884.cpp.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "C:\Users\pyw08\Desktop\BOJ step-by-step problem solving\Step2 - if statement\BOJ2884.cpp" > CMakeFiles\BOJ__.dir\Step2_-_if_statement\BOJ2884.cpp.i

CMakeFiles/BOJ__.dir/Step2_-_if_statement/BOJ2884.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/BOJ__.dir/Step2_-_if_statement/BOJ2884.cpp.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "C:\Users\pyw08\Desktop\BOJ step-by-step problem solving\Step2 - if statement\BOJ2884.cpp" -o CMakeFiles\BOJ__.dir\Step2_-_if_statement\BOJ2884.cpp.s

# Object files for target BOJ__
BOJ___OBJECTS = \
"CMakeFiles/BOJ__.dir/Step2_-_if_statement/BOJ2884.cpp.obj"

# External object files for target BOJ__
BOJ___EXTERNAL_OBJECTS =

BOJ__.exe: CMakeFiles/BOJ__.dir/Step2_-_if_statement/BOJ2884.cpp.obj
BOJ__.exe: CMakeFiles/BOJ__.dir/build.make
BOJ__.exe: CMakeFiles/BOJ__.dir/linklibs.rsp
BOJ__.exe: CMakeFiles/BOJ__.dir/objects1.rsp
BOJ__.exe: CMakeFiles/BOJ__.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="C:\Users\pyw08\Desktop\BOJ step-by-step problem solving\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable BOJ__.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\BOJ__.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/BOJ__.dir/build: BOJ__.exe

.PHONY : CMakeFiles/BOJ__.dir/build

CMakeFiles/BOJ__.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\BOJ__.dir\cmake_clean.cmake
.PHONY : CMakeFiles/BOJ__.dir/clean

CMakeFiles/BOJ__.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "C:\Users\pyw08\Desktop\BOJ step-by-step problem solving" "C:\Users\pyw08\Desktop\BOJ step-by-step problem solving" "C:\Users\pyw08\Desktop\BOJ step-by-step problem solving\cmake-build-debug" "C:\Users\pyw08\Desktop\BOJ step-by-step problem solving\cmake-build-debug" "C:\Users\pyw08\Desktop\BOJ step-by-step problem solving\cmake-build-debug\CMakeFiles\BOJ__.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/BOJ__.dir/depend

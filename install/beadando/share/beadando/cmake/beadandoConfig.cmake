# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_beadando_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED beadando_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(beadando_FOUND FALSE)
  elseif(NOT beadando_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(beadando_FOUND FALSE)
  endif()
  return()
endif()
set(_beadando_CONFIG_INCLUDED TRUE)

# output package information
if(NOT beadando_FIND_QUIETLY)
  message(STATUS "Found beadando: 0.3.4 (${beadando_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'beadando' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${beadando_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(beadando_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${beadando_DIR}/${_extra}")
endforeach()

cmake_minimum_required(VERSION 3.8)
project(sherlock)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

add_executable(sherlock1 src/sherlock1.cpp)
ament_target_dependencies(sherlock1 rclcpp std_msgs)


add_executable(sherlock2 src/sherlock1.cpp)
ament_target_dependencies(sherlock2 rclcpp std_msgs)


add_executable(anderson src/anderson.cpp)
ament_target_dependencies(anderson rclcpp std_msgs)

install(TARGETS
  sherlock1
  sherlock2
  anderson
  DESTINATION lib/${PROJECT_NAME})
ament_package()

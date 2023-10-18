# Cmake project generator  

Usage: `python3 ./generate_project.py [-p PROJECT_NAME] [-l LIBRARIES [LIBRARIES ...]] [-a APPLICATIONS [APPLICATIONS ...]]`  

Project inside the repository was generated using `python3 generate_project.py -p hell_proj -l hell dell sell -a s1 s2 s3 s4`  

Note that for proper configuring you should add source into generated libraries and tests. Otherwise, CMake error will occur.  

Project hierarchy:  
<pre>
project_name  
|_ applications  
  |_sample1  
    |_main.cpp  
|_src  
  |_lib1  
    |_whatever.h  
    |_whatever.cpp  
  |_lib2  
    |_anything.h  
    |_anything.cpp  
|_tests  
  |_lib1_tests  
    |_whatever_1_tests.cpp  
    |_whatever_2_tests.cpp  
  |_lib2_tests  
    |_anything_tests.cpp  
</pre>

## Notable Differences Between CORP 1 & CORP 2

### Development Environment
* The engine is now being developed with a Python binding of Raylib (using the C API), which makes it faster.

### Style
* CORP 2 uses PascalCase for classes, instances and methods, while using camelCase for variables.

### Objects & Services
* The Object Service is removed, instead you can use the NewObject() and RemoveObject() functions imported from main.
* Several attributes & methods like type & children are protected.
* Children lists are now dictionaries. The only way to get the children list is to call GetChildren()
* A new component system is here, which erases most services like GUIService, ScriptService.

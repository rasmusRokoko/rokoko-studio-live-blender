# Important plugin info for Blender
bl_info = {
    'name': 'Rokoko SmartsuitPro',
    'author': 'Rokoko',
    'category': 'Animation',
    'location': 'View 3D > Tool Shelf > SmartsuitPro',
    'description': 'Import your Smartsuit animation directly into Blender',
    'version': (0, 1),
    'blender': (2, 80, 0),
}

# If first startup of this plugin, load all modules normally
# If reloading the plugin, use importlib to reload modules
# This lets you do adjustments to the plugin on the fly without having to restart Blender
if "bpy" not in locals():
    import bpy
    from . import core
    from . import panels
    from . import operators
    from . import properties
else:
    import importlib
    importlib.reload(core)
    importlib.reload(panels)
    importlib.reload(operators)
    importlib.reload(properties)


# List of all buttons and panels
classes = [
    panels.main.ReceiverPanel,
    panels.objects.ObjectsPanel,
    operators.receiver.ReceiverStart,
    operators.receiver.ReceiverStop,
]


# register and unregister all classes
def register():
    print("\n### Loading SmartsuitPro...")

    # Register all classes
    for cls in classes:
        bpy.utils.register_class(cls)

    properties.register()

    print("### Loaded SmartsuitPro successfully!\n")


def unregister():
    print("### Unloading SmartsuitPro...")

    # Register all classes
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    print("### Unloaded SmartsuitPro successfully!\n")


if __name__ == '__main__':
    register()
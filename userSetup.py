import sys
import maya.cmds as cmds

tool_dir = r"C:\Users\23684\Documents\maya\2022\zh_CN\scripts"
if tool_dir not in sys.path:
    sys.path.append(tool_dir)

menu_name = "Yeti"

def load_yeti_tools():
    try:
        import gerenzhuanyong
        gerenzhuanyong.main()  # 创建菜单
    except Exception as e:
        cmds.warning(f"Failed to load yeti_tools at startup: {e}")

# 延迟执行，保证 UI 初始化完成
if not cmds.menu(menu_name, exists=True):
    cmds.evalDeferred(load_yeti_tools)

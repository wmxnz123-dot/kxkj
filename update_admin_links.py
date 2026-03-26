import os
import glob

html_files = glob.glob('prototype_ui/admin_*.html')

sidebar_content = """        <ul class="space-y-1" id="sidebar-menu">
            <!-- 工作台 -->
            <li>
                <a href="admin_workbench.html" class="flex items-center px-6 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition">
                    <i class="fa-solid fa-desktop w-6"></i> <span class="ml-3">智能工作台</span>
                </a>
            </li>
            <!-- 数据检索管理 -->
            <li>
                <div class="flex items-center justify-between px-6 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition cursor-pointer" onclick="toggleMenu(this)">
                    <div class="flex items-center">
                        <i class="fa-solid fa-magnifying-glass w-6"></i> <span class="ml-3">数据检索管理</span>
                    </div>
                    <i class="fa-solid fa-angle-down text-xs transition-transform duration-200"></i>
                </div>
                <ul class="pl-14 py-2 space-y-3 text-sm hidden bg-gray-800/50">
                    <li><a href="admin_dashboard.html" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">数据检索</a></li>
                    <li><a href="admin_data_map.html" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">3D人口态势大屏</a></li>
                    <li><a href="admin_search_config.html" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">数据检索配置</a></li>
                </ul>
            </li>
            <!-- 认领数据管理 -->"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_marker = '<ul class="space-y-1" id="sidebar-menu">'
    end_marker = '<!-- 认领数据管理 -->'
    
    if start_marker in content and end_marker in content:
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[1]
        new_content = before + sidebar_content + after
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

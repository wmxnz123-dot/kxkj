import os
import glob
import re

sidebar_content = """<aside class="w-64 bg-gray-900 text-white flex flex-col h-full">
    <div class="h-16 flex items-center px-6 border-b border-gray-800">
        <i class="fa-solid fa-cubes text-blue-500 text-2xl mr-3"></i>
        <span class="text-lg font-bold tracking-wider">一人一档后台</span>
    </div>
    <div class="flex-1 overflow-y-auto py-4">
        <ul class="space-y-1" id="sidebar-menu">
            <!-- 工作台 -->
            <li>
                <a href="admin_dashboard.html" class="flex items-center px-6 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition">
                    <i class="fa-solid fa-desktop w-6"></i> <span class="ml-3">工作台</span>
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
                    <li><a href="#" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">数图分析</a></li>
                    <li><a href="#" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">数据检索配置</a></li>
                </ul>
            </li>
            <!-- 认领数据管理 -->
            <li>
                <div class="flex items-center justify-between px-6 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition cursor-pointer" onclick="toggleMenu(this)">
                    <div class="flex items-center">
                        <i class="fa-solid fa-hand-holding-hand w-6"></i> <span class="ml-3">认领数据管理</span>
                    </div>
                    <i class="fa-solid fa-angle-down text-xs transition-transform duration-200"></i>
                </div>
                <ul class="pl-14 py-2 space-y-3 text-sm hidden bg-gray-800/50">
                    <li><a href="admin_catalog_config.html" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">目录管理</a></li>
                    <li><a href="admin_corrections.html" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">数据纠错处置</a></li>
                </ul>
            </li>
            <!-- 自有数据管理 -->
            <li>
                <div class="flex items-center justify-between px-6 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition cursor-pointer" onclick="toggleMenu(this)">
                    <div class="flex items-center">
                        <i class="fa-solid fa-folder-open w-6"></i> <span class="ml-3">自有数据管理</span>
                    </div>
                    <i class="fa-solid fa-angle-down text-xs transition-transform duration-200"></i>
                </div>
                <ul class="pl-14 py-2 space-y-3 text-sm hidden bg-gray-800/50">
                    <li><a href="#" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">目录管理</a></li>
                </ul>
            </li>
            <!-- 授权管理 -->
            <li>
                <div class="flex items-center justify-between px-6 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition cursor-pointer" onclick="toggleMenu(this)">
                    <div class="flex items-center">
                        <i class="fa-solid fa-shield-halved w-6"></i> <span class="ml-3">授权管理</span>
                    </div>
                    <i class="fa-solid fa-angle-down text-xs transition-transform duration-200"></i>
                </div>
                <ul class="pl-14 py-2 space-y-3 text-sm hidden bg-gray-800/50">
                    <li><a href="admin_auth_templates.html" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">规则配置</a></li>
                    <li><a href="#" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">异常监控</a></li>
                    <li><a href="#" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">可信存证服务</a></li>
                    <li><a href="admin_auth_records.html" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">授权统计分析</a></li>
                </ul>
            </li>
            <!-- 数据服务管理 -->
            <li>
                <a href="admin_services_config.html" class="flex items-center px-6 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition">
                    <i class="fa-solid fa-layer-group w-6"></i> <span class="ml-3">数据服务管理</span>
                </a>
            </li>
            <!-- 个人中心管理 -->
            <li>
                <div class="flex items-center justify-between px-6 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition cursor-pointer" onclick="toggleMenu(this)">
                    <div class="flex items-center">
                        <i class="fa-solid fa-user-gear w-6"></i> <span class="ml-3">个人中心管理</span>
                    </div>
                    <i class="fa-solid fa-angle-down text-xs transition-transform duration-200"></i>
                </div>
                <ul class="pl-14 py-2 space-y-3 text-sm hidden bg-gray-800/50">
                    <li><a href="#" class="text-gray-400 hover:text-white transition relative before:content-[''] before:absolute before:-left-4 before:top-2 before:w-2 before:h-2 before:border-2 before:border-gray-500 before:rounded-full">仪表盘配置</a></li>
                </ul>
            </li>
            <!-- 监管统计 -->
            <li>
                <a href="#" class="flex items-center px-6 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition">
                    <i class="fa-solid fa-chart-line w-6"></i> <span class="ml-3">监管统计</span>
                </a>
            </li>
        </ul>
    </div>
</aside>"""

js_content = """
  <script>
    function toggleMenu(element) {
        const ul = element.nextElementSibling;
        const icon = element.querySelector('.fa-angle-down');
        if (ul.classList.contains('hidden')) {
            ul.classList.remove('hidden');
            icon.classList.add('rotate-180');
        } else {
            ul.classList.add('hidden');
            icon.classList.remove('rotate-180');
        }
    }
    
    // Highlight active menu based on current URL
    document.addEventListener("DOMContentLoaded", function() {
        const currentPath = window.location.pathname.split('/').pop();
        if(!currentPath) return;
        
        const links = document.querySelectorAll('#sidebar-menu a');
        links.forEach(link => {
            const href = link.getAttribute('href');
            if(href && href !== '#' && currentPath.includes(href)) {
                // If it's a submenu item
                const parentUl = link.closest('ul.pl-14');
                if(parentUl) {
                    parentUl.classList.remove('hidden');
                    const parentDiv = parentUl.previousElementSibling;
                    if(parentDiv) {
                        parentDiv.classList.add('bg-blue-600', 'text-white', 'border-r-4', 'border-blue-400');
                        parentDiv.classList.remove('text-gray-300', 'hover:bg-gray-800');
                        const icon = parentDiv.querySelector('.fa-angle-down');
                        if(icon) icon.classList.add('rotate-180');
                    }
                    link.classList.remove('text-gray-400', 'before:border-gray-500');
                    link.classList.add('text-white', 'before:bg-blue-400', 'before:border-transparent');
                } else {
                    // Top level item
                    link.classList.add('bg-blue-600', 'text-white', 'border-r-4', 'border-blue-400');
                    link.classList.remove('text-gray-300', 'hover:bg-gray-800');
                }
            }
        });
    });
  </script>
"""

files = glob.glob('/Users/zhanghuimin/Downloads/000潍坊个人数据空间/trae/kxkj/prototype_ui/admin_*.html')
for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace aside
    new_content = re.sub(r'<aside class="w-64 bg-gray-900 text-white flex flex-col h-full">.*?</aside>', sidebar_content, content, flags=re.DOTALL)
    
    # Add JS if not present
    if 'function toggleMenu' not in new_content:
        new_content = new_content.replace('</body>', js_content + '</body>')
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file_path}")

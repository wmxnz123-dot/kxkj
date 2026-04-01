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

document.addEventListener("DOMContentLoaded", function() {
    const currentPath = window.location.pathname.split('/').pop() || 'admin_dashboard.html';
    const links = document.querySelectorAll('#sidebar-menu a');
    links.forEach(link => {
        const href = link.getAttribute('href');
        if(href && href !== '#' && currentPath.includes(href)) {
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
                link.classList.add('bg-blue-600', 'text-white', 'border-r-4', 'border-blue-400');
                link.classList.remove('text-gray-300', 'hover:bg-gray-800');
            }
        }
    });
});
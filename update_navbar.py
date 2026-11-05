import os
from pathlib import Path
from bs4 import BeautifulSoup

# Yahan aapka pura updated Navbar ka HTML code ek single string me embedded hai
NEW_NAVBAR_HTML = """
<nav class="sticky top-0 z-50 bg-white shadow-md py-4 transition-all" id="navbar">
<div class="max-w-7xl mx-auto px-6 flex justify-between items-center">
<a class="flex items-center gap-2 group z-50" href="/index">
<div class="w-10 h-10 bg-brand-black text-brand-gold flex items-center justify-center font-bold text-xl rounded transition-transform group-hover:scale-105">FE</div>
<div class="flex flex-col">
<h1 class="font-heading font-bold text-xl text-gray-900 leading-none">Flooring Expert</h1>
<span class="text-xs text-gray-500 uppercase tracking-wide">Surface Solutions</span>
</div>
</a>
<!-- Desktop Menu -->
<div class="hidden lg:flex items-center gap-6 font-medium text-sm text-gray-600">
<a class="hover:text-brand-gold transition-colors" href="/kitchen/index.html">Modular Kitchens</a>

<div class="relative group h-full py-4 cursor-pointer">
<span class="hover:text-brand-gold transition-colors flex items-center gap-1">
                        Carpet tiles <i class="fa-solid fa-chevron-down text-xs ml-1"></i>
</span>
<div class="dropdown-menu absolute top-full left-0 w-56 bg-white shadow-xl rounded-lg border border-gray-100 overflow-hidden py-2 hidden group-hover:block">
<div class="px-4 py-1 text-xs font-bold text-gray-400 uppercase tracking-wider">carpet tiles</div>
<a class="block px-4 py-2 hover:bg-gray-50 hover:text-brand-gold" href="/welspun/carpet-tiles/celestial">Celestial</a>
<a class="block px-4 py-2 hover:bg-gray-50 hover:text-brand-gold" href="/welspun/carpet-tiles/earthy-woods">Earthy Woods</a>
<a class="block px-4 py-2 hover:bg-gray-50 hover:text-brand-gold" href="/welspun/carpet-tiles/meander">Meander</a>
<a class="block px-4 py-2 hover:bg-gray-50 hover:text-brand-gold" href="/welspun/carpet-tiles/savy-street">Savy Street</a>
<a class="block px-4 py-2 hover:bg-gray-50 hover:text-brand-gold" href="/welspun/carpet-tiles/urban-streaks">Urban Streaks</a>
</div>
</div>
<div class="relative group h-full py-4 cursor-pointer">
<span class="hover:text-brand-gold transition-colors flex items-center gap-1">
                        Welspun <i class="fa-solid fa-chevron-down text-xs ml-1"></i>
</span>
<div class="dropdown-menu absolute top-full left-0 w-56 bg-white shadow-xl rounded-lg border border-gray-100 overflow-hidden py-2 hidden group-hover:block">
<div class="px-4 py-1 text-xs font-bold text-gray-400 uppercase tracking-wider">Flooring</div>
<a class="block px-4 py-2 hover:bg-gray-50 hover:text-brand-gold" href="/welspun/welspun-lick-n-lock/index">Click-N-Lock</a>
<a class="block px-4 py-2 hover:bg-gray-50 hover:text-brand-gold" href="/welspun/multistile/index">Multistile</a>
<div class="border-t my-1"></div>
<a class="block px-4 py-2 hover:bg-gray-50 hover:text-brand-gold" href="/welspun/carpet-tiles/index">Carpet Tiles</a>
</div>
</div>
<div class="relative group h-full py-4 cursor-pointer">
<span class="hover:text-brand-gold transition-colors flex items-center gap-1">
                        Pare <i class="fa-solid fa-chevron-down text-xs ml-1"></i>
</span>
<!-- Mega Menu Dropdown -->
<div class="dropdown-menu absolute top-full left-1/2 -translate-x-1/2 w-[600px] bg-white shadow-xl rounded-xl border border-gray-100 p-6 hidden group-hover:block cursor-default z-50">
<div class="grid grid-cols-2 gap-8">
<!-- Column 1: Flooring -->
<div class="border-r border-gray-100 pr-6">
<h3 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4 border-b border-gray-50 pb-2">Flooring</h3>
<div class="flex flex-col gap-3">
<a class="flex items-center text-gray-600 hover:text-brand-gold transition-colors duration-200 font-medium group/link" href="/pare/lvt-flooring">
<i class="fa-solid fa-caret-right text-[10px] mr-2 opacity-0 -translate-x-2 transition-all group-hover/link:opacity-100 group-hover/link:translate-x-0 text-brand-gold"></i>
                                    LVT Flooring
                                </a>
<a class="flex items-center text-gray-600 hover:text-brand-gold transition-colors duration-200 font-medium group/link" href="/pare/spc-flooring">
<i class="fa-solid fa-caret-right text-[10px] mr-2 opacity-0 -translate-x-2 transition-all group-hover/link:opacity-100 group-hover/link:translate-x-0 text-brand-gold"></i>
                                    SPC Flooring
                                </a>
<a class="flex items-center text-gray-600 hover:text-brand-gold transition-colors duration-200 font-medium group/link" href="/pare/hdf-flooring">
<i class="fa-solid fa-caret-right text-[10px] mr-2 opacity-0 -translate-x-2 transition-all group-hover/link:opacity-100 group-hover/link:translate-x-0 text-brand-gold"></i>
                                    HDF Flooring
                                </a>
</div>
</div>
<!-- Column 2: Wall & Ceiling -->
<div>
<a class="block text-xs font-bold text-gray-400 uppercase tracking-wider mb-4 border-b border-gray-50 pb-2 hover:text-brand-gold transition-colors" href="/pare/wall-and-ceiling">Wall &amp; Ceiling</a>
<div class="grid grid-cols-2 gap-x-4 gap-y-3">
<a class="flex items-center text-gray-600 hover:text-brand-gold transition-colors duration-200 font-medium group/link" href="/pare/wpc/innov-plus">
<i class="fa-solid fa-caret-right text-[10px] mr-2 opacity-0 -translate-x-2 transition-all group-hover/link:opacity-100 group-hover/link:translate-x-0 text-brand-gold"></i>
                                    INNOV+
                                </a>
<a class="flex items-center text-gray-600 hover:text-brand-gold transition-colors duration-200 font-medium group/link" href="/pare/wpc/innov2-plus">
<i class="fa-solid fa-caret-right text-[10px] mr-2 opacity-0 -translate-x-2 transition-all group-hover/link:opacity-100 group-hover/link:translate-x-0 text-brand-gold"></i>
                                    INNOV2+
                                </a>
<a class="flex items-center text-gray-600 hover:text-brand-gold transition-colors duration-200 font-medium group/link" href="/pare/wpc/easy-plus">
<i class="fa-solid fa-caret-right text-[10px] mr-2 opacity-0 -translate-x-2 transition-all group-hover/link:opacity-100 group-hover/link:translate-x-0 text-brand-gold"></i>
                                    EASY+
                                </a>
<a class="flex items-center text-gray-600 hover:text-brand-gold transition-colors duration-200 font-medium group/link" href="/pare/wpc/acoustic">
<i class="fa-solid fa-caret-right text-[10px] mr-2 opacity-0 -translate-x-2 transition-all group-hover/link:opacity-100 group-hover/link:translate-x-0 text-brand-gold"></i>
                                    ACOUSTIC
                                </a>
<a class="flex items-center text-gray-600 hover:text-brand-gold transition-colors duration-200 font-medium group/link" href="/pare/wpc/luxe">
<i class="fa-solid fa-caret-right text-[10px] mr-2 opacity-0 -translate-x-2 transition-all group-hover/link:opacity-100 group-hover/link:translate-x-0 text-brand-gold"></i>
                                    LUXE
                                </a>
<a class="flex items-center text-gray-600 hover:text-brand-gold transition-colors duration-200 font-medium group/link" href="/pare/wpc/evolv-plus">
<i class="fa-solid fa-caret-right text-[10px] mr-2 opacity-0 -translate-x-2 transition-all group-hover/link:opacity-100 group-hover/link:translate-x-0 text-brand-gold"></i>
                                    EVOLV+
                                </a>
</div>
</div>
</div>
</div>
</div>
<div class="relative group h-full py-4 cursor-pointer">
<span class="hover:text-brand-gold transition-colors flex items-center gap-1">
                        Bekker <i class="fa-solid fa-chevron-down text-xs ml-1"></i>
</span>
<div class="dropdown-menu absolute top-full left-0 w-64 bg-white shadow-xl rounded-lg border border-gray-100 overflow-hidden py-2 hidden group-hover:block">
<div class="px-4 py-1 text-xs font-bold text-gray-400 uppercase tracking-wider">Flooring</div>
<a class="block px-4 py-2 hover:bg-gray-50 hover:text-brand-gold" href="/bekker/engineered-wood">Engineered Wood</a>
<a class="block px-4 py-2 hover:bg-gray-50 hover:text-brand-gold" href="/bekker/laminate-flooring">Laminate Flooring</a>
<a class="block px-4 py-2 hover:bg-gray-50 hover:text-brand-gold" href="/bekker/spc-flooring">SPC Flooring</a>
</div>
</div>
<a class="hover:text-brand-gold transition-colors" href="/cera/index">Cera</a>
<a class="hover:text-brand-gold transition-colors" href="/myk-laticrete/index">MYK Laticrete</a>
<button class="hover:text-brand-gold transition-colors text-gray-600 ml-2" onclick="document.getElementById('globalSearchModal').classList.remove('hidden'); document.getElementById('globalSearchInput').focus();" title="Search Products &amp; Catalogues">
<i class="fa-solid fa-magnifying-glass text-lg"></i>
</button>
<a class="px-5 py-2.5 bg-brand-black text-white rounded hover:bg-gray-800 transition-colors shadow-lg hover:shadow-xl" href="#contact">Get Quote</a>
</div>
<!-- Mobile Right Icons (Search + Hamburger Menu) -->
<div class="lg:hidden flex items-center gap-5">
<button class="text-gray-800 focus:outline-none hover:text-brand-gold transition-colors" onclick="document.getElementById('globalSearchModal').classList.remove('hidden'); document.getElementById('globalSearchInput').focus();">
<i class="fa-solid fa-magnifying-glass text-xl"></i>
</button>
<button class="text-gray-800 focus:outline-none hover:text-brand-gold transition-colors" onclick="document.getElementById('mobile-menu').classList.toggle('hidden')">
<i class="fa-solid fa-bars text-xl"></i>
</button>
</div>
</div>
<!-- Mobile Menu with Accordion Dropdowns -->
<div class="hidden bg-white border-t border-gray-100 absolute w-full shadow-lg h-screen overflow-y-auto pb-32 z-40 left-0" id="mobile-menu">
<div class="flex flex-col p-6 gap-2">
<details class="group border-b border-gray-50 pb-2">
<summary class="list-none flex justify-between items-center cursor-pointer py-3 font-bold text-gray-800">
                        Carpet Tiles
                        <span class="transition-transform duration-300 group-open:rotate-180">
<i class="fa-solid fa-chevron-down text-xs text-brand-gold"></i>
</span>
</summary>
<div class="flex flex-col gap-3 pl-4 py-2 border-l-2 border-gray-100 ml-2 animate-fade-in-down">
<a class="text-sm text-gray-600 hover:text-brand-gold" href="/welspun/carpet-tiles/celestial">Celestial</a>
<a class="text-sm text-gray-600 hover:text-brand-gold" href="/welspun/carpet-tiles/earthy-woods">Earthy Woods</a>
<a class="text-sm text-gray-600 hover:text-brand-gold" href="/welspun/carpet-tiles/meander">Meander</a>
<a class="text-sm text-gray-600 hover:text-brand-gold" href="/welspun/carpet-tiles/savy-street">Savy Street</a>
<a class="text-sm text-gray-600 hover:text-brand-gold" href="/welspun/carpet-tiles/urban-streaks">Urban Streaks</a>
</div>
</details>
<details class="group border-b border-gray-50 pb-2">
<summary class="list-none flex justify-between items-center cursor-pointer py-3 font-bold text-gray-800">
                        Welspun
                        <span class="transition-transform duration-300 group-open:rotate-180">
<i class="fa-solid fa-chevron-down text-xs text-brand-gold"></i>
</span>
</summary>
<div class="flex flex-col gap-3 pl-4 py-2 border-l-2 border-gray-100 ml-2">
<a class="text-sm text-gray-600 hover:text-brand-gold" href="/welspun/welspun-lick-n-lock/index">Click-N-Lock</a>
<a class="text-sm text-gray-600 hover:text-brand-gold" href="/welspun/multistile/index">Multistile</a>
<a class="text-sm text-gray-600 hover:text-brand-gold" href="/welspun/carpet-tiles/index">Carpet Tiles</a>
</div>
</details>
<details class="group border-b border-gray-50 pb-2">
<summary class="list-none flex justify-between items-center cursor-pointer py-3 font-bold text-gray-800">
                        Pare
                        <span class="transition-transform duration-300 group-open:rotate-180">
<i class="fa-solid fa-chevron-down text-xs text-brand-gold"></i>
</span>
</summary>
<div class="flex flex-col gap-3 pl-4 py-2 border-l-2 border-gray-100 ml-2 animate-fade-in-down">
<div class="text-xs font-bold text-gray-400 uppercase tracking-wider mt-1">Flooring</div>
<a class="text-sm text-gray-600 hover:text-brand-gold pl-2" href="/pare/lvt-flooring">LVT Flooring</a>
<a class="text-sm text-gray-600 hover:text-brand-gold pl-2" href="/pare/spc-flooring">SPC Flooring</a>
<a class="text-sm text-gray-600 hover:text-brand-gold pl-2" href="/pare/hdf-flooring">HDF Flooring</a>
<div class="text-xs font-bold text-gray-400 uppercase tracking-wider mt-2 border-t border-gray-50 pt-3 mb-1">
<a class="hover:text-brand-gold transition-colors" href="/pare/wall-and-ceiling">Wall &amp; Ceiling</a>
</div>
<a class="text-sm text-gray-600 hover:text-brand-gold pl-2" href="/pare/wpc/innov-plus">INNOV+</a>
<a class="text-sm text-gray-600 hover:text-brand-gold pl-2" href="/pare/wpc/innov2-plus">INNOV2+</a>
<a class="text-sm text-gray-600 hover:text-brand-gold pl-2" href="/pare/wpc/easy-plus">EASY+</a>
<a class="text-sm text-gray-600 hover:text-brand-gold pl-2" href="/pare/wpc/baffle">BAFFLE</a>
<a class="text-sm text-gray-600 hover:text-brand-gold pl-2" href="/pare/wpc/acoustic">ACOUSTIC</a>
<a class="text-sm text-gray-600 hover:text-brand-gold pl-2" href="/pare/wpc/luxe">LUXE</a>
<a class="text-sm text-gray-600 hover:text-brand-gold pl-2" href="/pare/wpc/evolv-plus">EVOLV+</a>
</div>
</details>
<details class="group border-b border-gray-50 pb-2">
<summary class="list-none flex justify-between items-center cursor-pointer py-3 font-bold text-gray-800">
                        Bekker
                        <span class="transition-transform duration-300 group-open:rotate-180">
<i class="fa-solid fa-chevron-down text-xs text-brand-gold"></i>
</span>
</summary>
<div class="flex flex-col gap-3 pl-4 py-2 border-l-2 border-gray-100 ml-2">
<a class="text-sm text-gray-600 hover:text-brand-gold" href="/bekker/engineered-wood">Engineered Wood</a>
<a class="text-sm text-gray-600 hover:text-brand-gold" href="/bekker/laminate-flooring">Laminate Flooring</a>
<a class="text-sm text-gray-600 hover:text-brand-gold" href="/bekker/spc-flooring">SPC Flooring</a>
</div>
</details>
<a class="py-3 font-bold text-gray-800 hover:text-brand-gold border-b border-gray-50" href="/kitchen/index.html">Modular Kitchens</a>
<a class="py-3 font-bold text-gray-800 hover:text-brand-gold border-b border-gray-50" href="/cera/index">Cera</a>
<a class="py-3 font-bold text-gray-800 hover:text-brand-gold border-b border-gray-50" href="/myk-laticrete/index">MYK Laticrete</a>
<a class="py-3 font-bold text-gray-800 hover:text-brand-gold border-b border-gray-50" href="/brochure">Brochure</a>
<button class="py-3 font-bold text-left text-gray-800 hover:text-brand-gold border-b border-gray-50 flex items-center justify-between" onclick="document.getElementById('mobile-menu').classList.add('hidden'); document.getElementById('globalSearchModal').classList.remove('hidden'); document.getElementById('globalSearchInput').focus();">
                        Search <i class="fa-solid fa-magnifying-glass"></i>
</button>
<a class="bg-brand-black text-white text-center py-4 rounded mt-6 font-medium shadow-lg" href="/index.html#contact" onclick="document.getElementById('mobile-menu').classList.add('hidden')">Get Quote</a>
</div>
</div>
</nav>
"""

def update_all_pages(root_dir="."):
    root_path = Path(root_dir)
    html_files = list(root_path.glob("**/*.html"))
    print(f"Kul {len(html_files)} HTML files mili hain. Sabhi ko update kiya ja raha hai...\n")

    success_count = 0
    for file_path in html_files:
        # Script file ko skip karne ke liye
        if file_path.name == "update_navbar.py":
            continue
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")

            # Har file me <nav id="navbar"> ko dhundhein
            existing_nav = soup.find("nav", id="navbar")

            if existing_nav:
                # Naye navbar code se replace kar dein
                new_nav_soup = BeautifulSoup(NEW_NAVBAR_HTML.strip(), "html.parser")
                existing_nav.replace_with(new_nav_soup)

                # File ko save kar dein
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(soup))
                print(f"[SUCCESS] Updated: {file_path}")
                success_count += 1
            else:
                print(f"[SKIPPED] <nav id='navbar'> nahi mila: {file_path}")

        except Exception as e:
            print(f"[ERROR] {file_path} ko process karne me error aaya: {e}")

    print(f"\nKaam pura ho gaya! Total {success_count} pages successfully update ho chuke hain.")

if __name__ == "__main__":
    update_all_pages()
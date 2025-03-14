var app = (function(){
    let pages = [];
    let links = [];
    let currentIndex = 0;
    let root_vars = "";

    document.addEventListener("DOMContentLoaded", function(){
        root_vars = document.querySelector(':root');
        pages = document.querySelectorAll('[data-page]');
        links = document.querySelectorAll('[data-role="link"]');
        
        [].forEach.call(links, function(link){
            link.addEventListener("click", navigate)
        });

        pages[currentIndex].classList.add("active");
        links[currentIndex].classList.add("active");  // Make sure the first link is active

    });

    function navigate(ev){
        ev.preventDefault();
        let id = ev.currentTarget.href.split("#")[1];

        let newIndex = [...pages].findIndex(page => page.id === id);

        let currentPage = pages[currentIndex];
        let nextPage = pages[newIndex];

        // Change direction of transform animation
        let direction = currentIndex > newIndex ? "100%" : "-100%";

        root_vars.style.setProperty('--direction', direction);

        currentPage.classList.remove('active');
        currentPage.classList.add('hidden');

        links[currentIndex].classList.remove('active');
        links[newIndex].classList.add('active');  // Move active class to the clicked link

        currentPage.classList.remove('hidden');
        nextPage.classList.add('active');

        currentIndex = newIndex;
        
        return false;
    }

    return {
        pages,
        links,
        xhr: ajax
    }
})();

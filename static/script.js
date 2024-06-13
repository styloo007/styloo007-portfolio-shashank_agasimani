document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll('.card');
    const options = {
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, options);

    cards.forEach(card => {
        observer.observe(card);
    });
});



document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll('.project-card');
    const projectsPerPage = 2;
    let currentPage = 0;
  
    function displayProjects() {
      const startIndex = currentPage * projectsPerPage;
      const endIndex = Math.min(startIndex + projectsPerPage, cards.length);
  

      for (let i = 0; i < cards.length; i++) {
        cards[i].style.display = 'none';
      }
  
      for (let i = startIndex; i < endIndex; i++) {
        cards[i].style.display = 'block';
      }
    }
  
    function updatePaginationButtons() {
      const prevBtn = document.getElementById("prev-btn");
      const nextBtn = document.getElementById("next-btn");
  
      prevBtn.disabled = currentPage === 0;
      nextBtn.disabled = currentPage + 1 >= Math.ceil(cards.length / projectsPerPage);
    }
  
    function goToPreviousPage() {
      if (currentPage > 0) {
        currentPage--;
        displayProjects();
        updatePaginationButtons();
      }
    }
  
    function goToNextPage() {
      if (currentPage + 1 < Math.ceil(cards.length / projectsPerPage)) {
        currentPage++;
        displayProjects();
        updatePaginationButtons();
      }
    }

    displayProjects();
    updatePaginationButtons();
  

    document.getElementById("prev-btn").addEventListener("click", goToPreviousPage);
    document.getElementById("next-btn").addEventListener("click", goToNextPage);
  });
  



export class HeaderScroll {
    constructor() {
        this.header = document.querySelector('header');
        this.init();
    }

    init() {
        window.addEventListener('scroll', () => this.handleScroll());
    }

    handleScroll() {
        if (!this.header) return;
        
        if (window.scrollY > 100) {
            this.header.style.background = 'rgba(37, 99, 235, 0.95)';
            this.header.style.backdropFilter = 'blur(10px)';
        } else {
            this.header.style.background = 'linear-gradient(135deg, var(--primary-color), var(--secondary-color))';
            this.header.style.backdropFilter = 'none';
        }
    }
}
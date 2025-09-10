export class Navigation {
    constructor() {
        this.hamburger = document.querySelector('.hamburger');
        this.navLinks = document.querySelector('.nav-links');
        this.init();
    }

    init() {
        if (this.hamburger) {
            this.hamburger.addEventListener('click', () => this.toggleMobileMenu());
        }
    }

    toggleMobileMenu() {
        const isVisible = this.navLinks.style.display === 'flex';
        this.navLinks.style.display = isVisible ? 'none' : 'flex';
        
        // Add mobile menu styling when opened
        if (!isVisible) {
            this.navLinks.classList.add('mobile-menu-open');
        } else {
            this.navLinks.classList.remove('mobile-menu-open');
        }
    }
}
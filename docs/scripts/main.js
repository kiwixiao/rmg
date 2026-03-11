// Main application entry point
import { Navigation } from './modules/navigation.js';
import { SmoothScroll } from './modules/smooth-scroll.js';
import { HeaderScroll } from './modules/header-scroll.js';
import { Animations } from './modules/animations.js';

class App {
    constructor() {
        this.init();
    }

    init() {
        // Initialize modules when DOM is loaded
        document.addEventListener('DOMContentLoaded', () => {
            new Navigation();
            new SmoothScroll();
            new HeaderScroll();
            new Animations();

            console.log('CFD Website loaded successfully');
        });
    }
}

// Initialize the application
new App();
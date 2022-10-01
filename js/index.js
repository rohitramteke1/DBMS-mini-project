// Container
const home = document.getElementById('home');
const about = document.getElementById('about');
const help = document.getElementById('help');
const contact = document.getElementById('contact');
const footer = document.getElementById('footer');

// Navbar-links
const home_link = document.getElementById('home-link')
const about_link = document.getElementById('about-link')
const contact_link = document.getElementById('contact-link')
const help_link = document.getElementById('help-link')


class Container_Display{
    constructor() {
        // container's
        this.home = home;
        this.about = about;
        this.help = help;
        this.contact = contact;
        this.footer = footer;

        // navbar links
        this.home_link = home_link;
        this.about_link = about_link;
        this.contact_link = contact_link;
        this.help_link = help_link;

    }
    container_display_home() {
        this.home.style.display = 'block';
        this.about.style.display = 'none';
        this.help.style.display = 'none';
        this.contact.style.display = 'none';
    }
    container_display_about() {
        this.home.style.display = 'none';
        this.about.style.display = 'block';
        this.help.style.display = 'none';
        this.contact.style.display = 'none';
    }
    container_display_help() {
        this.home.style.display = 'none';
        this.about.style.display = 'none';
        this.help.style.display = 'block';
        this.contact.style.display = 'none';
    }
    container_display_contact() {
        this.home.style.display = 'none';
        this.about.style.display = 'none';
        this.help.style.display = 'none';
        this.contact.style.display = 'block';
    }
}

class Click_On_Navbar_Links extends Container_Display {
    constructor() {
        super();
    }
    click_on_home() {
        this.home_link.addEventListener("click", ()=> {
            this.container_display_home();
        })
    }
    click_on_about() {
        this.about_link.addEventListener("click", ()=> {
            this.container_display_about();
        })
    }
    click_on_help() {
        this.help_link.addEventListener("click", ()=> {
            this.container_display_help();
        })
    }
    click_on_contact() {
        this.contact_link.addEventListener("click", ()=> {
            this.container_display_contact();
        })
    }
}

root = new Click_On_Navbar_Links();

// Show the Home-Page whenever we refresh the Page
root.container_display_home();

// Hide the respective-container on the click events
root.click_on_home();
root.click_on_about();
root.click_on_contact();
root.click_on_help();
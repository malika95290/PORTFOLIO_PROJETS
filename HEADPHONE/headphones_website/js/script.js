const navMenu = document.getElementById('nav-menu'),
        navToggle = document.getElementById('nav-toggle'),
        navClose = document.getElementById('nav-close')

// MENU SHOW

if (navToggle) {
    navToggle.addEventListener('click', ()=> {
        navMenu.classList.add('show-menu')
    })
}

// MENU HIDDEN

if (navClose) {
    navClose.addEventListener('click', ()=> {
        navMenu.classList.remove('show-menu')
    })
 }

// REMOVE MENU MOBILE

const navLink = document.querySelectorAll('.nav__link')

// Lorsqu'on clique sur chacun des nav__link, on enlève la class show_menu

const linkAction = () => {
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show-menu')
}

navLink.forEach(n => n.addEventListener('click', linkAction))

// ADD BLUR HEADER

const blurHeader = () =>{
    const header = document.getElementById('header')
    // When the scroll is greater than 50 viewport innerHeight, add the blur header
    this.scrollY >= 50 ? header.classList.add('blur-header')
                       : header.classList.remove('blur-header')
} 

window.addEventListener('scroll', blurHeader)

// SWIPER FAVORITES

let swiperFavorite = new Swiper('.favorite__swiper', {
    loop: true,
    slidesPerview: 'auto',
    centeredSlides: 'auto',
    grabCursor: true,

    breakpoints: {
        768: {
            slidesPerView: 3
        }
    }
})

// SHOW SCROLL UP

const scrollUp = () =>{
    const scrollUp = document.getElementById('scroll-up')
    //When the scroll is higher than 350 viexport height, add the scroll-up
    this.scrollY >= 350 ? scrollUp.classList.add('show-scroll')
                        : scrollUp.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollUp)

// SCROLL SECTIONS ACTIVE LINK 

const sections = document.querySelectorAll('section[id]')

const scrollActive = () => {
    const scrollDown = window.scrollY

    sections.forEach(current =>{
        const sectionHeight = current.offsetHeight,
                sectionTop = current.offsetTop - 58,
                sectionId = current.getAttribute('id'),
                sectionsClass = document.querySelector('.nav__menu a[href*=' + sectionId + ']')

        if (scrollDown > sectionTop && scrollDown <= sectionTop + sectionHeight){
            sectionsClass.classList.add('active-link')
        }else{
            sectionsClass.classList.remove('active-link')
        }
    })
}
window.addEventListener('scroll', scrollActive)

// SCROLL REVEAL ANIMATION

const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 400,
    reset: true, // Animations repeat
})

sr.reveal(`.home__social, .favorite__container, .sponsor__container, .footer`)
sr.reveal(`.home__title span:nth-child(1)`, {origin: 'left', opacity: 1})
sr.reveal(`.home__title span:nth-child(3)`, {origin: 'right', opacity: 1})
sr.reveal(`.home__tooltip, .home__button, .model__button`, {origin: 'bottom'})
sr.reveal(`.about__data`, {origin: 'left'})
sr.reveal(`.about__img, .model__tooltip`, {origin: 'right'})

export function basicSearchToggle() {
    const body = document.documentElement.querySelector('body')
    if (localStorage.getItem('darkMode') === null) {
        localStorage.setItem('darkMode', 'false'); // só define se ainda não tiver nada
    }
    if (localStorage.getItem('darkMode') === 'true') {
        body.classList.add('darkmode');
        
    } else {
        body.classList.remove('darkmode');
    }

    document.addEventListener('DOMContentLoaded', () => {
        const logo = document.getElementById("logo")
        const footerElement = document.querySelector('search-footer')
        const darkModeButton = footerElement.shadowRoot.getElementById('darkmode')

        if (localStorage.getItem('darkMode') === 'true') {
            logo.src = "../assets/images/logo_light.png"
            logo.style.visibility = 'visible'
            darkModeButton.innerText = "Tema escuro: Ativado"
        }else{
            logo.src = "../assets/images/logo_color.png"
            logo.style.visibility = 'visible'
            darkModeButton.innerText = "Tema escuro: Desativado"
        }
    })

}

export function advancedSearchToggle() {
    const body = document.documentElement.querySelector('body')

    if (localStorage.getItem('darkMode') === null) {
        localStorage.setItem('darkMode', 'false'); // só define se ainda não tiver nada
    }

    if (localStorage.getItem('darkMode') === 'true') {
        body.classList.add("darkmode");
    } else {
        body.classList.remove("darkmode");
    }

    document.addEventListener('DOMContentLoaded', () => {
        const logo = document.getElementById("logo_svg")
        if (localStorage.getItem('darkMode') === 'true') {
            logo.src = "../assets/images/googlelogo_light_clr_74x24px.svg"
            logo.style.visibility = 'visible'
        }else{
            logo.src = "../assets/images/googlelogo_clr_74x24px.svg"
            logo.style.visibility = 'visible'
        }

    })
}
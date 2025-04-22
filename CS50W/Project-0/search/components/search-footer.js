class SearchFooter extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' })

        this.shadowRoot.innerHTML = `
        <style> 
            footer {
                /* min-height: 8vh; */
                /* ocupa 8% da altura da tela */
                background-color: #f2f2f2;
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                z-index: 1;
            }

            footer.hidden {
                transform: translateY(100%);
            }

            #upper-footer {
                padding: 0px 30px;
                color: #1f1f1f;
                border-bottom: 1px solid #dadce0;
                font-size: 15px;
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
                unicode-bidi: isolate;
            }

            #bottom-footer {
                justify-content: space-evenly;
                display: flex;
                flex-wrap: wrap;
                padding: 0 20px;
                unicode-bidi: isolate;
            }

            #bottom-footer div {
                display: flex;
                flex-wrap: wrap;
            }

            .a-footer {
                display: block;
                padding: 15px;
                white-space: nowrap;
                color: #1f1f1f;
                cursor: pointer;
                text-decoration: none;
            }

            a:hover {
                text-decoration: underline;
            }


            .config {
                background-color: #fff;
                position: absolute;
                bottom: 100%;
                left: -25px;
                width: 180px;
                height: auto;
                visibility: hidden;
                border-radius: 8px;
                box-shadow: 0 2px 10px 0 rgba(0, 0, 0, 0.2);
                z-index: 1001;
            }

            .config-item {
                display: flex;
                justify-content: left;
                width: 100%;
                padding: 0px 10px 0px 10px;

            }

            .config-item:hover {
                background-color: #e5e5e5;
            }

            .config-item a {
                color: #1f1f1f;
                line-height: normal;
                align-items: center;
                display: flex;
                justify-content: space-between;
                padding-bottom: 4px;
                padding-top: 4px;
                cursor: pointer;
                line-height: 23px;
                white-space: nowrap;
                font-size: 14px;
                text-decoration: none;
}
        </style>

        <div id="upper-footer">
            <p>Brasil</p>
        </div>
        <div id="bottom-footer">
            <div>
                <a class="a-footer" href="https://about.google/">Sobre</a>
                <a class="a-footer" href="https://ads.google.com/">Publicidade</a>
                <a class="a-footer" href="https://www.google.com/business/">Negócios</a>
                <a class="a-footer" href="https://www.google.com/search/howsearchworks/">Como funciona a Pesquisa</a>
            </div>
            <div>
                <a class="a-footer" href="https://policies.google.com/privacy">Privacidade</a>
                <a class="a-footer" href="https://policies.google.com/terms">Termos</a>
                <div style="position: relative;">
                    <a id="config-btn" class="a-footer" href="">Configurações</a>
                    <div id="config-menu" class="config">
                        <div class="config-item">
                            <a href="">Idioma</a>
                        </div>
                        <div class="config-item">
                            <a href="">Pesquisa Avancada</a>
                        </div>
                        <div class="config-item">
                            <a href="">Tema escuro: Desativado</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
     
        `

        const configBtn = this.shadowRoot.getElementById("config-btn");
        const menu = this.shadowRoot.getElementById("config-menu");

        configBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            menu.style.visibility = menu.style.visibility === 'visible' ? 'hidden' : 'visible';
        });

        document.addEventListener('click', (e) => {
            const path = e.composedPath();
            if (!path.includes(configBtn) && !path.includes(menu)) {
                menu.style.visibility = 'hidden';
            }
        })

    }
}

customElements.define('search-footer', SearchFooter)

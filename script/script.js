class CoolTimer extends HTMLElement {
  constructor() {
    super();
    const template = document.getElementById("cool-timer");
    const templateContent = template.content;
    this.attachShadow({ mode: "open" }).appendChild(
      templateContent.cloneNode(true),
    );
  }
}

customElements.define("cool-timer", CoolTimer);

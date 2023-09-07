async function addText() {
    let div = document.getElementById("ayuda")
    let txt = await eel.hello()()
    div.innerHTML += txt
}
// Gets proposition and stores it in Python
async function agregar() {
    // Get input
    const input = document.getElementById("prop").value;
    // Store propositions Container
    let container = document.getElementById("propContainer");

    // Store input in python
    if (input != ""){
        // Send value to Python and add it to GUI
        let n = await eel.add_prop(input)()
        container.innerHTML += `<div id='proposicion'> \
                                    <h4>${n}</h4> \
                                    <p>${input}</p> \
                                </div>`
        
        // Resetting input in GUI
        document.getElementById("prop").value = ""
        // Resetting operations in GUI
        document.getElementById("operaciones").innerHTML = "";
    }
    else {
        alert("Introduzca una proposición")
    }
}

// Automatic initiation of propositions (total of 20)
async function autoIni() {
    // Store propositions Container
    let container = document.getElementById("propContainer");
    // Clean GUI before execution
    container.innerHTML = ""
    document.getElementById("operaciones").innerHTML = "";
    // Get auto_prop dict after setting it on Python
    let props = await eel.auto_ini()()
    // Iterate over it, adding elements
    for (const [key, prop] of Object.entries(props)) {
        container.innerHTML += `<div id='proposicion'> \
                                    <h4>${key}</h4> \
                                    <p>${prop}</p> \
                                </div>`
      }

}

// Resets every element by rebooting the page
async function reiniciar() {
    location.reload()
    await eel.reset()()
}


// Gets and operates manual operation
async function manualExe() {
    // Getting operation
    const operacion = document.getElementById("operacionManual").value

    // Validating it
    if (await eel.valid(operacion)()) {
        // Evaluate operation in Python
        resultado = await eel.operacion_manual(operacion)()
        // Set result in GUI
        document.getElementById("operaciones").innerHTML = 
                    `<div class="bottom"> 
                        <h4 class="resultado"> RESULTADO </h4>
                        <p id="manual">${resultado}</p>
                    </div>`
    }
    else {
        alert("Operación no válida")
    }
    
}

// Gets and operates automatic operation
async function autoExe() {
    // Getting prop_index
    const index = document.getElementById("operacionAutomatica").value

    // Validating existence
    if (await eel.exists(index)()) {
        const conjunción = await eel.conjunction(index)()
        const disjunción = await eel.disjunction(index)()
        const condicional = await eel.conditional(index)()
        const negación = await eel.negation(index)()

        document.getElementById("operaciones").innerHTML =
        `<div class="operacion">
            <h4 class="resultado"> RESULTADOS </h4>
            <div class="grid">
                <div class="top">
                    <h4 class="titulo">Conjunción</h4>
                    <p id="conjunction"> ${conjunción} <br></p>
                </div>
                <div class="top">
                    <h4 class="titulo">Disjunción</h4>
                    <p id="disjunction"> ${disjunción}</p>
                </div>
                <div class="top">
                    <h4 class="titulo">Condicional</h4>
                    <p id="conditional"> ${condicional}</p>
                </div>
            </div>
            <div class="bottom">
                <h4 class="titulo">Negación</h4>
                <p id="negation"> ${negación}</p>
            </div>
        </div>`
    }
    else {
        alert("Proposición inexistente")
    }
}
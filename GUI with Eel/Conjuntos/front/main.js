// Obtener input de caja de texto
function getInput() {
    let input = document.getElementById("nInput").value
    const re = new RegExp("^[1-9]$")

    // Llamar función para añadir operaciones a la GUI
    if (re.test(input)) {
        addOperations(input)
    }
    else {
        alert("Input inválido, ingrese un número entre 1 y 9")
    }
}


// Añadir operaciones a cajas de texto
async function addOperations(set) {
    let U = document.getElementById("union")
    U.innerHTML = await eel.union(set)()

    let I = document.getElementById("intersection")
    I.innerHTML = await eel.intersection(set)()

    let D = document.getElementById("difference")
    D.innerHTML = await eel.difference(set)()

    let C = document.getElementById("complement")
    C.innerHTML = await eel.complement(set)()
}
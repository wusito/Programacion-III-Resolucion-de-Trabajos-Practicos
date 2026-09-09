// EJERCICO 1
const inputFechaNac = document.getElementById('fechanac');
inputFechaNac.addEventListener('change', validarFechaNacimiento);

function validarFechaNacimiento() {
    const fechaIngresadaValue = inputFechaNac.value;

    if (!fechaIngresadaValue) return;

    const fechaIngresada = new Date(fechaIngresadaValue);
    const fechaActual = new Date();
    fechaActual.setHours(0, 0, 0, 0);
    fechaIngresada.setHours(0, 0, 0, 0);

    if (fechaIngresada > fechaActual) {
        alert("La fecha de nacimiento no puede ser posterior a la fecha actual.");
        inputFechaNac.value = ""; // Limpia el campo inválido
        return false;
    }

    return true;
}


// EJERCICO 2
const inputDNI = document.getElementById('dni');
inputDNI.addEventListener('change', validarDigitosDNI);

function validarDigitosDNI() {
    const dniValue = inputDNI.value.trim();

    if (!dniValue) return false;

    if (dniValue.toString().length !== 8) {
        alert("El DNI debe contener 8 dígitos.");
        inputDNI.value = ""; // Limpia el campo inválido
        return false;
    }

    return true;
}


// EJERCICIO 3

// EJERCICO 1 ------------------------------------------------------------------------------------------------
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
        inputFechaNac.value = ""; // Limpia el campo inválido.
        return false;
    }

    return true;
}



// EJERCICO 2 ------------------------------------------------------------------------------------------------
const inputDNI = document.getElementById('dni');
inputDNI.addEventListener('change', validarDigitosDNI);

function validarDigitosDNI() {
    const dniValue = inputDNI.value.trim();

    if (!dniValue) return false;

    if (dniValue.toString().length !== 8) {
        alert("El DNI debe contener 8 dígitos.");
        inputDNI.value = ""; // Limpia el campo inválido.
        return false;
    }

    return true;
}



// EJERCICIO 3.1 ---------------------------------------------------------------------------------------------
class Actividad {
    
    constructor(nombre, lugar, dia, horario, cupo, estado){ 
        this.nombre = nombre;
        this.lugar = lugar;
        this.dia = dia;
        this.horario = horario;
        this.cupo = cupo;
        this.estado = "Disponible";
    }
}



// EJERCICIO 3.2 ---------------------------------------------------------------------------------------------
class SistemaDeportes {
    
    constructor() {
        this.actividades = []; // Lista donde se guardan las actividades.
    }

    // Método para recibir un objeto Actividad y agregarlo a la lista.
    agregarActividad(actividad) {
        this.actividades.push(actividad);
        console.log(`Actividad agregada: ${actividad.nombre}`);
    }
}



// EJERCICIO 3.3 ---------------------------------------------------------------------------------------------
const actividad1 = new Actividad("Fútbol", "Cancha Principal, Campus Universitario.", "Lunes y Miércoles", "18:00 a 20:00", 15);
const actividad2 = new Actividad("Básquet", "Pabellón de Básquet, Campus Universitario.", "Martes y Jueves", "18:00 a 20:00", 12);
const actividad3 = new Actividad("Vóley", "Pabellón de Vóley, Campus Universitario.", "Miércoles y Viernes", "18:00 a 20:00", 10);
const actividad4 = new Actividad("Atletismo", "Circuito de Atletismo, Campus Universitario.", "Lunes y Jueves", "18:00 a 20:00", 8);

// Instanciamos la clase de SistemaDeportes.
const miSportSystem = new SistemaDeportes();

// Agrega las actividades al sistema de deportes.
miSportSystem.agregarActividad(actividad1);
miSportSystem.agregarActividad(actividad2);
miSportSystem.agregarActividad(actividad3);
miSportSystem.agregarActividad(actividad4);



// EJERCICIO 4 -----------------------------------------------------------------------------------------------
function mostrarActividadesDeportivas(sportsystem) {
    const cuerpoTabla = document.getElementById("cuerpoTabla");
    cuerpoTabla.innerHTML = ""; //Limpia la tabla.

    // Recorre el array.
    sportsystem.actividades.forEach(actividad => {
        
        // Crea la fila y los componentes dinámicamente.
        cuerpoTabla.innerHTML += `
            <tr>
                <td>${actividad.nombre}</td>
                <td>${actividad.lugar}</td>
                <td>${actividad.dia}</td>
                <td>${actividad.horario}</td>
                <td>${actividad.cupo}</td>
                <td>${actividad.estado}</td>
            </tr>
        `;
    });
}

// Llama a la función y pasa la instancia para que se rellene la tabla.
mostrarActividadesDeportivas(miSportSystem);



// EJERCICIO 5 -----------------------------------------------------------------------------------------------
document.getElementById('btnGenerar').addEventListener('click', (e) => {
    e.preventDefault();

    const cantidadInput = document.getElementById('cantidadParticipantes');
    const cantidad = parseInt(cantidadInput.value);
    const contenedor = document.getElementById('contenedorParticipantes');

    // Valida los límites establecidos en el input.
    if (isNaN(cantidad) || cantidad < 1 || cantidad > 10) {
        alert("Por favor, ingrese un número válido entre 1 y 10.");
        return;
    }

    // Limpia el contenido previo para evitar acumulaciones.
    contenedor.innerHTML = '';

    // Genera los bloques dinámicamente.
    for (let i = 1; i <= cantidad; i++) {
        // Crea el contenedor tipo TARJETA (Card) para cada participante.
        const divParticipante = document.createElement('div');
        divParticipante.className = 'card mb-4 border-info';

        // Crea el título del bloque (Cabecera de la tarjeta).
        const cabecera = document.createElement('div');
        cabecera.className = 'card-header bg-info text-white fw-bold';
        cabecera.textContent = `Datos del Participante ${i}`;
        divParticipante.appendChild(cabecera);

        // Crea el cuerpo de la tarjeta donde irán los inputs.
        const cuerpoCard = document.createElement('div');
        cuerpoCard.className = 'card-body row g-3';

        // Define los campos y el tamaño que ocuparán en pantalla.
        const campos = [
            { label: 'Apellido y Nombre:', type: 'text', id: `nombre_${i}`, col: 'col-md-12' },
            { label: 'DNI:', type: 'text', id: `dni_${i}`, col: 'col-md-6' },
            { label: 'Fecha de nacimiento:', type: 'date', id: `fecha_${i}`, col: 'col-md-6' },
            { label: 'Sexo:', type: 'select', id: `sexo_${i}`, opciones: ['Seleccionar', 'Masculino', 'Femenino', 'Otro'], col: 'col-md-6' },
            { label: 'Nivel:', type: 'select', id: `nivel_${i}`, opciones: ['Seleccionar', 'Principiante', 'Intermedio', 'Avanzado'], col: 'col-md-6' }
        ];

        // Construye los elementos HTML de cada campo.
        campos.forEach(campo => {
            const grupo = document.createElement('div');
            grupo.className = campo.col;

            const label = document.createElement('label');
            label.className = 'form-label mb-1 text-muted small fw-bold';
            label.textContent = campo.label;
            label.setAttribute('for', campo.id);
            grupo.appendChild(label);

            let input;
            if (campo.type === 'select') {
                input = document.createElement('select');
                input.className = 'form-select';
                campo.opciones.forEach(opc => {
                    const option = document.createElement('option');
                    option.value = opc === 'Seleccionar' ? '' : opc.toLowerCase();
                    option.textContent = opc;
                    input.appendChild(option);
                });
            } else {
                input = document.createElement('input');
                input.type = campo.type;
                input.className = 'form-control';
            }

            input.required = true;
            input.id = campo.id;
            input.name = campo.id;
            
            grupo.appendChild(input);
            cuerpoCard.appendChild(grupo);
        });

        // Inserta el cuerpo a la tarjeta, y la tarjeta al contenedor principal.
        divParticipante.appendChild(cuerpoCard);
        contenedor.appendChild(divParticipante);
    }
});
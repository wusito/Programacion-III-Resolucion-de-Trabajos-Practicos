document.addEventListener("DOMContentLoaded", () => {
    // EJERCICO 1 ------------------------------------------------------------------------------------------------
    // Función delegada para validar cualquier input de fecha de nacimiento (estático o dinámico)
    document.addEventListener('change', (e) => {
        if (e.target && (e.target.id === 'fechanac' || e.target.id.startsWith('fecha_') || e.target.id.startsWith('fechanac_'))) {
            const inputFechaNac = e.target;
            const fechaIngresadaValue = inputFechaNac.value;
            if (!fechaIngresadaValue) return;

            const fechaIngresada = new Date(fechaIngresadaValue);
            const fechaActual = new Date();
            fechaActual.setHours(0, 0, 0, 0);
            fechaIngresada.setHours(0, 0, 0, 0);

            if (fechaIngresada > fechaActual) {
                alert("La fecha de nacimiento no puede ser posterior a la fecha actual.");
                inputFechaNac.value = "";
                return false;
            }
            return true;
        }
    });



    // EJERCICO 2 ------------------------------------------------------------------------------------------------
    // Función delegada para validar cualquier input de DNI (estático o dinámico)
    document.addEventListener('change', (e) => {
        if (e.target && (e.target.id === 'dni' || e.target.id.startsWith('dni_'))) {
            const inputDNI = e.target;
            const dniValue = inputDNI.value.trim();
            if (!dniValue) return false;

            if (dniValue.toString().length !== 8) {
                alert("El DNI debe contener 8 dígitos.");
                inputDNI.value = "";
                return false;
            }
            return true;
        }
    });



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
        if (!cuerpoTabla) return;

        cuerpoTabla.innerHTML = ""; // Limpia la tabla.

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
    const generarParticipantes = () => {
        const cantidadInput = document.getElementById('cantidadParticipantes');
        if (!cantidadInput) return;
        const cantidad = parseInt(cantidadInput.value);
        const contenedor = document.getElementById('contenedorParticipantes');
        if (!contenedor) return;

        // Valida los límites establecidos en el input.
        if (isNaN(cantidad) || cantidad < 1 || cantidad > 10) {
            alert("Por favor, ingrese un número válido entre 1 y 10.");
            return;
        }

        // Limpia el contenido previo del contenedor dinámico.
        contenedor.innerHTML = '';

        // Genera los bloques dinámicamente con la misma estructura visual original.
        for (let i = 1; i <= cantidad; i++) {
            const divParticipante = document.createElement('div');
            divParticipante.className = 'row g-3 p-0 m-0 w-100 mb-4';

            // Si hay más de un participante, muestra un subtítulo integrador.
            let titulo = '';
            if (cantidad > 1) {
                titulo = `<div class="col-12"><h6 class="text-warning fw-bold mb-2">Participante ${i}</h6></div>`;
            }

            divParticipante.innerHTML = `
                ${titulo}
                <div class="col-md-4 position-relative">
                    <label for="nombre_${i}" class="form-label">Nombre:</label>
                    <input
                        type="text"
                        class="form-control"
                        id="nombre_${i}"
                        name="nombre_${i}"
                        placeholder="Ejemplo: Juan"
                        required
                    />
                </div>

                <div class="col-md-4 position-relative">
                    <label for="apellido_${i}" class="form-label">Apellido:</label>
                    <input
                        type="text"
                        class="form-control"
                        id="apellido_${i}"
                        name="apellido_${i}"
                        placeholder="Ejemplo: Pérez"
                        required
                    />
                </div>

                <div class="col-md-4 position-relative">
                    <label for="dni_${i}" class="form-label">DNI:</label>
                    <input
                        type="number"
                        class="form-control"
                        id="dni_${i}"
                        name="dni_${i}"
                        placeholder="Ingresar DNI sin puntos"
                        required
                    />
                </div>

                <div class="col-md-4 position-relative">
                    <label for="fechanac_${i}" class="form-label">Fecha de Nacimiento:</label>
                    <input type="date" class="form-control" id="fechanac_${i}" name="fechanac_${i}" required />
                </div>

                <div class="col-md-4 position-relative">
                    <label for="email_${i}" class="form-label">Correo Electrónico:</label>
                    <div class="input-group has-validation">
                        <span class="input-group-text">@</span>
                        <input type="email" class="form-control" id="email_${i}" name="email_${i}" required />
                    </div>
                </div>

                <div class="col-md-4 position-relative">
                    <label for="telefono_${i}" class="form-label">Teléfono:</label>
                    <input
                        type="tel"
                        class="form-control"
                        id="telefono_${i}"
                        name="telefono_${i}"
                        placeholder="+54 38 3412-3456"
                        required
                    />
                </div>

                <div class="col-md-4 position-relative">
                    <label>Sexo:</label>
                    <div class="form-check">
                        <input
                            class="form-check-input"
                            type="radio"
                            name="sexo_${i}"
                            id="femenino_${i}"
                            value="femenino"
                        />
                        <label class="form-check-label" for="femenino_${i}">Femenino</label>
                    </div>
                    <div class="form-check">
                        <input
                            class="form-check-input"
                            type="radio"
                            name="sexo_${i}"
                            id="masculino_${i}"
                            value="masculino"
                            checked
                        />
                        <label class="form-check-label" for="masculino_${i}">Masculino</label>
                    </div>
                </div>
            `;

            contenedor.appendChild(divParticipante);
        }
    };

    const btnGenerar = document.getElementById('btnGenerar');
    if (btnGenerar) {
        btnGenerar.addEventListener('click', (e) => {
            e.preventDefault();
            generarParticipantes();
        });
    }

    // Genera el campo inicial al cargar la página
    generarParticipantes();
});